import threading
import time
lis1=[1,2,3,4,5]
def sqr(n):
    print("The square of the multiple threading is %d"%(n*n))
    time.sleep(1)
def cub(n):
    print("The cube of the multiple threading is %d"%(n**3))
    time.sleep(1)
thread1=[threading.Thread(target=sqr,args=(i,)) for i in lis1]
thread2=[threading.Thread(target=cub,args=(j,)) for j in lis1]
for t in thread1:
    t.start()
for t in thread2:
    t.start()
