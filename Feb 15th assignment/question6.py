import multiprocessing
def addition(add):
    lis1=[]
    for i in add:
        lis1.append(i+10)
    print(lis1)
def multiple(mul):
    lis2=[]
    for i in mul:
        lis2.append(i*10)
    print(lis2)
def division(div):
    lis3=[]
    for i in div:
        lis3.append(i/10)
    print(lis3)
if __name__=="__main__":
    lis=[10,20,30,40]
    m=multiprocessing.Process(target=addition,args=(lis,))
    m2=multiprocessing.Process(target=multiple,args=(lis,))
    m3=multiprocessing.Process(target=division,args=(lis,))
    m.start()
    m2.start()
    m3.start()
