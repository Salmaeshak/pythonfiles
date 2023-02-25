from time import sleep
def task(sleep_time,message):
    sleep(sleep_time)
    print(message)
#create thread
from threading import Thread
thread = Thread(target=task,args=(1.5,'new message from another thread'))
#run thread
thread.start()
#wait for the thread to finish
print('waiting for the thread....')
thread.join()