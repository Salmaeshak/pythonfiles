from time import sleep
from threading import Thread
def cal_sqr(num):
    print("calculate the square root of the given number:")
    for n in num:
        sleep(0.3)
        print("square is:",n*n)
def cal_cube(num):
    print("calculatr the cube of the given number:")
    for n in num:
        sleep(0.3)
        print('cube is:',n*n*n)
lst = [4,5,6,7,2]
t1 = time() #get total time to execute the function
th1 = Thread(target = cal_sqr,args=(lst,)) #args should have more than one arguments
th2 = Thread(target = cal_cube,args=(lst,))
th1.start()
th2.strat()
th1.join()
th2.join()