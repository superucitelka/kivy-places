from kivy_garden.mapview import MapMarkerPopup
from .locationpopupmenu import LocationPopupMenu

class PlaceMarker(MapMarkerPopup):
    place_data = []

    def on_release(self):
        menu = LocationPopupMenu()
        menu.title = self.place_data[1]
        menu.text = self.place_data[2]
        menu.open()
