# import time
# from multiprocessing import Pool


# def run(fn) :
#   time.sleep(2)
#   print (fn)

# if __name__ == "__main__" :
#   startTime = time.time()
#   testFL = [1,2,3,4,5]
#   pool = Pool(10)#可以同时跑10个进程

#   pool.map(run,testFL)
#   pool.close()
#   pool.join()   
#   endTime = time.time()
#   print ("time :", endTime - startTime)


#coding: utf-8
import multiprocessing
import time

time.sleep(2)

a = [1,2,3,4,5]

def func(id):
    # print ("msg:", msg)
    # time.sleep(1)
    # print ("end")
    # return msg
    a[id] += 1
    print(a[id])
    time.sleep(1)
    return a[id]

if __name__ == "__main__":
    pool = multiprocessing.Pool(processes = 5)
    
    
    # msg = "hello %d" %(i)

        # print(func(i))
    results =  [pool.apply_async(func, (i,)) for i in range(0, 5) ]  #维持执行的进程总数为processes，当一个进程执行完毕后会添加新的进程进去

    for result in results:
        print(result,result.get())
    print ("Mark~ Mark~ Mark~~~~~~~~~~~~~~~~~~~~~~")
    pool.close()
    pool.join()   #调用join之前，先调用close函数，否则会出错。执行完close后不会有新的进程加入到pool,join函数等待所有子进程结束
    print ("Sub-process(es) done.")
    # time.sleep(2)

