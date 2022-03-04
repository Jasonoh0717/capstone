from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen


class SplashWindow(Screen):
    pass


class LoginWindow(Screen):
    def login_released(self,usnm, passw):
        print(f"user name = {usnm.text}")
        print(f"password = {passw.text}")
        self.clear_released(usnm,passw)
        pass

    def clear_released(self,usnm,passw):
        usnm.text = ""
        passw.text = ""
        pass
    pass

class ProfileWindow(Screen):
    pass

class ProfileCreateWindow(Screen):
    pass



class WindowManager(ScreenManager):
    pass


kv = Builder.load_file("my.kv")


class MyMainApp(App):
    def build(self):
        return kv


if __name__ == "__main__":
    MyMainApp().run()