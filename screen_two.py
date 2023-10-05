from kivy.metrics import dp
from kivymd.uix.menu import MDDropdownMenu
from kivymd.uix.snackbar import Snackbar
from kivy.uix.screenmanager import Screen

from kivymd.uix.dialog import MDDialog
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.pickers import MDDatePicker
from datetime import datetime


class ScreenTwo(Screen):

    task_list_dialog = None

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.menu_left = None
        self.menu_right = None

        menu_items_left = [
            {
                "viewclass": "OneLineListItem",
                "text": f"ллл {i}",
                "height": dp(56),
                "on_release": lambda x=f"Left Item {i}": self.menu_callback(x),
            } for i in range(5)
        ]
        menu_items_right = [
            {
                "viewclass": "OneLineListItem",
                "text": f"жжж {i}",
                "height": dp(56),
                "on_release": lambda x=f"Right Item {i}": self.menu_callback(x),
            } for i in range(5)
        ]

        self.menu_left = MDDropdownMenu(
            items=menu_items_left,
            width_mult=4,
        )

        self.menu_right = MDDropdownMenu(
            items=menu_items_right,
            width_mult=4,
        )

    def callback(self, button):
        if button.icon == "menu":
            self.menu_left.caller = button
            self.menu_left.open()
        elif button.icon == "dots-vertical":
            self.menu_right.caller = button
            self.menu_right.open()

    def menu_callback(self, text_item):
        self.menu_left.dismiss()
        self.menu_right.dismiss()
        Snackbar(text=text_item).open()

    # show task function
    def show_task_dialog(self):
        if not self.task_list_dialog:
            self.task_list_dialog = MDDialog(
                title="Create task",
                type="custom",
                content_cls=DialogContent()
            )
        self.task_list_dialog.open()

    # adding tasks
    def add_task(self, task, task_date):
        print(task.text, task_date)

    def close_dialog(self, **kwargs):
        self.task_list_dialog.dismiss()


class DialogContent(MDBoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.ids.date_text.text = datetime.now().strftime("%A %d %B %Y")

    # for show the date picker
    def show_date_picker(self):
        date_dialog = MDDatePicker()
        date_dialog.bind(on_save=self.on_save)

    # this function will get the date and save in a friendly form
    def on_save(self, instance, value, date_range):
        date = value.strftime("%A %d %B %Y")
        self.ids.date_text.text = str(date)
