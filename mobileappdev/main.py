from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.widget import Widget


class WidgetsExample(BoxLayout):
    def on_button_click(self):
        print('''A brain tumor is an abnormal growth or mass of cells in or around your brain.''')


class BoxLayoutExample(BoxLayout):
    pass


class MainWidget(Widget):
    pass


class BrainTumorApp(App):
    pass


BrainTumorApp().run()
