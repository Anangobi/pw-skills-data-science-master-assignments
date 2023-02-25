def square(lis):
    lis1=[]
    for i in lis:
        lis1.append(i**2)
    print(lis1)
if __name__=="__main__":
    lis=[1,2,3,4,5,6,7,8,9]
    m=multiprocessing.Process(target=square, args=(lis,))
    print("the sample program for the assignment is")
    m.start()
    m.join()
