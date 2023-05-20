class Test:
    def m1(self,a,b):
        def calc(a,b):
            print("The addition of two number is: ",a+b)
            print("The subtraction of two number is: ",a-b)
            print("The multiplication of two number is: ",a*b)
            print("The division of two number is: ",a/b)
        calc(a,b)
t=Test().m1(2,3)

