from kivymd.uix.dialog import MDDialog
from kivy.uix.screenmanager import ScreenManager, Screen
from kivymd.uix.screen import MDScreen
from kivy.properties import ObjectProperty
import sympy as sp
import time
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout

class MainScreenManager(ScreenManager):
    pass

class FirstPage(Screen):
    slide = ObjectProperty(None)
    f_in = ObjectProperty(None)
    a_in = ObjectProperty(None)
    output = []
    def sl(self,*args):
        self.slide.text = str(int(args[1]))
        print(self.slide.text)
        return self.slide.text
    def calc(self):
        products_container = self.ids.output
        products_container.clear_widgets()
        fun = self.f_in.text
        x0 = float(self.a_in.text)
        e = float("1e-{}".format(self.slide.text))
        x = sp.Symbol('x')
        exp = sp.sympify(fun) 
        dydx = exp.diff() 

        f = sp.lambdify(x, exp)
        df = sp.lambdify(x, dydx)

        xi_1 = x0
        st=time.time()
        l = []
        while True:
            if df(xi_1) == 0.0:
                print("Divide by zero error")
                break
            xi = xi_1 - f(xi_1)/df(xi_1)
            print("x =",xi,"f(x) =",f(xi))
            if abs(xi - xi_1) < e:
                break
            xi_1 = xi
            l.append("x = "+str(xi)+"  f(x) = "+str(f(xi)))

        for index, item in enumerate(l):
            products_container = self.ids.output
            height = 150 - (index * 60)  # decrease height by 10 for every iteration
            details = BoxLayout(size_hint_y=None, height=height, width=660, pos_hint={'top': 1})
            products_container.add_widget(details)

            if index == len(l) - 1:  # if it's the last iteration
                name = Label(text=str("Approximate root is: "+str(item)), size_hint_x=.3, color=(1, 1, 1, 1))
            else:
                name = Label(text=str(item), size_hint_x=.3, color=(1, 1, 1, 1))

            details.add_widget(name)
        et=time.time()
        print("Runtime:",et-st)    
        print("So the approximate root is :",xi)
    


    # def reset(self):
    #     self.p_n.text = ""
    #     self.p_a.text = ""


        

        # xi = str(xi)
        # products_container = self.ids.output
        # details = BoxLayout(size_hint_y=None,height=150,width=220,pos_hint={'top': 1})
        # products_container.add_widget(details)

        # name = Label(text=str("x ="+xi),size_hint_x=.3,color=(1,1,1,1))
        # details.add_widget(name)
        