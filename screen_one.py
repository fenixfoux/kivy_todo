from kivy.uix.screenmanager import ScreenManager, SwapTransition, Screen, FadeTransition, NoTransition

class ScreenOne(Screen):
    def test_func(self):
        print('any text')