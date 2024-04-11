import flet as ft
from PageView.landingView import *
from components.landing1 import *
from components.landing2 import *
from components.landing3 import *
from PageView.loginView import *
from PageView.signinView import *
from PageView.homeView import *
from components.OTP_view import *
import test

def main(page: ft.Page):
    
    #Basic Setup info
    page.padding = 10
    page.spacing = 0
    page.window_height = 812
    page.window_width = 375
    page.window_max_height = 812
    page.window_max_width = 375
    page.window_resizable = False
    page.bgcolor = '#FFFFFF'
    
    def router(route):
        page.views.clear()

        if page.route == '/':
            landing = Landing(page)
            page.views.append(landing)
        
        if page.route == '/Landing1':
            nextPage = Landing1(page)
            page.views.append(nextPage)
            
        if page.route == '/Landing2':
            nextPage = Landing2(page)
            page.views.append(nextPage)
        
        if page.route == '/Landing3':
            nextPage = Landing3(page)
            page.views.append(nextPage)
            
        if page.route == '/Signup':
            nextPage = Signup(page)
            page.views.append(nextPage)
        
        if page.route == '/Login':
            nextPage = Login(page)
            page.views.append(nextPage)
        
        if page.route == '/OTP':
            nextPage = OTP_view(page)
            page.views.append(nextPage)
            
        if page.route == '/Main':
            nextPage = Home(page)
            page.views.append(nextPage)
            
        if page.route == '/test':
            nextPage = test.Test(page)
            page.views.append(nextPage)
            
        page.update()
    
    page.on_route_change = router  
    page.go('/test') 
    
ft.app(target=(main),assets_dir='assets/')