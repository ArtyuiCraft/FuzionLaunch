from simple_term_menu import TerminalMenu

def menu(options=[1, 2, 3]):
    menu = TerminalMenu(options)
    return options[menu.show()]
