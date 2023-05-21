from utils.display_options import select_option

from functions.hello_world import hello_world
from functions.stop import stop
from functions.display_data import display_data

if __name__ == '__main__':
    control = True

    options = [
        ("Saudação", hello_world),
        ("Listar dados ", display_data),
        ("Sair", stop)
    ]

    while control:
        control = select_option(options)
