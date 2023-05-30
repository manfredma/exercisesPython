#!/usr/bin/env python3


# 布尔表达式 、条件表达式
# if conditional_test:
#    do something
#

age_0 = 22
age_1 = 18

if (age_0 >= 21) and (age_1 >= 21):
    print("both old than 21")
else:
    print("not both old than 21")

if (age_0 >= 21) or (age_1 >= 21):
    print("either old than 21")
else:
    print("neither not old than 21")

requested_toppings = ['mushrooms', "onions", "pineapple"]
if "mushrooms" in requested_toppings:
    print("in requested toppings")

age = 12
if age < 4:
    print("Your admission cost is $0")
elif age < 18:
    print("Your admission cost is $25")
else:
    print("Your admission cost is $40")

age = 22
if age < 4:
    price = 0
elif age < 18:
    price = 25
else:
    price = 40
print(f"Your admission cost is ${price}")


# 使用 If 语句处理列表
requested_toppings = ['mushrooms', 'green peppers', 'extra cheese']
for requested_topping in requested_toppings:
    print(f'Adding {requested_topping}')

print("\nFinished making your pizza!")
