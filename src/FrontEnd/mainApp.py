from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button


class HelloApp(App):
    def build(self):
        layout = BoxLayout(orientation='vertical', padding=20, spacing=20)
        
        label = Label(
            text='¡Hola desde Kivy! 👋',
            font_size='32sp',
            size_hint_y=0.7
        )
        
        button = Button(
            text='Click aquí',
            size_hint_y=0.3
        )
        button.bind(on_press=self.on_button_press)
        
        layout.add_widget(label)
        layout.add_widget(button)
        
        return layout
    
    def on_button_press(self, instance):
        instance.text = '¡Funcionó! ✨'


if __name__ == '__main__':
    HelloApp().run()