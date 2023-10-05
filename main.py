from kivy.uix.screenmanager import ScreenManager, SwapTransition, Screen, FadeTransition, NoTransition
from kivymd.app import MDApp
from kivy.core.window import Window

from main_screen import MainScreen
from screen_one import ScreenOne
from screen_two import ScreenTwo
from screen_three import ScreenThree


class MainApp(MDApp):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        Window.size = (400, 450) # todo: find a way to resize before start application

    def build(self):
        screen_manager = ScreenManager(transition=NoTransition())
        screen_manager.add_widget(MainScreen(name='main_screen'))
        screen_manager.add_widget(ScreenOne(name='screen_one'))
        screen_manager.add_widget(ScreenTwo(name='screen_two'))
        screen_manager.add_widget(ScreenThree(name='screen_three'))
        return screen_manager



if __name__ == '__main__':
    MainApp().run()
