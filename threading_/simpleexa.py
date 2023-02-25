from time import sleep
def task():
    #block for a moment
    sleep(3)
    #display a msg
    print("this is from another thread")
#task()
from threading import Thread
#create a thread
thread = Thread(target=task)
#next we can create an instance of the threading. thread class and specify
#our function name as the target argument in the constructor
#run the thread
thread.start()