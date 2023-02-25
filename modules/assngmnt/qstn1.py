""" WAP to generate a random colour hex , random alphabetical string ,random value b/w 2 intiger ,
and random multiple of 7 b/w 0 and 70
hint : random.randint()"""
import random
print("generate random colour hex")
rand = random.randint(0,16777215)
hex_num = str(hex(rand))
x = "#"+ hex_num[2:]
print(x)

print("random alphabetical string is")
print(random.choice("hai salma"))

print("random intiger")
print(random.randint(10,100))

print("random multiple of 7 b/w 0 t0 70")
print(random.randrange(0,70,7))