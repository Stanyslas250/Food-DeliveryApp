import asyncio
from flet import *

async def btn_Resend(t: Text, btn: TextButton):
            for i in range(0,51):
                t.value = int(i*0,1)
                await asyncio.sleep(0.1)
                await t.update_async()
            btn.disabled = False
            await btn.update_async()
            return Row([
                        btn,
                        t
                        ]) 