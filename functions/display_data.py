import json

from utils.display_options import select_option


def print_data(label, data):
    print(f"{label}:")
    print(data)


def print_class():
    file = open('./database/class.json')
    class_json = json.load(file)

    print_data("Turmas", class_json)
    file.close()


def print_user():
    file = open('./database/user.json')
    user_json = json.load(file)

    print_data("Usuários", user_json)
    file.close()


def print_group():
    file = open('./database/group.json')
    group_json = json.load(file)

    print_data("Grupos", group_json)
    file.close()


def display_data():
    options = [
        ("Usuários", print_user),
        ("Turmas ", print_class),
        ("Grupos", print_group),
    ]

    return select_option(options)
