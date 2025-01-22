# Import necessary modules from Kivy library
from kivy import app  # Import the App class to create the main application
from kivy.uix.button import Button  # Import the Button widget to create clickable buttons
from kivy.uix.gridlayout import GridLayout  # Import GridLayout to organize widgets in a grid pattern

# Define the main application class
class MyApp(app.App):  
    # The 'build' method is used to set up the UI components and return the layout
    def build(self):  
        # Create a GridLayout with 3 columns and 2 rows, with 10px spacing between widgets and 20px padding around the layout
        layout = GridLayout(cols=4, rows=2, spacing=10, padding=20)  

        # Create Button widgets with text labels
        button1 = Button(text='Button 1')  
        button2 = Button(text='Button 2')  
        button3 = Button(text='Button 3')  
        button4 = Button(text='Button 4')  
        button5 = Button(text='Button 5')  
        button6 = Button(text='Button 6')  

        # Add the Button widgets to the layout
        layout.add_widget(button1)  
        layout.add_widget(button2)  
        layout.add_widget(button3)  
        layout.add_widget(button4)  
        layout.add_widget(button5)  
        layout.add_widget(button6)  

        # Return the layout to be displayed in the application
        return layout  

# Run the application by creating an instance of MyApp and calling the 'run' method
MyApp().run()  
