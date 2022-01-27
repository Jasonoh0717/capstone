from kivy.app import App
from kivy.uix.boxlayout import BoxLayout

class LogIn(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def validate_user(self):
        user = self.ids.username_field
        pwd = self.ids.pwd_field
        info = self.ids.info

        uname = user.text
        passw = pwd.text

        if uname == '' or passw == '':
            info.text = '[color=#FF0000]Username and/ or password required[/color]'
        else:
            if  uname == 'admin' and passw == 'admin':
                info.text = '[color=#000FF0]Logged In Successfully!!![/color]'
            else:
                info.text = '[color=#FF0000]Invalid Username and/ or Password [/color]'

class LogInApp(App):
    def build(self):
        return LogIn()

if __name__=="__main__":
    sa = LogInApp()
    sa.run()

