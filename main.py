from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
# from kivy.uix.widget import Widget
# from kivy.uix.label import Label
from kivy.properties import StringProperty




class MainWidget(BoxLayout):
    text = StringProperty()
    def __init__(self,**kwargs):
        super(MainWidget,self).__init__(**kwargs)
        self.text = "0"
        self.count = 0


    def add(self,instance):
        print("add!")
        self.count +=1
        self.text = str(self.count)

    def minus(self,instance):
        print("minus!")
        self.count -= 1
        self.text = str(self.count)

    def reset(self,instance):
        print("reset!")
        self.count = 0
        self.text = str(self.count)


class kvfile(App):
    def build(self):
        return MainWidget()


if __name__ == "__main__":
    kvfile().run()
