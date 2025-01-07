def add(*args):
    print(args[0])
    a = 0
    for i in args : # *args는 튜플 
        a += i
    return a
print(add(11,23,4,5,6,7,8,9))

def calculate(n, **kwargs):
                                 # **kwargs는 딕셔너리
    
    for key, value in kwargs.items():
        print(key)
        print(value)
    print(kwargs["add"])

    n += kwargs["add"]
    n *= kwargs["multiply"]



calculate(3,add=3, multiply=5)



class Car:
    def __init__(self, **kwargs):
        self.make = kwargs["make"]
        #self.model = kwargs["model"]
        self.model = kwargs.get("model") # model이 존재하지않아도 오류 없음음


my_car = Car(make="nissan")
print(my_car.model)