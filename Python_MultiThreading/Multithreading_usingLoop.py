import threading   # use concurrent 
import time
lock=threading.Lock()
def fun(second) :
    

    print(f"Sleeping for {second} second ....")
    time.sleep(second)
    

 



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