from kivymd.app import MDApp
from kivymd.uix.screen import Screen
from kivy.core.window import Window
from kivy.lang import Builder
from kivymd.uix.filemanager import MDFileManager
import os
# from brain_tumor_cnn import predi
Window.size = (400, 500)

kv = """


BoxLayout:
    orientation: 'vertical'
    
    MDTopAppBar:
        title:"Brain Tumor Detetction"
        
    MDFloatLayout:
        MDLabel:
            text:"In general, diagnosing a brain tumor usually begins with magnetic resonance imaging (MRI). Once MRI shows that there is a tumor in the brain, the most common way to determine the type of brain tumor is to look at the results from a sample of tissue after a biopsy or surgery"
            size_hint_x:(0.9)
            font_style:"Body1"
            pos_hint:{"center_x": 0.5, "center_y": 0.5}
            
        MDRaisedButton:
            text:"Detect"
            on_release:app.file_manager_open()
            pos_hint:{"center_x": 0.5, "center_y": 0.2}


"""


class App(MDApp):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        Window.bind(on_keyboard=self.events)
        self.manager_open = False
        self.file_manager = MDFileManager(
            exit_manager=self.exit_manager, select_path=self.select_path
        )
    def file_manager_open(self):
        self.file_manager.show(os.path.expanduser("~"))  # output manager to the screen
        self.manager_open = True

    def select_path(self, path: str):
        self.exit_manager()
        # print(predi(path))
        print(path)

    def exit_manager(self, *args):
        self.manager_open = False
        self.file_manager.close()

    def events(self, instance, keyboard, keycode, text, modifiers):
        if keyboard in (1001, 27):
            if self.manager_open:
                self.file_manager.back()
        return True

    def build(self):
        screen = Screen()
        self.theme_cls.theme_style = "Light"
        return Builder.load_string(kv)


if __name__ == "__main__":
    App().run()

