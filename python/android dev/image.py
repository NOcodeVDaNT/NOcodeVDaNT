from kivy.app import App
from kivy.uix.image import Image, AsyncImage
from kivy.uix.boxlayout import BoxLayout
from kivy.core.window import Window

Window.size = (800, 500)

class MyApp(App):
    def build(self):
        URL_OF_IMAGE = 'https://www.python.org/static/community_logos/python-logo-master-v3-TM.png'

        # Create a layout to hold the images
        layout = BoxLayout(orientation='vertical', spacing=10, padding=20)

        # Add the first image (local) and center it using center_x and center_y
        img1 = Image(source='image.jpg', size_hint=(None, None), 
                     pos_hint={'center_x': 0.5, 'center_y': 0.5}, 
                     width=200, height=200)
        layout.add_widget(img1)

        # Add the second image (async load from URL)
        img2 = AsyncImage(source=URL_OF_IMAGE, size_hint=(1, 1))
        layout.add_widget(img2)

        return layout

# Run the app
MyApp().run()
