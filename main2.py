from laba2 import Dog

def main():
    dog = Dog("Bobik", 1, "Лайка", True)
    print(dog.make_sound())
    print(dog.info())
    print(dog.actions())
    del dog
    print("Объект удален") 


if __name__ == "__main__":
    main()