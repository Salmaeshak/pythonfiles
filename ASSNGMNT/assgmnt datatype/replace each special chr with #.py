str1 = '/*John is @developer & musician!!'
print("string is :",str1)
str1 = str1.replace('/','#').replace('*','#').replace('@','#').replace('&','#').replace('!','#')
print("new string is : ",str1)