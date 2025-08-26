from laba1 import Octagon #импортируем класс

def main(): #создаем функцию 
    O = Octagon(13) #добавляем объект
    O.S_opis() #используем все методы
    O.S_vpis()
    O.per()
    O.paint()
if __name__ == '__main__': #проверяем на прямой запуск
    main() #запускаем функцию