from utils.display_options import select_option

from functions.hello_world import hello_world
from functions.stop import stop

if __name__ == '__main__':
    options = [
        ("Saudação", hello_world),
        ("Sair", stop)
    ]

    select_option(options)
