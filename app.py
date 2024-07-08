import kivy
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.popup import Popup
from kivy.graphics import Color, Rectangle

class CustomBoxLayout(BoxLayout):
    def __init__(self, **kwargs):
        super(CustomBoxLayout, self).__init__(**kwargs)
        with self.canvas.before:
            Color(0.9, 0.9, 0.9, 1)  # RGBA
            self.rect = Rectangle(size=self.size, pos=self.pos)
        self.bind(size=self._update_rect, pos=self._update_rect)

    def _update_rect(self, instance, value):
        self.rect.size = instance.size
        self.rect.pos = instance.pos

class RegistrationApp(App):
    def build(self):
        self.title = "Registration Form"
        layout = CustomBoxLayout(orientation='vertical', padding=30, spacing=10)
        
        head_label = Label(
            text="Hansaja Python User Registration App", 
            font_size=26, 
            bold=True, 
            height=40,
            color=[0.2, 0.6, 0.8, 1]  # Color in RGBA
        )

        name_label = Label(text="Name:", font_size=18, color=[0.2, 0.6, 0.8, 1])
        self.name_input = TextInput(multiline=False, font_size=18, background_color=[1, 1, 1, 1], foreground_color=[0, 0, 0, 1])
        
        email_label = Label(text="Email:", font_size=18, color=[0.2, 0.6, 0.8, 1])
        self.email_input = TextInput(multiline=False, font_size=18, background_color=[1, 1, 1, 1], foreground_color=[0, 0, 0, 1])

        password_label = Label(text="Password:", font_size=18, color=[0.2, 0.6, 0.8, 1])
        self.password_input = TextInput(multiline=False, font_size=18, password=True, background_color=[1, 1, 1, 1], foreground_color=[0, 0, 0, 1])

        confirm_label = Label(text="Confirm Password:", font_size=18, color=[0.2, 0.6, 0.8, 1])
        self.confirm_input = TextInput(multiline=False, font_size=18, password=True, background_color=[1, 1, 1, 1], foreground_color=[0, 0, 0, 1])

        # button
        submit_button = Button(
            text='Register', 
            font_size=18, 
            on_press=self.register, 
            background_color=[0.2, 0.6, 0.8, 1], 
            color=[1, 1, 1, 1]
        )

        layout.add_widget(head_label)
        layout.add_widget(name_label)
        layout.add_widget(self.name_input)
        layout.add_widget(email_label)
        layout.add_widget(self.email_input)
        layout.add_widget(password_label)
        layout.add_widget(self.password_input)
        layout.add_widget(confirm_label)
        layout.add_widget(self.confirm_input)
        layout.add_widget(submit_button)
        
        return layout
    
    def register(self, instance):
        # collect information
        name = self.name_input.text
        email = self.email_input.text
        password = self.password_input.text
        confirm_password = self.confirm_input.text

        # validation
        if (name.strip() == '' or email.strip() == '' or 
            password.strip() == '' or confirm_password.strip() == ''):
            message = "Please fill in all fields"
        elif password != confirm_password:
            message = "Passwords do not match"
        else:
            filename = name + '.txt'
            with open(filename,'w') as file:
                file.write('Name: {}\n'.format(name))
                file.write('Email: {}\n'.format(email))
                file.write('Password: {}\n'.format(password)) 
            message = "Registration Successful !!!\nName: {}\nEmail: {}".format(name,email)


        # popup
        popup = Popup(
            title="Registration Status", 
            content=Label(text=message, color=[0.2, 0.6, 0.8, 1]), 
            size_hint=(None, None),
            size=(400, 200),
            background_color=[0.9, 0.9, 0.9, 1]
        )
        popup.open()

if __name__ == '__main__':
    RegistrationApp().run()
