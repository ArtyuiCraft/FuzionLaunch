from typing import Callable

main_menu = []

class menu:

    def __init__(self,name:str,func:Callable):
        self.name = name
        self.function = func

    def selected(self):
        self.function()
