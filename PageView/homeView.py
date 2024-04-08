import flet as ft
from components import *

class Home(ft.View):
   def __init__(self, page: ft.Page):
        super(Home, self).__init__(
            route='/Main', horizontal_alignment="center",
            vertical_alignment="center",padding=0, bgcolor='red'
        )
        
        self.page = page
        
        self.close = ft.ElevatedButton(text='Close')
        
        

        
        
        self.controls=[
                self.close
            
        ]