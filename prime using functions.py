def prime():
    num=0
    i=0
    for num in range(a+1,b):
        temp=1
        for i in range(2,num):
            if(num%i==0):
                temp=0
                break
        if (temp==1):
            print(num,end=" ")

#taking inputs
a=int(input("enter the starting number: "))
b=int(input("enter the ending number: "))

#calling the function
prime()