'''

from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.scatter import Scatter
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.boxlayout import BoxLayout

class MainApp(App):
    def build(self):
        button = Button(text='Hello from Kivy',size_hint=(.5, .5),pos_hint={'center_x': .5, 'center_y': .5})

        button.bind(on_press=self.on_press_button)
        
        textinput = TextInput (font_size = 50,)

        


        return button

    def on_press_button(self, instance):
        print('You pressed the button!')
    def on_text(instance, value):
        print('The widget', instance, 'have:', value)

    


if __name__ == '__main__':
    app = MainApp()
    app.run()

'''
#модули
import random
from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
import wikipedia
import time
#Главная
class Design():
    pass
class MainApp(App):
    def build(self):
        self.TextBoxStore = []# переходник для функций
        self.OutputLabel = []# переходник для функций
        box = BoxLayout(orientation = 'vertical')
        output_label = TextInput(text='Hello from Kivy',pos_hint={'center_x': 0.5, 'center_y': .2}, multiline=True,readonly=True)
        #button = Button(text='Search',pos_hint={'center_x': 0.5, 'center_y': .2})
        button = Button(text='Поиск',size_hint_y=None,height=100)
        
        button.bind(on_press=self.textPrint)
        
        textB = TextInput (font_size = 50, size_hint_y=None,height=100)
        
        floatLay = FloatLayout()
        
        print(textB.text)
        
        box.add_widget(textB)
        box.add_widget(button)
       
        box.add_widget(output_label)
        
        self.OutputLabel.append(output_label) # Поле ввода и табличка помещаются в списки
        self.TextBoxStore.append(textB)
        
        
        return box # материнский объект для всех виджетов
    def button_pressed(self, instance):
        print("ah")
    def textPrint(self, widget): # Вывод результата(ов) поиска
        
        try:
            #self.OutputLabel[0].text = "Идет поиск. Пожалуйста, подождите"
            
            item = self.TextBoxStore[0]
            if item.text == "":
                
                self.OutputLabel[0].text = "Вы ничего не ввели. "
                
            else:
                wikipedia.set_lang("ru")
                self.OutputLabel[0].text = wikipedia.summary(item.text)
                print(wikipedia.summary(item.text))
        except:
            wikipedia.set_lang("ru")
            if wikipedia.search(item.text) == []:
                replies = ["Без понятия :(", "Не знаю о чем вы.", "???", "У меня нет идей."]
                self.OutputLabel[0].text = random.choice(replies)

            else:
                tab = wikipedia.search(item.text)
                for i in range(0, len(tab)):
                    
                    self.OutputLabel[0].text = self.OutputLabel[0].text + f" {tab[i]},"
                    
  
# запуск
if __name__ == '__main__':
    app = MainApp()
    app.run()
