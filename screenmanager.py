from kivy.uix.screenmanager import ScreenManager, Screen
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
            l.append("x = "+str(xi)+"  f(x) = "+str(f(xi)))
            if abs(xi - xi_1) < e:
                break
            xi_1 = xi
            
        for index,item in enumerate(l):
            products_container = self.ids.output
            details = BoxLayout()
            products_container.add_widget(details)

            name = Label(text=str(item), color=(1,1,1,1))
            details.add_widget(name)

            if index == len(l)-1:
                name.text = "Answer: " + name.text

        et=time.time()
        print("Runtime:",et-st)    
        print("So the approximate root is :",xi)