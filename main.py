import threading
import os
import asyncio
import edge_tts
from kivy.app import App
from kivy.clock import Clock
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.scrollview import ScrollView
from kivy.uix.textinput import TextInput


class EnglishTutorApp(App):

  def build(self):
    self.title = "المعلم الخاص بالذكاء الاصطناعي"
    root_layout = BoxLayout(
        orientation="vertical", padding=10, spacing=10
    )

    header_label = Label(
        text="🗣️ المعلم الخاص بالذكاء الاصطناعي",
        size_hint_y=None,
        height=50,
        font_size=18,
    )
    root_layout.add_widget(header_label)

    self.chat_history = Label(
        text=(
            "Welcome! Type your message in English to get responses and"
            " meanings...\n\n"
        ),
        size_hint_y=None,
        halign="left",
        valign="top",
    )
    self.chat_history.bind(
        texture_size=self.chat_history.setter("size")
    )

    scroll = ScrollView(size_hint=(1, 1))
    scroll.add_widget(self.chat_history)
    root_layout.add_widget(scroll)

    input_layout = BoxLayout(
        orientation="horizontal", size_hint_y=None, height=50, spacing=10
    )

    self.user_input = TextInput(
        hint_text="Type here in English...",
        multiline=False,
        font_size=16,
    )
    input_layout.add_widget(self.user_input)

    send_button = Button(
        text="Send",
        size_hint_x=None,
        width=100,
        background_color=(0.1, 0.6, 1, 1),
    )
    send_button.bind(on_press=self.send_message)
    input_layout.add_widget(send_button)

    root_layout.add_widget
