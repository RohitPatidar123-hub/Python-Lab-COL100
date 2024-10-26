import threading   # use concurrent 
import time
lock=threading.Lock()
def fun(second) :
    print(f"Thread {second} acquiring  lock")
    lock.acquire()
    print(f"Thread {second} acquired the  lock")

    print(f"Sleeping for {second} second ....")
    time.sleep(second)
    lock.release()

    print(f"Thread {second} release the the  lock")



start =time.perf_counter()
threads=[]
for i in range(10) :
    t=threading.Thread(target =fun,args=[i])
    t.start()
    threads.append(t)

for thread in threads:
    thread.join()

end =  time.perf_counter()
print(end- start)   