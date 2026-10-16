from kivy.app import App
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
        hint_text="Type here in English...", multiline=False, font_size=16
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

    root_layout.add_widget(input_layout)
    return root_layout

  def send_message(self, instance):
    text = self.user_input.text.strip()
    if not text:
      return
    self.chat_history.text += f"\nYou: {text}"
    user_msg = text
    self.user_input.text = ""
    self.process_ai_response(user_msg)

  def process_ai_response(self, user_text):
    text_lower = user_text.lower()

    if "hi" in text_lower or "hello" in text_lower or "hey" in text_lower:
      reply = (
          "Hello there! It is wonderful to practice English with you. How is"
          " your day going?"
      )
      meaning = "المعنى: أهلاً بك! من الرائع ممارسة الإنجليزية معك. كيف حال يومك؟"
    elif "how are you" in text_lower:
      reply = (
          "I'm doing great, thank you! What would you like to talk about"
          " today?"
      )
      meaning = "المعنى: أنا بخير، شكراً لك! عن ماذا تحب أن نتحدث اليوم؟"
    elif "name" in text_lower:
      reply = (
          "I am your personal English conversation tutor. What is your name?"
      )
      meaning = "المعنى: أنا معلمك الخاص للغة الإنجليزية. ما هو اسمك؟"
    else:
      reply = (
          f"That's interesting! You mentioned '{user_text}'. Can you tell me"
          " more about it?"
      )
      meaning = f"المعنى: هذا أمر ممتع! لقد ذكرت '{user_text}'. هل يمكنك إخباري بالمزيد؟"

    full_display = f"{reply}\n({meaning})"
    self.update_chat(full_display)

  def update_chat(self, text):
    self.chat_history.text += f"\n\nTutor: {text}\n-------------------"


if __name__ == "__main__":
  EnglishTutorApp().run()
