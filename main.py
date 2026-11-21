from kivy.app import App #импортируем приложение
from kivy.uix.button import Button #импортируем кнопку
from kivy.uix.label import Label #импортируем надпись
from kivy.uix.boxlayout import BoxLayout #импорт "коробочки", где все компонуется
from kivy.uix.screenmanager import ScreenManager, Screen #импорт экранов
from kivy.uix.screenmanager import WipeTransition


from kivy.config import Config

Config.set('graphics', 'resizable', '0')
Config.set('graphics', 'width', '342')
Config.set('graphics', 'height', '456')







class MenuScreen(Screen):
   def __init__(self, **kwargs):
       super().__init__(**kwargs)

   def start_game(self):
       self.manager.current = "game"

   def go_to_shop(self):
       self.manager.current = "shop"

class Rock(Button):
    # def __init__(self, **kwargs):
    #     super().__init__(**kwargs)

    def on_press(self):
        ...
        # print(self.parent.parent)
        # self.parent.parent.handle_click()


class GameScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.clicks = 0

    def handle_click(self):
        self.clicks += 1
        self.ids.clicks_count.text = f"Clicks: {self.clicks}"


    def go_to_menu(self):
        self.manager.current = "menu"

    def go_to_shop(self):
            self.manager.current = "shop"

class ShopScreen(Screen):
    def go_to_menu(self):
        self.manager.current = "menu"

    def start_game(self):
           self.manager.current = "game"


class ClickerApp(App): #класс, объект которого - приложение
   def build(self): #здесь происходит сборка приложения
      manager = ScreenManager(transition = WipeTransition(duration = 1))

      manager.add_widget(MenuScreen(name="menu"))
      manager.add_widget(GameScreen(name="game"))
      manager.add_widget(ShopScreen(name="shop"))

      return manager





app = ClickerApp()
app.run()

