from kivy.uix.boxlayout import BoxLayout
from kivymd.uix.button import MDFlatButton
from kivy.app import App
from kivymd.uix.dialog import MDDialog


class Content(BoxLayout):
    pass

class SearchPopupMenu(MDDialog):
    def __init__(self):
        app = App.get_running_app()
        super().__init__(content_cls = Content(), buttons = [
            MDFlatButton(
                text="CANCEL", text_color=app.theme_cls.primary_color
            ),
            MDFlatButton(
                text="OK", text_color=app.theme_cls.primary_color
            ),
        ])
        self.size_hint = [.9, .3]
