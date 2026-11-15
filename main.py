from kivy.app import App #импортируем приложение
from kivy.uix.button import Button #импортируем кнопку
from kivy.uix.label import Label #импортируем надпись
from kivy.uix.boxlayout import BoxLayout #импорт "коробочки", где все компонуется
from kivy.uix.screenmanager import ScreenManager, Screen #импорт экранов








class MenuScreen(Screen):
   def __init__(self, **kwargs):
       super().__init__(**kwargs)

       layout = BoxLayout(orientation="vertical") #создание коробочки
       label = Label(text="Грибооооооооооооочки") #создание надписи

       button = Button(text="Скушать грибочек =)") #создание кнопки
       button.on_press = self.start_game #действие при нажатии кнопки

       
       layout.add_widget(label) #добавление надписи в коробочку
       layout.add_widget(button) #добавление кнопки в коробочку

       self.add_widget(layout) #добавление коробочки в экран

   def start_game(self):
       self.manager.current = "game"


class GameScreen(Screen):
    pass


class ClickerApp(App): #класс, объект которого - приложение
   def build(self): #здесь происходит сборка приложения
      manager = ScreenManager()

      manager.add_widget(MenuScreen(name="menu"))
      manager.add_widget(GameScreen(name="game"))

      return manager





app = ClickerApp()
app.run()

