from datetime import datetime
from io import open
import pickle
import os
from week2.simple_promo_class_exercise.Promo import Promo

abs_path = os.path.dirname(os.path.abspath(__file__))


class PromoRegisters:
    promos = []

    def __init__(self):
        self.load()

    def add(self, promo):
        self.promos.append(promo)
        self.save()

    def show(self):
        if len(self.promos)==0:
            print("No records available")
            return
        for promo in self.promos:
            print(promo)

    def load(self):
        file = open(os.path.join(abs_path,'promopersistance.pckl'), 'a+b')
        file.seek(0)
        try:
            self.promos = pickle.load(file)
        except :
            print("No records available")
        finally:
            file.close()
            del file

    def save(self):
        file = open(os.path.join(abs_path,'promopersistance.pckl'), 'wb')
        pickle.dump(self.promos, file)
        file.close()
        del file

    def __del__(self):
        self.save()


promos = PromoRegisters()
promos.add(Promo("Chicken", datetime(year=2021, day=14, month=2)))
promos.add(Promo("Meat", datetime(year=2019, day=14, month=2)))
promos.add(Promo("Donut", day= 13, year=1999, month=3))
promos.add(Promo("Waffle", day= 14, year=2022, month=4))
promos.show()


