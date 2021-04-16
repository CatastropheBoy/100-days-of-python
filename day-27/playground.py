def add(*args):
    res = 0
    for n in args:
        res += n
    return res

print(add(5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5))


def calculate(n, **kwargs):
    # for key, value in kwargs.items():
    n += kwargs["add"]
    n *= kwargs["multiply"]
    print(n)

calculate(2, add=3, multiply=3)

class Car:

    def __init__(self, **kwargs):
        self.make = kwargs.get("make")
        self.model = kwargs.get("model")
        self.color = kwargs.get("color")

mr_car = Car(make="Nissan", model="GTR")
print(mr_car.model)