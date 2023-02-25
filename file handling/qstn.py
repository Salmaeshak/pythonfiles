"""wap to read  a file line by line and store in to a list"""
def file_read(fna):
    with open(fna) as f:
        out_list = f.readlines()
    print(out_list)
file_read('test')

# f = open('test','r')
# print(f.read())