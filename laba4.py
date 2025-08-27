#13-arch


import pandas as pd


class Summ:

    def __init__(self):
        self.data = pd.read_csv('var3.csv')
        self.df = self.data.copy() 
    
    def __pos__(self):
        a = self.df.shape[0] 
        self.df = self.df.drop_duplicates()
        b = self.df.shape[0] 
        c = a - b
        print(f'В файле удалено : {c} дубликатов')

    def transaction(self, summa=1000.00):
        df_below_summa = self.df[self.df["Сумма операции"] < summa]
        df_above_summa = self.df[self.df["Сумма операции"] >= summa]

        df_below_summa.to_csv("Transaction_amount_below_1000.csv", index=False)
        df_above_summa.to_csv("Transaction_amount_above_1000.csv", index=False)

        print("Сохранено")


