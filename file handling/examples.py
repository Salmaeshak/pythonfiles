#f = open('test','r')
#print(f.read())
#print(f.read(8))
#print(f.readline())
#for i in f:
   # print(i)
#f.close()


#a mode
# f = open('test','a')
# f.write('python is oops')
# f.close()
# f = open('test','r')
# for i in f:
#     print(i)
# f.close()

#w mode
# f = open('test','w')
# f.write('python language is oops')
# f.close()

# f = open('test','r')
# for i in f:
#     print(i)
# f.close()

# #seek(offset) method
f = open('test','r')
f.seek(5)
print(f.readline())
f.close()


# # #tell()
# f = open('test','r')
# f.readline()
# pos = f.tell()
# f.close()
# print("the position :",pos)
#
# from shutil import copyfile
# copyfile('test','test1')