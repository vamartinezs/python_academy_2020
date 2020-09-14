from io import open
import pickle


class Register:
    people = []

    def __init__(self):
        self.load()

    def add(self, p):
        self.people.append(p)
        self.save()

    def show(self):
        for p in self.people:
            print(p)

    def load(self):
        file = open('people_register.pckl', 'ab+')
        file.seek(0)
        try:
            self.people = pickle.load(file)
        except:
            print("Register file is empty")
        finally:
            file.close()
            del file

    def save(self):
        file = open('people_register.pckl', 'wb')
        pickle.dump(self.people, file)
        file.close()
        del file

    def __del__(self):
        self.save()
