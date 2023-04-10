import os
from kivymd.app import MDApp
from kaki.app import App
from kivy.factory import Factory
from kivy.core.window import Window
from kivy.core.text import LabelBase

Window.size = (1920,1080)

class NR(MDApp, App):
    DEBUG = 1
    KV_FILES = {
        os.path.join(os.getcwd(), "screenmanager.kv"),
        os.path.join(os.getcwd(), "FirstPage.kv"),  
    }
    CLASSES = {
        "MainScreenManager": "screenmanager",
        "FirstPage": "screenmanager",
    }
    AUTORELOADER_PATHS = [
        (".", {"recursive": True}),
    ]
    def build_app(self):
        return Factory.MainScreenManager()
    
if __name__ == "__main__":
    LabelBase.register(name="SPoppins", fn_regular="Poppins-Regular.ttf")
    LabelBase.register(name="MPoppins", fn_regular="Poppins-Bold.ttf")
    LabelBase.register(name="LPoppins", fn_regular="Poppins-Light.ttf")
    NR().run()