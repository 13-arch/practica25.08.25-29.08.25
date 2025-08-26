import pandas as pd
import matplotlib.pyplot as plt
from llogg import logging
# Класс
class Players:
    @logging
    def __init__(self, file_name):
        self.file_name = file_name
        self.df = pd.read_csv(file_name)
        
    def plot_country_distribution(self):
        # Группируем данные по странам и считаем количество игроков в каждой стране
        country_counts = self.df['country'].value_counts()
        
        # Круговая диаграмма
        plt.figure(figsize=(13, 13))
        plt.pie(country_counts, labels=country_counts.index, autopct='%1.1f%%', startangle=90, colors=plt.cm.Paired.colors)
        plt.title('Количество игроков PS')
        plt.axis('equal')  
        plt.show()