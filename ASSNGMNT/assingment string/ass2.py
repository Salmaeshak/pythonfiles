# qstn 1
str = "/*jon is @developer & musician!!"
print("old string is =", str)
print("new string is =",
      str.replace('/', '#').replace('*', '#').replace('@', '#').replace('&', '#').replace('!', '#').replace('!', '#'))

# qstn 2
s1 = "luminar"
s2 = "python"
s3 = s1[0:4]
s4 = s1[4:7]
print(s3 + s2 + s4)

#qstn 2 method 2
s12 = "luminar"
s22 = "python"
length = len(s12)
index = length/2
s32 = s12[0:index]
s42 = s22[index:length]
new_string = print(s32+s22+s42)
