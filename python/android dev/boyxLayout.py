from kivy import app
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout

class MyApp(app.App):
    def build(self):                    #horizontal
        layout = BoxLayout(orientation='vertical', spacing=10, padding=20)
        bt1=Button(text='Button 1')
        bt2=Button(text='Button 2')
        bt3=Button(text='Button 3')
        bt4=Button(text='Button 4')
        
        layout.add_widget(bt1)
        layout.add_widget(bt2)
        layout.add_widget(bt3)
        layout.add_widget(bt4)
        
        return layout
    
    
MyApp().run()