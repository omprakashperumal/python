# sample_program.py

def greet(name):
    print(f"Hello, {name}! Welcome to Python.")

def add(a, b):
    return a + b

def main():
    name = input("Enter your name: ")
    greet(name)

    print("Let's do a quick addition.")
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
    
    result = add(num1, num2)
    print(f"The sum of {num1} and {num2} is: {result}")

if __name__ == "__main__":
    main()

