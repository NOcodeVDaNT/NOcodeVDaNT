from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout


class MyApp(App):
    def build(self):
        layout = FloatLayout()

        # Inner BoxLayout (flow-like layout) for widgets
        inner_layout = BoxLayout(
            orientation="vertical",
            spacing=10,
            size_hint=(None, None),
            size=(300, 200),  # Define size explicitly for centering
        )
        # Position the BoxLayout at the center of the FloatLayout
        inner_layout.pos_hint = {"center_x": 0.5, "center_y": 0.5}

        # Add widgets to the inner layout
        username_input = TextInput(hint_text="Username", multiline=False, size_hint=(None, None), size=(300, 50))
        password_input = TextInput(hint_text="Password", password=True, multiline=False, size_hint=(None, None), size=(300, 50))
        login_button = Button(text="Login", size_hint=(None, None), size=(300, 50))

        # Bind login button to a function
        login_button.bind(on_press=self.handle_login)

        inner_layout.add_widget(username_input)
        inner_layout.add_widget(password_input)
        inner_layout.add_widget(login_button)

        # Add the centered inner layout to the float layout
        layout.add_widget(inner_layout)
        layout.pos=(100, 100)

        return layout

    def handle_login(self, instance):
        print("Login button pressed!")


MyApp().run()
