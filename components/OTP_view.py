from flet import *
from PageView.signinView import Signup





class OTP_view(View):
    def __init__(self, page: Page):
        super().__init__( 
                        route='/OTP', horizontal_alignment="center",
                        vertical_alignment="center",padding=20, bgcolor='#fd2345')
        
        self.page = page
        phone = 250
        
        self.design = Container(
            Column(alignment=MainAxisAlignment.START,
                   horizontal_alignment=CrossAxisAlignment.CENTER,
                   controls=[
                        Column(alignment=MainAxisAlignment.START,
                               horizontal_alignment=CrossAxisAlignment.CENTER,
                               controls=[
                                Text('Verification',size=30,color='white',weight='bold'),
                                Text("The code has been sent to \n your phone number", size=16, text_align=TextAlign.CENTER,color='white')
                        ]),
                        Container(
                            Column([
                                Row(alignment=MainAxisAlignment.SPACE_BETWEEN,
                                    controls=[
                                    Text('CODE',size=16,color='darkblue'),
                                    Row([
                                        TextButton('Resend',disabled=True),
                                        Text('in 50sec')
                                    ])
                                ])
                            ])
                        )
            ])
        )
        
        self.controls=[
            self.design
        ]