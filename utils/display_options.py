import curses

def execute_option(selected_function):
    selected_function()

def select_option(options):
    selected_index = 0

    stdscr = curses.initscr()
    curses.cbreak()
    stdscr.keypad(True)

    try:
        while True:
            stdscr.clear()

            for index, (label, _) in enumerate(options):
                prefix = '> ' if index == selected_index else '  '
                stdscr.addstr(f'{prefix}{label}\n')

            key = stdscr.getch()

            if key == curses.KEY_UP:
                selected_index = (selected_index - 1) % len(options)
            elif key == curses.KEY_DOWN:
                selected_index = (selected_index + 1) % len(options)
            elif key == ord('\n'):
                break

    finally:
        curses.endwin()

    selected_function = options[selected_index][1]
    execute_option(selected_function)