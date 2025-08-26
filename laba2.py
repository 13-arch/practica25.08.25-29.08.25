#13-arch


class Animal:

    def __init__(self,name ,age,species):
        self.name=name
        self.age=age
        self.species=species

    def make_sound(self):
        return f"{self.name} издает звук"

    def info(self):
        return f"Имя: {self.name}, возраст: {self.age}, вид: {self.species}"
    

class Dog(Animal):
    def __init__(self, name, age,breed,guard_status):
        super().__init__(name, age, "dog")
        self.breed=breed
        self.guard_status=guard_status
    
    def info(self):
        infa = super().info()
        return f"{infa}, порода: {self.breed}, охраноспособность: {'присутствует' if self.guard_status else 'отсутствует'}"
    
    def make_sound(self):
        return f"{self.name} гав-гав"
    
    def actions(self):
        if self.guard_status:
            return f"{self.name} на страже"
        else:
            return f"{self.name} не на страже"
        

