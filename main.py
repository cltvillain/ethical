from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.utils import platform
import webbrowser

class ShareContactsApp(App):
    def build(self):
        layout = BoxLayout(orientation='vertical', padding=50, spacing=20)
        
        label = Label(text="Salman Sir — do you want to share your contact with Isa?", font_size=20)
        layout.add_widget(label)
        
        btn_yes = Button(text="YES", size_hint=(1, 0.3), background_color=(0, 0.6, 1, 1))
        btn_no = Button(text="NO", size_hint=(1, 0.3), background_color=(0.7, 0.7, 0.7, 1))
        
        btn_yes.bind(on_release=self.share_contact)
        btn_no.bind(on_release=self.stop_app)
        
        layout.add_widget(btn_yes)
        layout.add_widget(btn_no)
        
        return layout

    def share_contact(self, instance):
        email = "isaxvillain@gmail.com"
        subject = "Share Contact with Isa"
        body = "Salam Sir — please attach your vCard (.vcf) or paste contact details below:\n\nName:\nPhone:\nEmail:\nOrg:\n\nThanks,"
        mailto_link = f"mailto:{email}?subject={subject}&body={body}"
        
        # Open default mail client
        webbrowser.open(mailto_link)
        App.get_running_app().stop()

    def stop_app(self, instance):
        App.get_running_app().stop()


if __name__ == '__main__':
    ShareContactsApp().run()
