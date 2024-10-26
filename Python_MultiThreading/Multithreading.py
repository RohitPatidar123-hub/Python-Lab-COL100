import threading    # use concurrent 
import time
from concurrent.futures import ThreadPoolExecutor


def fun(second) :
    print(f"Sleeping for {second} secoond")
    time.sleep(second)
    print("completee ",second)
    return second

def main() : 
    # normal code with out thread
    # time1= time.perf_counter()
    # fun(4)
    # fun(3)
    # fun(2)
    # fun(1)   
    # time2= time.perf_counter()
    # print(time2-time1)

    #same code using thread 
    time1= time.perf_counter()
    # t1 = threading.Thread(target =fun,args=[4])
    # t2 = threading.Thread(target =fun,args=[3])
    # t3 = threading.Thread(target =fun,args=[2])
    # t4 = threading.Thread(target =fun,args=[1])

    # t1.start()
    # t2.start()
    # t3.start()
    # t4.start() 

    # t1.join()
    # t2.join()
    # t3.join()
    # t4.join()
   
    time2= time.perf_counter()
    print(time2-time1) 


def poolingDemo() :
    with ThreadPoolExecutor() as executor :
        # time1= time.perf_counter()
        # future = executor.submit(fun ,4)
        
        # future = executor.submit(fun ,3)
        
        # future = executor.submit(fun ,2)
       
        # future = executor.submit(fun ,1)
        # print(future.result())
        # print(future.result())
        # print(future.result())
        # print(future.result())
        # time2= time.perf_counter()
        # print(time2-time1) 
        l=[4,5,6,1,2]
        time1= time.perf_counter()
        results = executor.map(fun,l)
        for result in results :
            print(result) 
        time2= time.perf_counter()
        print(time2-time1)     

poolingDemo()        