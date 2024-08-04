import pyqrcode
from PIL import Image
from pyzbar.pyzbar import decode
from json import loads, dumps


user_list = [
    {"id": 1, "name": "John", "email": "john@doe.gmail.com", "age": 30},
    {"id": 2, "name": "Jane", "email": "jane@doe.gmail.com", "age": 25},
    {
        "id": 3,
        "name": "Bob",
        "email": "bob@gmail.com",
        "age": 40,
    },
    {
        "id": 4,
        "name": "Sally",
        "email": "sally@gmail.com",
        "age": 35,
    },
]

create_user = lambda id, name, email, age: {
    "id": id,
    "name": name,
    "email": email,
    "age": age,
}

add_user = lambda record: user_list.append(record)

get_user_by_id = lambda id: next((user for user in user_list if user["id"] == id), None)

fetch_all_users = lambda length: user_list[:]


def generate_smartscan(user_data: dict, filename: str):
    data = dumps(user_data)
    qr_code = pyqrcode.create(data)
    qr_code.png(filename, scale=8)


def decode_smartscan(image_path: str):
    image = Image.open(image_path)
    decoded_objects = decode(image)
    if not decoded_objects:
        return None
    return decoded_objects[0].data.decode("utf-8")


def register_user_from_smart_scan(path: str):
    user_data = decode_smartscan(path)
    if user_data is None:
        return None
    data = loads(user_data)
    user = create_user(**data)
    add_user(user)
    print(fetch_all_users(10))


if __name__ == "__main__":
    # Add a new user
    add_user(create_user(5, "Sam", "sam@gmail.com", 22))

    # Find a user
    print(get_user_by_id(5))

    # List all users
    print(fetch_all_users(5))

    name = "John Doe"
    email = "john.doe@gmail.com"
    filename = "smartscan.png"
    generate_smartscan(create_user(7, name, email, 38), filename)

    image_path = r"smartscan.png"
    decoded_data = decode_smartscan(image_path)
    print(decoded_data)

    register_user_from_smart_scan(image_path)
