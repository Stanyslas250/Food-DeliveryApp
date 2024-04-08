import flet as ft
from components import *


#This class will define the view for the outboarding

class Landing(ft.View):
    def __init__(self, page: ft.Page):
        super(Landing, self).__init__(
            route='/', horizontal_alignment="center",
            vertical_alignment="center",padding=0, bgcolor='white'
        )
        
        self.logo = ft.Image(src="image/Logo.svg",fit=ft.ImageFit.CONTAIN)
        
        self.btnNext = ft.IconButton('ARROW_FORWARD',
                                    icon_color='#FF7622',
                                    style=ft.ButtonStyle(
                                        bgcolor={"": "transparent"},
                                        shape={"": ft.RoundedRectangleBorder(radius=8)},
                                        side={"": ft.BorderSide(2)},
                                        ),
                                    on_click=lambda e: self.page.go("/Landing1")
                                    )

        self.controls=[
            self.logo,
            ft.Divider(height=25,color='transparent'),
            self.btnNext,
            
        ]
        
