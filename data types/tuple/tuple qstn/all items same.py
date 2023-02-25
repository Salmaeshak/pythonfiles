tup = (1,1,2,1,1)
# f = 1
# for i in tup:
#     for j in range(i,len(tup)-1):
#         if tup[i] == tup[j+1]:
#             f=0
#             break
# if f==1:
#     print("same")
# else:
#     print("not same")

#second method
tup = set(tup)
if len(tup) == 1 :
    print("same")
else:
    print("not same")