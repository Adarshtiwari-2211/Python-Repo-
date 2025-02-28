class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def greet(self):
        print(f"Hello, my name is {self.name} and I am {self.age} years old.")

def main():
    person1 = Person("John", 25)
    person2 = Person("Jane", 30)
    
    person1.greet()
    person2.greet()

if __name__ == "__main__":
    main()
