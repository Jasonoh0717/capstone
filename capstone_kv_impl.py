import kivy
kivy.require('1.9.0')

from kivy.config import Config
Config.set('graphics', 'width', '375')#configure a file
Config.set('graphics', 'height', '667')
from kivy.app import App
from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.uix.widget import Widget
from kivy.uix.screenmanager import ScreenManager, Screen
import db

global current_user
current_user = object()
global kivy_app
kivy_app = object()


def check_email(email):
    import re
    regex = '^[a-z0-9\._]+[@]\w+[.]\w{2,3}$' # regular expression pattern to check email validation

    if(re.search(regex,email)):
        print("Valid Email")
        return True
    else:
        print("Invalid Email")
        return  False


class UserData:
    def __init__(self,un =""):
        self.UserName=un
        self.FirstName=""
        self.LastName=""
        self.ZipCode=""
        self.DateOfBirth=""
        self.Email=""
        self.Interests=""
        pass

    def update(self,data):
        self.UserName = data[1]
        self.FirstName= data[3]
        self.LastName= data[4]
        self.ZipCode= data[5]
        self.DateOfBirth= data[6]
        self.Email= data[7]
        self.Interests= data[8]
        pass


    pass


class LoginWindow(Screen):#
    def login_released(self,usnm, passw):
        print(f"user name = {usnm.text}")
        print(f"password = {passw.text}")
        userNameExists = db.un_exists(usnm.text)
        if userNameExists == True:
            result = db.un_login(usnm.text,passw.text)
            if result == True:
                global current_user
                current_user = UserData(usnm.text)
                # clear text fields
                usnm.text =""
                passw.text =""
                #set window to profile
                kivy_app.root.current = "profile"
                pass
            else:
                kivy_app.root.current = "login_wrong_password"
        else:
            # give users feedback that they are not able to log in due to invalid credentials
            kivy_app.root.current = "login_no_username"
            pass

        self.manager.transition.direction = "left"

        pass

        pass

    pass

class LoginNoUsernameWindow(Screen):
    pass

class LoginEmailUsernameWindow(Screen):
    def email_username(self, email, message, email_button, cancel_button):
        kivy_app.root.current = "login_email_username_confirmation"
        self.manager.transition.direction = "left"

        pass
    pass
class LoginEmailUsernameConfirmationWindow(Screen):
    pass

class LoginWrongPasswordWindow(Screen):
    pass

class LoginResetPasswordWindow(Screen):
    def email_password_reset(self,email, message, email_button, cancel_button):
        kivy_app.root.current = "login_reset_password_confirmation"
        self.manager.transition.direction = "left"

        pass
    pass
class LoginResetPasswordConfirmationWindow(Screen):
    pass


class ProfileView(Widget):
    pass

class ProfileWindow(Screen):
    def display_userdata(self,usnm,first_name,last_name,zip_code,date_of_birth,email,interests):
        user_profiles = db.profile_get(current_user.UserName)
        assert len(user_profiles) > 0

        user_data = user_profiles[0]
        current_user.update(user_data)

        usnm.text = current_user.UserName
        first_name.text = current_user.FirstName
        last_name.text = current_user.LastName
        zip_code.text = current_user.ZipCode
        date_of_birth.text = current_user.DateOfBirth
        email.text = current_user.Email
        interests.text = current_user.Interests


        pass

    pass


class ProfileCreateWindow(Screen):
    def create_profile_released(self,usnm,passw,passw2,first_name,last_name,zip_code,date_of_birth,email,interests):
        all_required_info = True
        required_fields = [usnm,passw,passw2,first_name,last_name,zip_code,date_of_birth,email]
        for field in required_fields:
            if field.text == "":
                all_required_info = False
                field.background_color = [1, 0.5, 0.5, 1]
            else:
                field.background_color = [1, 1, 1, 1]
                pass

        if passw2.text != passw.text:
            all_required_info = False
            passw2.background_color = [1, 0.5, 0.5, 1]

        # if not check_email(email.text):
        #     all_required_info = False
        #     email.background_color = [1, 0.5, 0.5, 1]

        if not all_required_info:
            return

        global current_user

        user_name_already_in_use = db.un_exists(usnm.text)
        if user_name_already_in_use:
            usnm.background_color = [1, 0.5, 0.5, 1]
            current_user = UserData(usnm.text)
            kivy_app.root.current = "profile_username_already_in_use"
            self.manager.transition.direction = "left"
        else:

            db.profile_new(usnm.text,passw.text,first_name.text,last_name.text,zip_code.text, date_of_birth.text,email.text,interests.text)
            current_user.UserName = usnm.text
            current_user.FirstName = first_name.text
            current_user.LastName = last_name.text
            current_user.ZipCode = zip_code.text
            current_user.DateOfBirth = date_of_birth.text
            current_user.Email = email.text
            current_user.Interests = interests.text

            kivy_app.root.current = "profile"
            self.manager.transition.direction = "left"

        pass

    pass

class ProfileUserNameAlreadyInUseWindow(Screen):
    message_base = None


    def update_message(self):
        if self.message_base == None:
            self.message_base = self.message.text
        self.message.text = current_user.UserName + self.message_base
        pass
    pass

class WindowManager(ScreenManager):

    def get_username(self):
        global current_user

        return current_user.UserName

    def update_username(self,newusername ):

        global  current_user
        current_user.UserName = newusername

        pass

    def clear_released(self,* args):
        for element in args:
            element.text = ""
            pass
        pass


    pass


current_user = UserData()



class MyMainApp(MDApp):
    def build(self):
        return Builder.load_file("my.kv")



def main():
    db.init()
    pass


if __name__ == "__main__":
    kivy_app = MyMainApp()

    main()
    kivy_app.run()
