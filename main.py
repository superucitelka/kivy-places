from kivy.uix.boxlayout import BoxLayout
from kivy.properties import ObjectProperty, StringProperty, BooleanProperty
from kivy.uix.screenmanager import Screen

from classes.database import Database
from kivymd.app import MDApp
from kivymd.theming import ThemableBehavior
from kivymd.uix.list import OneLineIconListItem, MDList
from homescreen.homescreen import HomeScreen
from mapscreen.searchpopupmenu import SearchPopupMenu
from mapscreen.mapscreen import MapScreen
from mapscreen.mapscreen import PlaceMarker

import sqlite3


class ContentNavigationDrawer(BoxLayout):
    screen_manager = ObjectProperty()
    nav_drawer = ObjectProperty()


class ItemDrawer(OneLineIconListItem):
    icon = StringProperty()
    text = StringProperty()

    def change_text(self, val):
        self.text = val


class DrawerList(ThemableBehavior, MDList):
    def set_color_item(self, instance_item):
        """Called when tap on a menu item."""

        # Set the color of the icon and text for the menu item.
        for item in self.children:
            if item.text_color == self.theme_cls.primary_color:
                item.text_color = self.theme_cls.text_color
                break
        instance_item.text_color = self.theme_cls.primary_color


class RootScreen(Screen):
    pass


class MenuApp(MDApp):
    db = Database(dbtype='sqlite', dbname='places.db')
    connection = None
    cursor = None
    search_menu = None
    def build(self):
        return

    def on_start(self):
        self.connection = sqlite3.connect("places.db")
        self.cursor = self.connection.cursor()
        self.search_menu = SearchPopupMenu()


MenuApp().run()