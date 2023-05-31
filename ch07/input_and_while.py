#!/use/bin/env python3


prompt = "If you tell us who you are, we can personalize the messages you see."
prompt += "\nwhat is your first name?"

name = input(prompt)
print(f"\nHello, {name}!")

current_number = 1
while current_number <= 5:
    print(current_number)
    current_number += 1

unconfirmed_users = ['alice', 'brian', 'candace']
confirmed_users = []

while unconfirmed_users:
    current_user = unconfirmed_users.pop()
    confirmed_users.append(current_user)
    print(f"Verifying user: {current_user.title()}")
print("\nThe following users have been confirmed:")
for confirmed_user in confirmed_users:
    print(confirmed_user.title())


