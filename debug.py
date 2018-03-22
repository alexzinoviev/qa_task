# # import threading
# # INPUT_FILE = 'web_list.txt'
# #
# #
# #
# # def get_input_list_2():
# #     with open(INPUT_FILE, 'r') as f:
# #         lines = f.read().splitlines()
# #     return lines
# #
# # web_site_list = get_input_list_2()
# # print(web_site_list)
# #
# #
# # def main(i, url):
# #     print("thread " + str(i) + " started:" + url)
# #
# #
# # length_list = len(web_site_list)
# # th = 2
# # while length_list > 0:
# #     for i in range(th):
# #         t = threading.Thread(target=main, args=(i, web_site_list[i]))
# #         # print(web_site_list[i])
# #         t.start()
# #         length_list = len(web_site_list)
# #         try:
# #             web_site_list.remove(web_site_list[i])
# #         except IndexError:
# #             print("not removed")
# #     length_list = len(web_site_list)
#
#     # multi = True
#     # if multi is True:
#     #     th = 2
#     #     for i in range(th):
#     #         for web_site in web_site_list:
#     #             t = threading.Thread(target=main, args=(web_site, options.timeout, options.file))
#     #             print("thread " + web_site + " started")
#     #             t.start()
#     # else:
#
#
#
# import threading
#
# def writer(x, event_for_wait, event_for_set):
#     for i in range(10):
#         event_for_wait.wait() # wait for event
#         event_for_wait.clear() # clean event for future
#         print (x)
#         event_for_set.set() # set event for neighbor thread
#
# # init events
# e1 = threading.Event()
# e2 = threading.Event()
#
# # init threads
# t1 = threading.Thread(target=writer, args=(0, e1, e2))
# t2 = threading.Thread(target=writer, args=(1, e2, e1))
#
# # start threads
# t1.start()
# t2.start()
#
# e1.set() # initiate the first event
#
# # join threads to the main thread
# # t1.join()
# # t2.join()


time_list = [0.8301239013671875, 0.8696210384368896, 0.800112247467041, 0.8970849514007568, 1.0306990146636963, 0.9553341865539551, 0.942957878112793, 0.9830048084259033, 0.9741809368133545, 1.0241401195526123]
length = len(time_list)
sum = 0
for i in range(length):
    sum += time_list[i]
    print(sum)
avg = sum / length
print(avg)