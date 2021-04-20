from kivy.uix.boxlayout import BoxLayout
from kivy_garden.mapview import MapView
from kivy.clock import Clock
from kivy.app import App
from classes.database import Place
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.button import MDFlatButton
from kivymd.uix.dialog import MDDialog
from kivymd.uix.menu import MDDropdownMenu
from kivymd.uix.selectioncontrol import MDSwitch
from .placemarker import PlaceMarker


class PlaceContent(BoxLayout):
    def __init__(self, *args, **kwargs):
        super().__init__(**kwargs)
        app = App.get_running_app()
        categories = app.db.read_categories()
        menu_items = [{"viewclass": "OneLineListItem", "text": f"{category.name}", "on_release": lambda x=f"{category.name}": self.set_item(x)} for category in categories]
        # Vytvoření objektu menu_states pro výběr státu
        self.menu_categories = MDDropdownMenu(
            caller=self.ids.category_item,
            items=menu_items,
            position="center",
            width_mult=5,
        )

    # Metoda ošetřuje výběr státu z menu
    def set_item(self, text_item):
        # Podle textu vybrané položky se nastaví aktuálně vybraný stát
        self.ids.category_item.set_item(text_item)
        self.ids.category_item.text = text_item
        # Uzavření menu
        self.menu_categories.dismiss()


# Třída umožní vytvořit dialogové okno k editaci údajů daného místa
class PlaceDialog(MDDialog):
    def __init__(self, lat, lon, *args, **kwargs):
        super(PlaceDialog, self).__init__(
            type="custom",
            content_cls=PlaceContent(),
            title='Záznam místa',
            text='Ahoj',
            size_hint=(.8, 1),
            buttons=[
                MDFlatButton(text='Uložit', on_release=self.save_dialog),
                MDFlatButton(text='Zrušit', on_release=self.cancel_dialog)
            ]
        )
        self.lon = lon
        self.lat = lat

    # Ošetření tlačítka "Uložit"
    def save_dialog(self, *args):
        app = App.get_running_app()
        place = Place()
        place.name = self.content_cls.ids.place_name.text
        place.description = self.content_cls.ids.place_description.text
        place.latitude = self.lat
        place.longitude = self.lon
        category = app.db.read_category_by_name(self.content_cls.ids.category_item.text)
        place.category_id = category[0].id
        place.rate = self.content_cls.ids.place_rate.text
        place.url = self.content_cls.ids.place_url.text
        app.db.create_place(place)
        # Zavření dialogového okna
        self.dismiss()

    # Ošetření tlačítka "Zrušit"
    def cancel_dialog(self, *args):
        self.dismiss()


class EditModeSwitch(MDSwitch):
    def on_release(self):
        if self.active:
            self.parent.parent.ids.edit_mode_label.text = "Editační mód: zapnut"
        else:
            self.parent.parent.ids.edit_mode_label.text = "Editační mód: vypnut"


class PlacesMapView(MapView):
    getting_places_timer = None

    def start_getting_places_in_fov(self):
        try:
            self.getting_places_timer.cancel()
        except:
            pass

        self.getting_places_timer = Clock.schedule_once(self.get_places_in_fov, 1)

    def get_places_in_fov(self,*args):
        app = App.get_running_app()
        min_lat, min_lon, max_lat, max_lon = self.get_bbox()
        sql_statement = "SELECT * FROM places WHERE longitude > %s AND longitude < %s AND latitude > %s AND latitude < %s" % (min_lon, max_lon, min_lat, max_lat)
        app.cursor.execute(sql_statement)
        places = app.cursor.fetchall()
        self.places_names = []
        for place in places:
            name = place[1]
            if name in self.places_names:
                continue
            else:
                self.add_place(place)

    def add_place(self, place):
        lat, lon = place[5], place[6]
        marker = PlaceMarker(lat=lat, lon=lon, source='mapscreen/icons/marker-small.png')
        marker.place_data = place
        self.add_widget(marker)
        name = place[1]
        self.places_names.append(name)

    def create_place(self, lat, lon):
        self.dialog = PlaceDialog(lat=lat, lon=lon)
        self.dialog.open()
        self.get_places_in_fov()

    def on_touch_up(self, touch):
        if touch.grab_current == self:
            touch.ungrab(self)
            self._touch_count -= 1
            if self._touch_count == 0:
                # animate to the closest zoom
                zoom, scale = self._touch_zoom
                cur_zoom = self.zoom
                cur_scale = self._scale
                if cur_zoom < zoom or cur_scale < scale:
                    self.animated_diff_scale_at(1. - cur_scale, *touch.pos)
                elif cur_zoom > zoom or cur_scale > scale:
                    self.animated_diff_scale_at(2. - cur_scale, *touch.pos)
                self._pause = False
                self.coordinate = self.get_latlon_at(x=touch.pos[0],y=touch.pos[1],zoom=cur_zoom)
                if self.parent.ids.edit_mode.active:
                    self.parent.ids.edit_mode_label.text = "Editační mód: zapnuto"
                    print(self.coordinate.lat, self.coordinate.lon)
                    self.create_place(self.coordinate.lat, self.coordinate.lon)
                else:
                    self.parent.ids.edit_mode_label.text = "Editační mód: vypnuto"
            return True
        return super(MapView, self).on_touch_up(touch)

class MapScreen(MDBoxLayout):
    def edit_mode_switch(self, *args):
        print('switch')