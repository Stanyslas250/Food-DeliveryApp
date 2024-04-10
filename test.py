from flet import *
import asyncio


class Test(View):
    def __init__(self, page: Page):
        super(Test, self).__init__(
            route='/test',horizontal_alignment='CENTER',vertical_alignment='END',padding=0, bgcolor='#121223'
        )
        
        def example():
            t = Text(value="Click the button...")
            pr = ProgressRing(width=16, height=16, stroke_width=2)

            async def button_clicked(e):
                t.value = "Doing something..."
                await t.update_async()
                b.disabled = True
                await b.update_async()
                for i in range(0, 101):
                    t.value = int(i * 0.1)                    
                    await asyncio.sleep(0.1)
                    await t.update_async()
                #t.value = "Click the button..."
                await t.update_async()
                b.disabled = False
                await b.update_async()

            b = FilledTonalButton("Start", on_click=button_clicked)
            
            return Column(
        [
            Text(
                "Circular progress indicator", style=TextThemeStyle.HEADLINE_SMALL
            ),
            Row([t]),
            b
        ],
        width=400,
        height=400,
    )
        
        self.design = example()
        
        self.controls=[
            self.design
        ]