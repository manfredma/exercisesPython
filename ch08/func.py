
def greet_user(username, language='python'):
    print(f"Hello, {username.title()}! Your favorite language is {language.title()}!")

greet_user("jesse")
greet_user(username="edward", language="C")

def get_formatted_name(first_name, last_name):
    """返回整洁的姓名。"""
    full_name = f"{first_name} {last_name}"
    return full_name.title()

musician = get_formatted_name("jimi", "hendrix")
print(musician)

# 匹配任意数量的参数
def make_pizza(size, *toppings):
    print(f"\n Making a {size}-inch pizza with the following toppings:")
    for topping in toppings:
        print(f"- {topping}")

make_pizza(16, "pepperoni")
make_pizza(12, "mushrooms", "green peppers", "extra cheese")

def build_profile(first, last, **user_info):
    user_info['first_name'] = first
    user_info['last_name'] = last
    return user_info

user_profile = build_profile("albert", "einstein", location="princeton", field="physics")
print(user_profile)