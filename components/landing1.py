import flet as ft
#Landing 1

class Landing1(ft.View):
    def __init__(self, page: ft.Page):
        super(Landing1, self).__init__(
            route='/Landing1', horizontal_alignment="center",
            vertical_alignment="center",padding=20, bgcolor='white'
        )
        
        self.page = page
        
        self.design = ft.Column(
                        adaptive=False,
                        alignment=ft.MainAxisAlignment.CENTER,
                        horizontal_alignment = ft.CrossAxisAlignment.CENTER,
                        controls= [ ft.Container(
                                height=292,
                                content= ft.Image(src='/image/image1.jpeg',fit=ft.ImageFit.FILL,border_radius=ft.border_radius.all(10))
                            ),
                            ft.Container(
                                ft.Column([
                                    ft.Text('All your favorites',color='#000000',weight='bold',size=24),
                                    ft.Text('Get all your loved foods in one once place,you just place the orer we do the rest',max_lines=2,size=16),
                                    ft.Row([
                                        ft.Container(
                                            shape=ft.BoxShape("circle"),
                                            width=10,
                                            height=10,
                                            bgcolor='#ff7622'
                                        ),
                                        ft.Container(
                                            shape=ft.BoxShape("circle"),
                                            width=10,
                                            height=10,
                                            bgcolor='#ffe1ce'
                                        ),
                                        ft.Container(
                                            shape=ft.BoxShape("circle"),
                                            width=10,
                                            height=10,
                                            bgcolor='#ffe1ce'
                                        )
                            ],alignment=ft.MainAxisAlignment.CENTER)
                                ],spacing=24,alignment=ft.MainAxisAlignment.CENTER,
                        horizontal_alignment = ft.CrossAxisAlignment.CENTER,)
                            ),
                            ft.Container(
                                ft.Column([
                                    ft.TextButton(text='Next',width=327,height=62,style=ft.ButtonStyle(color='white',bgcolor='#ff7622',
                                                                                             shape={"": ft.RoundedRectangleBorder(radius=8)}
                                                                                             ),
                                                  on_click=lambda e: self.page.go('/Landing2')),
                                    ft.TextButton(text='Skip',width=327,height=62,style=ft.ButtonStyle(color='#ff7622',bgcolor='transparent',
                                                                                             shape={"": ft.RoundedRectangleBorder(radius=8)}
                                                                                             ),
                                                  on_click=lambda e: self.page.go('/Signup')),
                                ],alignment=ft.MainAxisAlignment.CENTER,
                        horizontal_alignment = ft.CrossAxisAlignment.CENTER,)
                            )],
                           spacing=20
        )

        self.controls=[
            self.design
            
        ]