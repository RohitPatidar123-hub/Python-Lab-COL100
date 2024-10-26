from threading import Thread, Lock , RLock
import time
import sys

lock=RLock()

def task2() :
    print("Task 2 is attempting to acquire lock ")
    lock.acquire()


    print("Task 2 is acquired the lock ")
     
    time.sleep(2) 
    
    lock.release()

    print("Task 2 is release  the lock ")

def task1() :
    print("Task 1 is attempting to aquire the lock ")
    lock.acquire()

    print("Task 1 has acquired the lock")
    task2()
    time.sleep(2)
    lock.release()
    print("Task 1 has release the lock")

def task3() :
    print("Task 3 is attempting to acquire lock ")
    lock.acquire()


    print("Task 3 is acquired the lock ")
     
    time.sleep(2) 
    
    lock.release()

    print("Task 3 is release  the lock ")    
start =time.perf_counter()
thread1 = Thread(target=task1)
thread2 = Thread(target=task3)   
thread1.start()
thread2.start()

thread1.join()
thread2.join() 
end =time.perf_counter()

print(end-start)

