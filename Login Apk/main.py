from kivy.core.text import LabelBase
from kivymd.app import MDApp
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.lang import Builder
from kivy.core.window import Window

Window.size = (410, 580)

class MainScreen(Screen):
    pass

class LoginScreen(Screen):
    pass

class SignupScreen(Screen):
    pass

class LoginApp(MDApp):
    def build(self):
        screen_manager = ScreenManager()
        screen_manager.add_widget(MainScreen(name='main'))
        screen_manager.add_widget(LoginScreen(name='login'))
        screen_manager.add_widget(SignupScreen(name='signup'))

        Builder.load_file("login.kv")
        Builder.load_file("signup.kv")

        return screen_manager

LoginApp().run()
