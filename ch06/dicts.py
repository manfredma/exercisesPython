#!/usr/bin/env python3

alien_0 = {'color': 'green', 'points': 5}

print(alien_0['color'])
print(alien_0['points'])

print(type(alien_0['color']))
print(type(alien_0['points']))
print(type(alien_0))

print(alien_0)

alien_0["x_position"] = 0
alien_0["y_position"] = 25
print(alien_0)

del alien_0["x_position"]
print(alien_0)

print("\n")
favorite_language = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
}

language = favorite_language['sarah'].title()
print(f"Sarah's favorite language is {language}" )

language = favorite_language.get("edward").title()
print(f"Edward's favorite language is {language}" )

language = favorite_language.get("NotExists")
print(f"NotExists' favorite language is {language}" )

print("\n")
for name, language in favorite_language.items():
    print(f"{name.title()}'s favorite language is {language.title()}")
