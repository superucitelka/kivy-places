from kivy.uix.boxlayout import BoxLayout
from kivymd.uix.button import MDFlatButton
from kivymd.uix.dialog import MDDialog
from kivy.app import App
from kivymd.uix.swiper import MDSwiperItem


class MySwiper(MDSwiperItem):
    pass

class LocationContent(BoxLayout):
    def __init__(self, place, *args, **kwargs):
        super().__init__(**kwargs)
        self.ids.place_detail.text = f"Hodnocení: {place.rate}, kategorie: {place.category.name}"
        self.ids.place_description.text = place.description
        app = App.get_running_app()
        for photo in place.photos:
            slide = app.root_path + '/gallery/' + photo.url
            print(slide)
            swiper = MySwiper()
            swiper.ids.photo_image.source = slide
            self.ids.photogallery.add_widget(swiper)


class LocationPopupMenu(MDDialog):
    def __init__(self, id):
        app = App.get_running_app()
        place = app.db.read_place_by_id(id)
        super().__init__(
            type="custom",
            content_cls=LocationContent(place),
            text='Titulek fotky',
            size_hint=(.8, 1),
            buttons = [
                MDFlatButton(text='Zavřít', on_release=self.cancel_dialog)
            ]
        )
        self.title = place.name

    def cancel_dialog(self, *args):
        self.dismiss()

