from random import randint, choice


class Dog:
    """
    一次模拟小狗的简单尝试
    """

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def sit(self):
        """模拟小狗收到指令时蹲下"""
        print(f"{self.name} is now sitting!")

    def roll_over(self):
        """模拟小狗收到指令时打滚"""
        print(f"{self.name} rolled over!")


my_dog = Dog('Willie', 6)

print(type(my_dog))
print(f"My dog's name is {my_dog.name}.")
print(f"My dog is {my_dog.age} years old.")
my_dog.sit()
my_dog.roll_over()

print(f"randint = {randint(1, 6)}")


class Car:
    def __init__(self, make, model, year):
        """初始化描述汽车的属性"""
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        """返回整洁的描述信息"""
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()

    def read_odometer(self):
        """打印一条指出汽车里程的消息"""
        print(f"This car has {self.odometer_reading} miles on it.")


my_new_car = Car('audi', 'a4', 2019)
print(my_new_car.get_descriptive_name())
my_new_car.read_odometer()

my_new_car.odometer_reading = 23
my_new_car.read_odometer()


class Battery:
    def __init__(self, battery_size=75):
        """一次模拟电动汽车电瓶的简单尝试"""
        self.battery_size = battery_size

    def describe_battery(self):
        """打印一条描述电瓶容量的消息。"""
        print(f"This car has a {self.battery_size}-kWh battery.")


class ElectricCar(Car):
    """电动汽车的独特之处。"""

    def __init__(self, make, model, year):
        """初始化父类的属性。"""
        super().__init__(make, model, year)
        self.battery = Battery()


my_tesla = ElectricCar('tesla', 'model s', 2019)
print(my_tesla.get_descriptive_name())
my_tesla.battery.describe_battery()

players = ['charles', 'martina', 'michael', 'florence', 'eli']
first_up = choice(players)
print(f"{first_up}")
