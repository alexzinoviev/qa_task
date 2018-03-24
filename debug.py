t = {}

INPUT_FILE = 'web_list.txt'

def get_input_list():
    with open(INPUT_FILE, 'r') as f:
        lines = f.read().splitlines()
    return lines


web_site_list = get_input_list()

value1 = 1
value2 = 2

print(web_site_list)

for i in web_site_list:
    print(i)
    t[i] = ()
    print(t)


t["yahoo.com"] = value1
print(t)
t["yahoo.com"] = t["yahoo.com"] + value2
print(t)