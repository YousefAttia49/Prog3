import threading
import time 
def print_time():
    for i in range (5):
        print(f'time is {i}')
        time.sleep(1)

def print_letter():
    for i in "ABCDE":
        print(f'lettter is {i}')
        time.sleep(1)

thread1=threading.Thread(target=print_time)
thread2=threading.Thread(target=print_letter)

thread1.start()
thread2.start()
#starting the threading

thread1.join()
thread2.join()
#Waiting thread to finishing


print('finished')
