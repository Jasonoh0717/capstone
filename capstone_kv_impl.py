from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
import db

global current_user
current_user = object()
global kivy_app
kivy_app = object()


class UserData:
    def __init__(self,un =""):
        self.UserName=un
        self.FirstName=""
        self.LastName=""
        self.Email=""
        self.Interests=""
        pass

    def update(self,data):
        self.UserName = data[1]
        self.FirstName= data[3]
        self.LastName= data[4]
        self.Email= data[5]
        self.Interests= data[6]
        pass


    pass

# class SplashWindow(Screen):
#
#     pass

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




class ProfileWindow(Screen):
    def display_userdata(self,usnm,first_name,last_name,email,interests):
        user_profiles = db.profile_get(current_user.UserName)
        assert len(user_profiles) > 0

        user_data = user_profiles[0]
        current_user.update(user_data)

        usnm.text = current_user.UserName
        first_name.text = current_user.FirstName
        last_name.text = current_user.LastName
        email.text = current_user.Email
        interests.text = current_user.Interests




        pass
    pass

class ProfileCreateWindow(Screen):
    def create_profile_released(self,usnm,passw,first_name,last_name,email,interests):
        db.profile_new(usnm.text,passw.text,first_name.text,last_name.text,email.text,interests.text)
        global current_user
        current_user.UserName = usnm.text
        current_user.FirstName = first_name.text
        current_user.LastName = last_name.text
        current_user.Email = email.text
        current_user.Interests = interests.text


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

kv = Builder.load_file("my.kv")


class MyMainApp(App):
    def build(self):
        return kv

def main():
    # # Teo: use these lines to manipulate database
    # Database initialization and tests
    db.init()
    # db.un_exists('userNameThatDoesNotExist')
    # db.profile_delete('userNameThatDoesNotExist')
    # db.profile_delete('davidDelSol')
    # db.profile_new(
    #     'davidDelSol',
    #     'encrypted?',
    #     'david',
    #     'aloka',
    #     'test@preform.io',
    #     'salsa,extended intelligence,marathon running in a full suit'
    # )
    # db.profile_new(
    #     'Python733t',
    #     'encrypted?',
    #     'Doroteo ',
    #     'Bonilla',
    #     'doabonilla@yahoo.com',
    #     'work,school,sleep,repeat'
    # )
    # db.un_login('davidDelSol', 'encrypted?')
    # db.profile_update('davidDelSol', pw = 'definitelyNotEncripted!')
    # db.un_login('davidDelSol', 'definitelyNotEncripted!')
    # db.un_exists('davidDelSol')
    # db.profile_print(all = True)
    # db.profile_print(['Python733t'])
    # db.profile_print('Python733t')
    pass


if __name__ == "__main__":
    kivy_app = MyMainApp()

    main()
    kivy_app.run()
