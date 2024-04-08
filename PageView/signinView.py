from flet import *
from Service.Auth import *


class Signup(View):
    def __init__(self, page: Page):
        super(Signup, self).__init__(
            route='/Login',horizontal_alignment='CENTER',vertical_alignment='END',padding=0, bgcolor='#121223'
        )
        
        def Email(e):
            test = self.input.controls[1].value
            return test
        
        def checkValidation(e):
            if register_user(Email(e),Password(e)) == True :
                self.page.go('/Main')
        
        def Password(e):
            test = self.input.controls[3].value
            return test
        
        self.page = page
        self.input = Column(spacing=20,
                            alignment=MainAxisAlignment.START,
                            horizontal_alignment = CrossAxisAlignment.CENTER,
                            controls=[
                                    TextField(label='NAME',keyboard_type=KeyboardType.NAME),
                                    TextField(label='EMAIL',keyboard_type=KeyboardType.EMAIL),
                                    TextField(label='PHONE',keyboard_type=KeyboardType.PHONE),
                                    TextField(label='PASSWORD',label_style= TextStyle(),password=True,can_reveal_password=True),
                                    TextField(label='RE-TYPE PASSWORD',label_style= TextStyle(),password=True,can_reveal_password=True)
                            ]) 

        self.other = Row(alignment=MainAxisAlignment.CENTER,
                        controls=[
                            Text('Already have an account?',size=16,color='646982',italic=True),
                            TextButton(text='LOGIN',style=ButtonStyle(color='#ff7622'),on_click=lambda e: self.page.go("/Login"))
                        ])
        
        self.design = Container(
                        content=Column(
                            alignment=MainAxisAlignment.SPACE_EVENLY,
                            horizontal_alignment = CrossAxisAlignment.CENTER,
                            #spacing=5,
                            controls = [
                                        Text('Sign Up',
                                             color='white',
                                             size=30,
                                             weight='bold'),
                                        Text('Please sign up to get started',
                                            color='white',
                                            size=16),
                                        Container(
                                            adaptive=True,
                                            bgcolor='White',
                                            border_radius=BorderRadius(top_left=30,top_right=30,bottom_left=0,bottom_right=0),
                                            height=700,
                                            padding=padding.only(top=30,left=20,right=20),
                                            margin=margin.only(top=30),
                                            content = Column([
                                                self.input,
                                                TextButton(text='SIGN UP',width=327,height=62,style=ButtonStyle(color='white',bgcolor='#ff7622',
                                                                                             shape={"": RoundedRectangleBorder(radius=8)}
                                                        ),on_click=lambda e: checkValidation(e)),
                                                self.other
                                            ])
                                        )]
                            ))
        
        
        self.controls=[
            self.design
        ]