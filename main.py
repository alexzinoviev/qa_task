import requests
import time
import socket
import json
from optparse import OptionParser
from requests import ConnectTimeout, ReadTimeout, ConnectionError
import threading

INPUT_FILE = 'web_list.txt'
OUTPUT_FOLDER = 'output_data/'
BASE_URL = 'http://'


parser = OptionParser()
parser.add_option("-f", "--file", help="Write the test output to a JSON file", default="output_")
parser.add_option("-t", "--timeout", help="Set connection timeout", default=1, type="float")
parser.add_option("-u", "--user", help="Specify the user agent the requests are made with")
options, args = parser.parse_args()


def main(url, timeout, output_file_name):
    ip_address = None
    response_code = None
    number_of_redirects = None
    content_load_time = None
    tcp_connection_time = None
    dns_resolution_time = None
    headers = {'user-agent': options.user}
    try:
        r = requests.get(BASE_URL + url, timeout=timeout, headers=headers)
        response_code = r.status_code
        ip_address, dns_resolution_time = get_ip_address(url)
        tcp_connection_time = get_tcp_connection_time(ip_address)
        number_of_redirects = len(r.history)
        print_console_output(headers["user-agent"], url, ip_address, response_code, number_of_redirects)
        time_console_output(dns_resolution_time, tcp_connection_time, url)
        if response_code == 200:
            content_load_time = get_content_time(url, timeout, headers)
            print("Get content time = " + time_convert(content_load_time) + "\n======================")
        else:
            print("Response code is not 200\n======================")
    except (ConnectTimeout, ReadTimeout):
        tcp_connection_time = "Timeout"
        dns_resolution_time = "Timeout"
        time_console_output(dns_resolution_time, tcp_connection_time, url)
        print("======================")
    except ConnectionError:
        print(url + ": Connection Error, looks like to incorrect URL\n======================")
    if output_file_name is not None:
        json_file_preparation(headers["user-agent"], url, dns_resolution_time, ip_address, tcp_connection_time,
                              content_load_time, response_code, number_of_redirects, output_file_name)


def print_console_output(user, url, ip_address, response_code, number_of_redirects):
    print("User Agent: " + str(user))
    print("URL: " + url)
    print("IP " + ip_address)
    print("HTTP response code: " + str(response_code))
    print("Number of redirects: " + str(number_of_redirects))


def time_console_output(dns_resolution_time, tcp_connection_time, url):
    print("URL: " + url)
    print("DNS resolution time = " + time_convert(dns_resolution_time))
    print("TCP connection time = " + time_convert(tcp_connection_time))


def json_file_preparation(user_agent, url, dns_resolution_time, ip_address, tcp_connection_time, content_load_time,
                          response_code, number_of_redirects, output_file_name):
    payload = dict()
    payload["user-agent"] = user_agent
    payload["url"] = url
    payload["dnsResolutionTimeMs"] = time_convert(dns_resolution_time)
    payload["ip"] = ip_address
    payload["tcpConnectionTimeMs"] = time_convert(tcp_connection_time)
    payload["getContentLoadTimeMs"] = time_convert(content_load_time)
    payload["httpResponseCode"] = response_code
    payload["numberOfRedirects"] = number_of_redirects
    save_into_json(payload, output_file_name, url)


def time_convert(time_format):
    if time_format is None:
        return None
    elif time_format == "Timeout":
        return "Timeout"
    else:
        return "%.2f" % (time_format * 1000)


def save_into_json(payload, output_file_name, url):
    with open(OUTPUT_FOLDER + output_file_name + url + '.json', 'w') as outfile:
        json.dump(payload, outfile, indent=4)


def get_input_list():
    with open(INPUT_FILE, 'r') as f:
        lines = f.read().splitlines()
    return lines


def get_ip_address(url):
    dns_start = time.time()
    ip_address = socket.gethostbyname(url)
    dns_end = time.time()
    dns_resolution_time = dns_end - dns_start
    return ip_address, dns_resolution_time


def get_tcp_connection_time(ip_address):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    start_tcp_connect = time.time()
    s.connect((ip_address, 80))
    end_tcp_connect = time.time()
    tcp_connection_time = end_tcp_connect - start_tcp_connect
    return tcp_connection_time


def get_content_time(url, timeout, headers):
    start_get_content = time.time()
    requests.get(BASE_URL + url, timeout=timeout, headers=headers).text
    end_get_content = time.time()
    content_load_time = end_get_content - start_get_content
    return content_load_time


if __name__ == "__main__":
    web_site_list = get_input_list()
    for web_site in web_site_list:
        main(web_site, options.timeout, options.file)

