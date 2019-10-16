import kivy
kivy.require('1.0.7')
import voicechanger as v

from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.uix.slider import Slider
from kivy.uix.label import Label

class TestApp(App):

    def __init__(self):
        self.changer = v.Voicechanger()
        self.mainLabel = Label(text='[color=ff3333]Frequency[/color]\n[color=3333ff]Change[/color]: 0',
                                markup=True,
                                font_size='35sp')
        # self.changer.run()
        super(TestApp, self).__init__()

    def on_start(self):
        self.changer.run()

    def on_stop(self):
        self.changer.close()
        

    def touch(self,slider,pos):
        self.sliderValue = slider.value
        self.changer.setDelta(int(slider.value))
        self.mainLabel.text = '[color=ff3333]Frequency[/color]\n[color=3333ff]Change[/color]: ' + str(int(slider.value))
        # print("Slider touched. Value set to "+str(self.sliderValue))
        
    def build(self):
        # return a Button() as a root widget
        

        self.title = "Voice Changer v1.0"
        layout = GridLayout(cols=2)

        layout.add_widget(self.mainLabel)
        layout.add_widget(Slider(orientation='vertical',
                                 min=-10, 
                                 max=10, 
                                 value=0,
                                 value_track_color=[1, 1, 0, 1],
                                 on_touch_move=self.touch))
        return layout


if __name__ == '__main__':
    app = TestApp()
    # app.changer.run()
    app.run()
    app.changer.run()
    