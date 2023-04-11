__version__ = "1.0"
from kivymd.app import MDApp
from kivy.core.window import Window
from kivy.uix.screenmanager import Screen, NoTransition, CardTransition
from dbmain import DbMain
from kivy.properties import ObjectProperty
from kivymd.uix.snackbar import Snackbar
from kivy.uix.button import Button

Window.size = (375, 750)


class HomeScreen(Screen):
    pass


class LoginScreen(Screen):
    pass


class RegisterScreen(Screen):
    pass


class SettingsScreen(Screen):
    pass


class CategoryScreen(Screen):
    pass

class InsCategoryScreen(Screen):
    pass


class MainApp(MDApp):

    def on_start(self):
        self.theme_cls.primary_palette = 'Green'
        self.theme_cls.primaru_hue = '500'
        self.theme_cls.theme_style = 'Dark'
        self.db = DbMain('Fincapp.db')
        self.curr_user_id = -1
        self.curr_user_name = ""
        self.curr_user_email = ""

    def change_screen(self, screen_name, direction, mode):
        screen_manager = self.root.ids.screen_manager
        if direction == "None":
            screen_manager.transition = NoTransition()
            screen_manager.current = screen_name
            return
        screen_manager.transition = CardTransition(
            direction=direction, mode=mode)
        screen_manager.current = screen_name

    def opensidebarmenu(self, action):
        self.root.ids.nav_drawer.set_state(action)

    def chk_user(self, uname, upswd):
        screen_manager = self.root.ids.screen_manager
        chk_authorized = self.db.chk_usuario_cont(uname, upswd)

        return_str = self.db.get_user_name(3)
        print(return_str)

        if(chk_authorized == 1):
            print("Authorized access!!")
            self.change_screen("scr_home", direction='right', mode='push')
            self.curr_user_id = self.db.get_user_id(uname)
            self.curr_user_name = self.db.get_user_name(self.curr_user_id)
            self.curr_user_email = self.db.get_user_email(self.curr_user_id)
            self.root.ids['navsidebar_user_name'].text = self.curr_user_name
            self.root.ids['navsidebar_user_email'].text = self.curr_user_email
            self.db.upd_curr_user(self.curr_user_id)
        else:
            screen_manager.get_screen(
                'scr_login').ids.txt_login_info.text = "[color=ff0000]Invalid Username or Password. Try again![/color]"
            print("UNauthorized access!!")
        print("hello! Ur name : {}, id : {}, password : {}?".format(
            uname, self.curr_user_id, upswd))

    def register_user(self, usuario, nombre_completo, correof, indice, numero, passwordu):
        screen_manager = self.root.ids.screen_manager
        if(self.db.chk_exist_user(usuario) == 1):
            screen_manager.get_screen(
                'scr_register').ids.txt_info_register.text = "[color=ff0000]Nombre de usuario ya existe, Escoje otro.[/color]"
        else:
            self.db.ins_tbl_telefono(indice, numero)
            self.db.ins_tbl_email(correof)            
            self.db.ins_tbl_persona(usuario, nombre_completo, passwordu, 1, 1)
            self.change_screen("scr_login", direction='left', mode='push')
            Snackbar(text="New User Registered!").open()
            
    def leftmenucallback(self, x):
        screen_manager = self.root.ids.screen_manager
        self.change_screen("scr_settings", direction='left', mode='push')
        #Snackbar(text="Under Construction..").open()

    def save_settings(self, old_pwd, new_pwd):
        screen_manager = self.root.ids.screen_manager
        curr_pwd = self.db.get_user_pswd(self.curr_user_id)
        if(curr_pwd == old_pwd):
            self.db.upd_user_passwd(self.curr_user_id, new_pwd)
            self.change_screen("scr_login", direction='right', mode='push')
            Snackbar(text="New Password Updated!").open()
        else:
            screen_manager.get_screen(
                'scr_settings').ids.txt_info_settings.text = "[color=ff0000]Wrong old password.[/color]"

    def register_cat(self, categoriai):
        screen_manager = self.root.ids.screen_manager
        self.db.ins_tbl_cat(categoriai)
        Snackbar(text="New User Registered!").open()
        
    def actualizar_categorias(self):
        self.layout.clear_widgets()

        self.cur.execute('SELECT * FROM categorias')
        categorias = self.cur.fetchall()

        for categoria in categorias:
            btn = Button(text=categoria[1])
            self.botones.append(btn)
            self.layout.add_widget(btn)
MainApp().run()
