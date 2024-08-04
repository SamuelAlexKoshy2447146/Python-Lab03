from random import randint

from smartscan_registration_module import *


name = input("Enter the user's name:")
email = input("Enter email ID:")
age_str = input("Enter the age:")
try:
    age = int(age_str)
except ValueError:
    print("Invalid age")
else:
    id = randint(1, 100)
    generate_smartscan(create_user(id, name, email, age), "smartscan.png")

register_user_from_smart_scan("smartscan.png")
