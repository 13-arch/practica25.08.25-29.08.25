#13-arch


import math
import matplotlib.patches
import matplotlib.pyplot as plt


class Octagon:

    def __init__(self,a):
        self.a=a
        self.corner=135
        self.k=1+math.sqrt(2)

    def S_opis(self):
        self.R=self.a*math.sqrt(self.k/(self.k-1))
        self.S=self.R**2*3.14
        print(f'Радиус описанной окружности: {self.R}')
        print(f'Площадь описанной окружности: {self.S}')

    def S_vpis(self):
        self.r=math.sqrt(2)/2*self.a
        self.s=self.r**2*3.14
        print(f'Радиус вписанной окружности:{self.r}')
        print(f'Площадь вписанной окружности: {self.s}')

    def per(self):
        self.perimeter=8*self.a
        print(f'периметр октагона :{self.perimeter}')

    def paint(self): #выводим графики на экран
            self.square = 2*self.k*self.a**2
            self.mal_r = math.sqrt(self.square/8/(math.sqrt(2)-1))
            self.bol_r = math.sqrt(self.square/2/math.sqrt(2))

            plt.xlim(-20, 20)
            plt.ylim(-20, 20)
            plt.grid()
            axes = plt.gca()

            polygon_1 = matplotlib.patches.Polygon([(self.r, self.a/2),  #создаем октагон
                                                    (self.r, -self.a/2),
                                                    (self.a/2, -self.r),
                                                    (-self.a/2, -self.r),
                                                    (-self.r, -self.a/2),
                                                    (-self.r, self.a/2), 
                                                    (-self.a/2, self.r), 
                                                    (self.a/2, self.r)], 
                                                    fill = False, color = 'red')

            circle1 = matplotlib.patches.Circle((0, 0), radius=self.R, fill = False, color = 'black')  #описанная окружность
            circle2 = matplotlib.patches.Circle((0, 0), radius=self.r, fill = False, color = 'blue') #вписанная окружность
            axes.add_patch(circle1)
            axes.add_patch(circle2)
            axes.add_patch(polygon_1)
            plt.show()
        