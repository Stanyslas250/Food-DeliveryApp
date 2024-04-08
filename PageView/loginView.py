from flet import *
from Service.Auth import *


class Login(View):
    def __init__(self, page: Page):
        super(Login, self).__init__(
            route='/Login',horizontal_alignment='CENTER',vertical_alignment='END',padding=0, bgcolor='#121223'
        )
        
        self.page = page
        self.input = Column(spacing=20,
                            alignment=MainAxisAlignment.START,
                            horizontal_alignment = CrossAxisAlignment.CENTER,
                            controls=[
                                    TextField(label='EMAIL',keyboard_type=KeyboardType.EMAIL,on_blur=validate_required_fied,on_change=restart_state),
                                    TextField(label='PASSWORD',label_style= TextStyle(),password=True,can_reveal_password=True),
                            ])  
        self.other = Row(alignment=MainAxisAlignment.CENTER,
                        controls=[
                            Text("Don't have an account?",size=16,color='646982',italic=True),
                            TextButton(text='SIGN UP',style=ButtonStyle(color='#ff7622'),on_click=lambda e: self.page.go("/Signup"))
                        ])
        
        def Email(e):
            email = self.input.controls[0].value
            return email
        
        def Password(e):
            password = self.input.controls[1].value
            return password
        
        def checkValidation(e):
            if sign_in_user(Email(e),Password(e)) == True :
                self.page.go('/Main')
        
        self.google = Container(padding=padding.all(20),width=64,height=64,shape=BoxShape.CIRCLE,bgcolor='red',content=Image('image/google.png',fit=ImageFit.CONTAIN))
        self.loginMethod =Container(
                            Column([
                                self.other,
                                Column(horizontal_alignment = CrossAxisAlignment.CENTER,spacing=18,
                                    controls=[
                                    Text('Or'),
                                    Row(alignment=MainAxisAlignment.SPACE_EVENLY,
                                        controls=[
                                        self.google,
                                        self.google,
                                        self.google
                                    ])
                                ])
                            ])
        )
        self.design = Container(
                        content=Column(
                            alignment=MainAxisAlignment.START,
                            horizontal_alignment = CrossAxisAlignment.CENTER,
                            spacing=10,
                            controls = [
                                        Text('Log In',
                                             color='white',
                                             size=30,
                                             weight='bold'),
                                        Text('Please sign in to your existing account',
                                            color='white',
                                            size=16),
                                        Container(
                                            adaptive=False,
                                            bgcolor='White',
                                            border_radius=BorderRadius(top_left=30,top_right=30,bottom_left=0,bottom_right=0),
                                            padding=padding.only(top=30,left=20,right=20),
                                            margin=margin.only(top=30),
                                            content = Column(
                                                alignment=MainAxisAlignment.START,
                                                horizontal_alignment=CrossAxisAlignment.CENTER,
                                                height=600,
                                                controls=[
                                                self.input,
                                                TextButton(text='LOGIN',width=327,height=62,style=ButtonStyle(color='white',bgcolor='#ff7622',
                                                                                             shape={"": RoundedRectangleBorder(radius=8)}
                                                        ),on_click=lambda e: checkValidation(e)),
                                                self.loginMethod
                                            ])
                                        )]
                            ))
        
        
        self.controls=[
            self.design
        ]