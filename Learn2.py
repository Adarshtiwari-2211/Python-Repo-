def greet(name):
    print(f"Hello, {name}!")

def add_numbers(a, b):
    return a + b

def main():
    name = "Alice"
    greet(name)
    
    num1 = 5
    num2 =2
    num2 = 10
    result = add_numbers(num1, num2)
    
    print(f"The sum of {num1} and {num2} is {result}")

if __name__ == "__main__":
    main()