from kivy.app import App
# Import the App class from the kivy.app module. This is the base class for creating Kivy applications.

from kivy.uix.label import Label
# Import the Label class from the kivy.uix.label module. This class is used to create text labels in the application.

from kivy.core.window import Window
# Import the Window class from the kivy.core.window module. This class is used to manipulate the application window.

Window.size = (400, 200)
# Set the size of the application window to 400 pixels wide and 200 pixels high.

Window.clearcolor = (0, 1, 1, 1) # r_g_b_opacity
# Set the background color of the application window to cyan (red=0, green=1, blue=1) with full opacity (alpha=1).

class Myapp(App):
    # Define a new class Myapp that inherits from the App class. This class represents the application.

    def build(self):
        # Define the build method. This method is called when the application is built and should return the root widget of the application.

        lab = Label(text="Hello World", font_size=50, bold=True, italic=True, color=(1, 0, 0, 1)) # r_g_b_opacity
        # Create a new Label widget with the text "Hello World", font size 50, bold and italic text, and red color (red=1, green=0, blue=0) with full opacity (alpha=1).

        return lab
        # Return the Label widget as the root widget of the application.

Myapp().run()
# Create an instance of the Myapp class and call its run method define in kivy  to start the application.