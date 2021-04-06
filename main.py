from kivy.uix.screenmanager import Screen
from kivymd.app import MDApp
from kivy.lang import Builder


class BMIScreen(Screen):
    pass


class DatabaseScreen(Screen):
    pass


class Test(MDApp):

    def build(self):
        self.theme_cls.primary_palette = "Gray"
        builder = Builder.load_file('main.kv')
        return builder


Test().run()