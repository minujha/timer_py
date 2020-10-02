import time
# initial = time.time()
# print(initial)

# for items in range(45):
#     print("prince is very good boy")
#     time.sleep(2)
# print("time taken by for loop ",time.time()-initial)
# initial2 = time.time()
# i = 45
# while(i<45):
#     print("prince is very good boy")
#     i = i+1
# print("time taken by while loop ",time.time()-initial2)


localtime = time.asctime(time.localtime(time.time))
print(localtime)