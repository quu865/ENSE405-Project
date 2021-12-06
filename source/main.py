from kivy.lang import Builder
from kivymd.app import MDApp
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.clock import Clock
from kivy.properties import ObjectProperty
from kivy.uix.button import Button
from kivymd.uix.fitimage import FitImage
from kivymd.uix.gridlayout import GridLayout
from kivy.network.urlrequest import UrlRequest

class MenuScreen(Screen):
    pass

class DatabaseScreen(Screen):
    pass

class CaseScreen1(Screen):
    pass

class CaseScreen2(Screen):
    pass

class CaseScreen3(Screen):
    pass

class CaseScreen4(Screen):
    pass

class DiscussionScreen(Screen):
    pass

class S1DScreen(Screen):
    pass

class ResourcesScreen(Screen):
    pass

class StatisticsScreen(Screen):
    pass

class Stat1Screen(Screen):
    pass

class Stat2Screen(Screen):
    pass

class Stat3Screen(Screen):
    pass

class FastStatsScreen(Screen):
    pass

class ScreenManager(ScreenManager):
    pass
    

class MainApp(MDApp):
    def build(self):
        self.title='FIND Dashboard'
        self.theme_cls.theme_style = "Dark"
        buildKV = Builder.load_file("screen_nav.kv")
        return buildKV


if __name__ == '__main__':
    MainApp().run()