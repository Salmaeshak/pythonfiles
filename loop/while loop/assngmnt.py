#qstn 1 adding elements in list
#my_list = []
#n = int(input("enter the number of elements: "))
#i=1
#while(i<=n):
    #my_list.append(i)
    #i = i+1
#print(my_list)

#qstn 2 avrg of 5 numbers
#sum = 0
#i = 1
#while(i<=5):
   # number = int(input("enter the %dth number"%(i)))
    #sum = sum+number
   # i = i+1
#avr = sum/5
#print("average of 5 numbers is: ",avr)

#qstn3 square of numbers
#n = int(input("enter the number: "))
#i = 1
#while(i<=n):
    #print(i*i)
    #i = i+1
#qstn4 sum of even numbers
#n = int(input("enter the number : "))
#i = 1
#sum = 0
#while(i<=n):
   # if(i%2==0):
        #sum = sum+i
    #i = i+1
#print("sum of even numbers: ",sum)
#qstn5 print even and odd numbers
#n = int(input("enter the value of n :"))
#i = 1
#while(i<=n):
   # if(i%2)==0:
    #    print("%d is an even number"%(i))
   # else:
        #print("%d is an odd number"%(i))
   # i = i+1
#qstn6 reverse a number
#num = int(input("enter the number: "))
#rev_num = 0
#while(num!=0):
    #digit = num%10
    #rev_num = rev_num*10+digit
    #num = num//10
#print("reverse of  the number is ",rev_num)

#qstn7 prime or not
num = int(input("enter the number: "))
count = 0
i = 2
while i<num:
    if num%i==0:
        count = 1
        print(num,"is not a prime number")
    i = i+1
if count==0:
    print(num,"is a prime number")






