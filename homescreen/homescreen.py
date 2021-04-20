from kivy.app import App
from kivy.uix.scrollview import ScrollView
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.button import MDIconButton
from kivymd.uix.card import MDCard
from kivymd.uix.list import MDList
from .locationpopupmenu import LocationPopupMenu


class PlaceCard(MDCard):
    def __init__(self, place, **kwargs):
        super(PlaceCard, self).__init__(**kwargs)
        self.place = place

    def on_release(self):
        menu = LocationPopupMenu()
        menu.title = self.place.name
        menu.text = self.place.description
        menu.open()

class ScrollList(ScrollView):
    pass


class StarButton(MDIconButton):
    def on_release(self):
        self.icon = "star-outline" if self.icon == "star" else "star"
        rate = 0
        for obj in self.parent.children:
            if isinstance(obj, StarButton):
                if obj.icon == "star":
                    rate += 1
        self.parent.parent.place.rate = rate
        self.app = App.get_running_app()
        self.app.db.update()
        self.app.root.ids.homescreen.redraw()


class SortList(MDList):
    pass

class HomeScreen(MDBoxLayout):
    def __init__(self, **kwargs):
        super(HomeScreen, self).__init__(**kwargs)
        self.app = App.get_running_app()
        self.redraw()

    def redraw(self):
        self.clear_widgets()
        places = self.app.db.read_places()
        self.scroll_list = ScrollList()
        y = 0.5
        i = 1
        for place in places:
            place_card = PlaceCard(place)
            place_card.pos_hint = {"center_x": 0.5, "center_y": 1 - y * i}
            place_card.ids.name_label.text = place.name
            place_card.ids.category_label.text = place.category.name
            if place.photos:
                place_card.ids.place_image.source = place.photos[0].url
            else:
                place_card.ids.place_image.source = 'homescreen/images/nopicture.jpg'
            for i in range(5):
                star = StarButton()
                star.icon = "star-outline" if i >= int(place.rate) else "star"
                place_card.ids.box_bottom.add_widget(star)
            self.scroll_list.ids.card_list.add_widget(place_card)
            i += 1
        self.add_widget(self.scroll_list)
