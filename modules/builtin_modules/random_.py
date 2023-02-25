import random
print(dir(random))
print(random.random())#random numbers from 0 to 9
print(random.randint(1,100)) #taking random intiger
print(random.randrange(1,10))
print(random.randrange(1,10,2))
print(random.choice("salma hai"))
print(random.choice([1,3,5,4,2]))
print(random.choice((2,3,6,8)))
x = [1,2,3,4,5]
random.shuffle(x)
print(x)