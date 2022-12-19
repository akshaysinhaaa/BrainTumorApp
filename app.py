from kivymd.app import MDApp
from kivymd.uix.screen import Screen
from kivymd.uix.button import MDRectangleFlatButton,MDRaisedButton
from kivy.core.window import Window
from kivy.lang import Builder
from kivymd.uix.label import MDLabel
Window.size = (400, 700)
KV = """  
MDLabel:
    font_name: 'Fonts/Montserrat-ExtraBold.ttf'
"""

# creating Demo Class(base class)
class App(MDApp):

    def build(self):
        # screen = Builder.load_string(KV)
        screen = Screen()
        txt = MDLabel(text = "Brain Tumor Detection", theme_text_color = "Primary", font_style = "H4", pos_hint={
            'center_x': 0.58, 'center_y': 0.95})
        screen.add_widget(txt)
        # adding theme_color
        self.theme_cls.theme_style = "Dark"

        txt = MDLabel(text="Bennett University has been set up at Greater Noida and commenced operations on 08 Aug 2016, initially with B.Tech and MBA programs. With a focus on giving students a premium learning experience, in an immersive environment at a campus designed by the internationally renowned RSP Architects, coupled with enhanced use of technology to meet students aspirations.", theme_text_color="Primary", font_style="Button")
        screen.add_widget(txt)
        btn = MDRaisedButton(text="Detect", pos_hint={
            'center_x': 0.5, 'center_y': 0.8},
                                    on_release=self.btnfunc1)
        screen.add_widget(btn)

        # returning the screen
        return screen

    def btnfunc(self, obj):
        print("button is pressed!!")

    def btnfunc1(self, obj):
        print("Preessed!!")


if __name__ == "__main__":
    App().run()