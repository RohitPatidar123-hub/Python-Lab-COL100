from threading import Thread ,Lock 
import time

lock =Lock()

def fun1() :
    while(True):
        if(lock.acquire(blocking=False)) :
            print("Lock has been acquire by thread 1")
            time.sleep(3)
            lock.release()
            print("Lock has been release by thread 1")
            break 
        else : 
            print("Lock is acquire by someone else(Thread 2) ")   
            time.sleep(0.5)


def fun2() :
    while(True) :
        if(lock.acquire(blocking=False)) :
            print("Lock has been acquire by thread 2")
            time.sleep(3)
            lock.release()
            print("Lock has been release by thread 2")
            break 
        else : 
            print("Lock is aquire by someine else: (Thread 1)")
            time.sleep(0.5) 

start =time.perf_counter()
thread1 =Thread(target=fun1)
thread2 =Thread(target=fun2)
thread1.start()
thread2.start()

thread1.join()
thread2.join()
end =  time.perf_counter()
print(end- start)   