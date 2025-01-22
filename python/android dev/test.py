# Import necessary modules from Kivy library
from kivy import app  # Import the App class to create the main application
from kivy.uix.boxlayout import BoxLayout  # Import BoxLayout for layout arrangement
from kivy.uix.textinput import TextInput  # Import TextInput to take user input
from kivy.uix.button import Button  # Import Button for the login button
from kivy.uix.label import Label  # Import Label to display text or messages
from kivy.uix.popup import Popup  # Import Popup to show a message when login is successful or failed

# Define the main application class
class MyApp(app.App):  

    # Method to handle login button click
    def on_login(self, username, password):
        # Example login validation (hardcoded credentials)
        if username == "user" and password == "password":
            self.show_popup("Login Successful", "Welcome, " + username)
        else:
            self.show_popup("Login Failed", "Invalid username or password")

    # Method to display a popup message
    def show_popup(self, title, message):
        # Create a Label with the message
        popup_content = BoxLayout(orientation='vertical')
        label = Label(text=message)
        popup_content.add_widget(label)
        
        # Create a button to close the popup
        close_button = Button(text="Close")
        close_button.bind(on_press=lambda instance: popup.dismiss())  # Close the popup when pressed
        popup_content.add_widget(close_button)
        
        # Create and open the popup
        popup = Popup(title=title, content=popup_content, size_hint=(None, None), size=(300, 200))
        popup.open()

    # The 'build' method is used to set up the UI components and return the layout
    def build(self):  
        # Create a BoxLayout for the main layout (vertical arrangement)
        layout = BoxLayout(orientation='vertical', padding=10, spacing=10)

        # Create a TextInput for username with placeholder text
        self.username_input = TextInput(hint_text='Username', multiline=False)
        
        # Create a TextInput for password with placeholder text and password masking
        self.password_input = TextInput(hint_text='Password', password=True, multiline=False)

        # Create a Login button and bind it to the on_login method
        login_button = Button(text='Login')
        login_button.bind(on_press=self.handle_login)

        # Add the widgets to the layout
        layout.add_widget(self.username_input)
        layout.add_widget(self.password_input)
        layout.add_widget(login_button)

        # Return the layout to be displayed in the application
        return layout

    # Method to handle the login process when the button is clicked
    def handle_login(self, instance):
        username = self.username_input.text  # Get the username from the input field
        password = self.password_input.text  # Get the password from the input field
        self.on_login(username, password)  # Call on_login method to check credentials

# Run the application by creating an instance of MyApp and calling the 'run' method
MyApp().run()
