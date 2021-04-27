import os
import uuid
from shutil import copyfile
from kivy.app import App
from kivy.properties import ObjectProperty
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.image import AsyncImage
from kivy.uix.popup import Popup
from classes.database import Photo
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.button import MDFlatButton
from kivymd.uix.carousel import MDCarousel
from kivymd.uix.dialog import MDDialog
from kivymd.uix.label import MDLabel
from kivymd.uix.menu import MDDropdownMenu
from kivymd.uix.toolbar import MDBottomAppBar


class LoadDialog(FloatLayout):
    load = ObjectProperty(None)
    cancel = ObjectProperty(None)


class PhotoContent(BoxLayout):
    def __init__(self, id, *args, **kwargs):
        super().__init__(**kwargs)
        self.app = App.get_running_app()
        if id:
            photo = self.app.db.read_photo_by_id(id)
            self.ids.photo_title.text = photo.title
            self.ids.photo_url.text = photo.url
            self.ids.photo_url.source = self.app.root_path + '/gallery/' + photo.url
        else:
            photo = Photo(title="", url="", time="", type="barevná")
        types = ['barevná', 'černobílá']
        types_items = [{"viewclass": "OneLineListItem", "text": f"{typ}", "on_release": lambda x=f"{typ}": self.set_type(x)} for typ in types]
        self.menu_types = MDDropdownMenu(
            caller=self.ids.photo_type,
            items=types_items,
            position="center",
            width_mult=2,
        )
        self.ids.photo_type.set_item(photo.type)
        self.ids.photo_type.text = photo.type

        places = self.app.db.read_places()
        place_items = [{"viewclass": "OneLineListItem", "text": f"{place.name}", "place_id": place.id, "on_release": lambda x=f"{place.name}", y=place.id: self.set_place(x, y)} for place in places]
        # Vytvoření objektu menu_states pro výběr státu
        self.menu_places = MDDropdownMenu(
            caller=self.ids.place_name,
            items=place_items,
            position="center",
            width_mult=5,
        )
        if id:
            place = self.app.db.read_place_by_id(photo.place_id)
            self.ids.place_name.set_item(place.name)
            self.ids.place_name.text = place.name
            self.ids.place_name.place_id = place.id

    def set_type(self, text_item):
        self.ids.photo_type.set_item(text_item)
        self.ids.photo_type.text = text_item
        self.menu_types.dismiss()

    def set_place(self, place_name, place_id):
        self.ids.place_name.set_item(place_name)
        self.ids.place_name.text = place_name
        self.ids.place_name.place_id = place_id
        self.menu_places.dismiss()

    def load(self, path, filename):
        with open(os.path.join(path, filename[0])):
            ext = filename[0].split('.')[-1]
            file_name = "%s.%s" % (uuid.uuid4(), ext)
            destination = os.path.join('gallery', file_name)
            copyfile(os.path.join(path, filename[0]), destination)
        self.ids.photo_url.text = file_name
        self.ids.photo_url.source = self.app.root_path + '/gallery/' + file_name
        self._popup.dismiss()

    def dismiss_popup(self):
        self._popup.dismiss()

    def show_load(self):
        cont = LoadDialog(load=self.load, cancel=self.dismiss_popup)
        self._popup = Popup(title="Load file", content=cont,
                            size_hint=(0.9, 0.9))
        self._popup.open()


class PhotoDialog(MDDialog):
    def __init__(self, id, *args, **kwargs):
        super(PhotoDialog, self).__init__(
            type="custom",
            content_cls=PhotoContent(id),
            title='Fotografie',
            text='Titulek fotky',
            size_hint=(.8, 1),
            buttons=[
                MDFlatButton(text='Uložit', on_release=self.save_dialog),
                MDFlatButton(text='Zrušit', on_release=self.cancel_dialog)
            ]
        )
        self.id = id

    # Ošetření tlačítka "Uložit"
    def save_dialog(self, *args):
        app = App.get_running_app()
        if self.id:
            photo = app.db.read_photo_by_id(self.id)
            photo.title = self.content_cls.ids.photo_title.text
            photo.url = self.content_cls.ids.photo_url.text
            photo.type = self.content_cls.ids.photo_type.text
            photo.place_id = self.content_cls.ids.place_name.place_id
            app.db.update()
        else:
            photo = Photo()
            photo.title = self.content_cls.ids.photo_title.text
            photo.url = self.content_cls.ids.photo_url.text
            photo.type = self.content_cls.ids.photo_type.text
            photo.place_id = self.content_cls.ids.place_name.place_id
            app.db.create_photo(photo)
        app.root.ids.photoscreen.ids.photocarousel.redraw(app.root.ids.photoscreen.ids.photocarousel.index)
        self.dismiss()

    # Ošetření tlačítka "Zrušit"
    def cancel_dialog(self, *args):
        self.dismiss()


class BottomNav(MDBottomAppBar):
    def plus_button(self, *args):
        self.dialog = PhotoDialog(id=None)
        self.dialog.open()

    def edit_button(self, *args):
        id = self.parent.ids.photocarousel.children[0].children[0].photo_id
        self.dialog = PhotoDialog(id=id)
        self.dialog.open()

    def delete_button(self, *args):
        id = self.parent.ids.photocarousel.children[0].children[0].photo_id
        app = App.get_running_app()
        photo = app.db.read_photo_by_id(id)
        filepath = app.root_path + '/gallery/' + photo.url
        if os.path.exists(filepath):
            os.remove(filepath)
        else:
            print("The file does not exist")
        app.db.delete_photo(id)
        self.parent.ids.photocarousel.redraw(0)


class ColoredLabel(MDLabel):
    pass


class PhotoImage(AsyncImage):
    pass


class PhotoCarousel(MDCarousel):
    def __init__(self, **kwargs):
        super(PhotoCarousel, self).__init__(**kwargs)
        self.app = App.get_running_app()
        self.redraw(0)

    def redraw(self, index):
        self.clear_widgets()
        photos = self.app.db.read_photos()
        for photo in photos:
            box = MDBoxLayout(orientation="vertical", pos_hint={"top": 0.95},  size_hint_y=.9)
            box.photo_id = photo.id
            title = ColoredLabel()
            title.text = f"{photo.title} [{photo.id}]"
            src = self.app.root_path + '/gallery/' + photo.url
            image = AsyncImage(source=src, allow_stretch=True)
            box.add_widget(image)
            box.add_widget(title)
            self.add_widget(box)
        self.index = index

class PhotoScreen(MDBoxLayout):
    def __init__(self, **kwargs):
        super(PhotoScreen, self).__init__(**kwargs)

