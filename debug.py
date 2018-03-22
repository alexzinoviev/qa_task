# import threading
# INPUT_FILE = 'web_list.txt'
#
#
#
# def get_input_list_2():
#     with open(INPUT_FILE, 'r') as f:
#         lines = f.read().splitlines()
#     return lines
#
# web_site_list = get_input_list_2()
# print(web_site_list)
#
#
# def main(i, url):
#     print("thread " + str(i) + " started:" + url)
#
#
# length_list = len(web_site_list)
# th = 2
# while length_list > 0:
#     for i in range(th):
#         t = threading.Thread(target=main, args=(i, web_site_list[i]))
#         # print(web_site_list[i])
#         t.start()
#         length_list = len(web_site_list)
#         try:
#             web_site_list.remove(web_site_list[i])
#         except IndexError:
#             print("not removed")
#     length_list = len(web_site_list)

    multi = True
    if multi is True:
        th = 2
        for i in range(th):
            for web_site in web_site_list:
                t = threading.Thread(target=main, args=(web_site, options.timeout, options.file))
                print("thread " + web_site + " started")
                t.start()
    else: