import os
print(os.getcwd())

from utils.display_options import select_option

classFile = open('./database/class.txt', 'r')
userFile = open('./database/user.txt', 'r')
groupFile = open('./database/group.txt', 'r')

def print_data(label, data):
  print(f"{label}:")
  print(data)

def print_class():
  print_data("Turmas", classFile.read())
  classFile.close()

def print_user():
  print_data("Usuários", userFile.read())
  userFile.close()

def print_group():
  print_data("Grupos", groupFile.read())
  groupFile.close()

def display_data():
  options = [
        ("Usuários", print_user),
        ("Turmas ", print_class),
        ("Grupos", print_group),
    ]
  
  return select_option(options)