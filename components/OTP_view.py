from flet import *
from Service import *

class OTP_view(View):
    def __init__(self, page: Page):
        super().__init__(
                        route='/OTP', horizontal_alignment="center",
                        vertical_alignment="center",padding=20, bgcolor='#121223')
        
        self.page = page
        phone = 250     
        
        count = Text('',size=16,color='white')   
        Resend_Btn = TextButton('Resend',disabled=True)
        
        #resend = btn_Resend(count,Resend_Btn)
        
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
                                ])
                            ])
                        )
            ])
        )
        
            

        self.controls=[
            self.design
        ]