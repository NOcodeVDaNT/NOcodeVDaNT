from kivy.app import App  # Import the App class from the kivy.app module
from kivy.uix.button import Button  # Import the Button class from the kivy.uix.button module

# Define a new class 'appname' that inherits from the 'App' class
class appname(App):
    # Override the build method of the App class
    def build(self):
        # Create a Button instance with various properties
        btn = Button(
            text='submit',  # Set the text on the button
            font_size=50,  # Set the font size of the button text
            bold=True,  # Make the button text bold
            italic=True,  # Make the button text italic
            color=(1, 0, 0, 1),  # Set the color of the button text (red in this case)
            size_hint=(0.5, 0.1),  # Set the size hint of the button (50% width, 10% height)
            pos_hint={'center_x': 0.5, 'center_y': 0.5}  # Center the button on the screen
            # in center_x and centre_y position is caluculate as mid point of windows where as in 'x' and 'y' position is caluculate from bottom left corner
        )
        return btn  # Return the button instance to be displayed

# Create an instance of the 'appname' class and run the app
appname().run()