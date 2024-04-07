from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.togglebutton import ToggleButton

from deep_translator import GoogleTranslator

class Interface(BoxLayout):
	pass
	
class LeftLayout(BoxLayout):
    pass

class RightLayout(BoxLayout):
    pass

class TranslateApp(App):
	def build(self):
		self.source_lang = "auto"
		self.target_lang = "ru"
		return Interface()

	def on_source_language_russian(self, instance):
		if instance.state == 'down':
			self.source_lang = 'ru'
		else:
			# Если кнопка не нажата, source_lang остается прежним
			self.source_lang = 'auto'

	def on_source_language_english(self, instance):
		if instance.state == 'down':
			self.source_lang = 'en'
		else:
			# Если кнопка не нажата, source_lang остается прежним
			self.source_lang = 'auto'

	def on_source_language_italian(self, instance):
		if instance.state == 'down':
			self.source_lang = 'it'
		else:
			# Если кнопка не нажата, source_lang остается прежним
			self.source_lang = 'auto'

	def on_target_language_russian(self, instance):
		if instance.state == 'down':
			self.target_lang = 'ru'
		else:
			# Если кнопка не нажата, source_lang остается прежним
			self.target_lang = 'ru'

	def on_target_language_english(self, instance):
		if instance.state == 'down':
			self.target_lang = 'en'
		else:
			# Если кнопка не нажата, source_lang остается прежним
			self.target_lang = 'ru'

	def on_target_language_italian(self, instance):
		if instance.state == 'down':
			self.target_lang = 'it'
		else:
			# Если кнопка не нажата, source_lang остается прежним
			self.target_lang = 'ru'

	def translate_text(self):
		text_to_translate = self.root.ids.text_translate.text
		translated_text = GoogleTranslator(source=self.source_lang, target=self.target_lang).translate(text_to_translate)
		self.root.ids.translated_label.text = translated_text

	def exit_app(self):
		App.get_running_app().stop()

if __name__ == "__main__":
	TranslateApp().run()
