def print_even_numbers(numbers):
    for num in numbers:
        if num % 2 == 0:
            print(f"Even number: {num}")

def main():
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    print_even_numbers(numbers)

if __name__ == "__main__":
    main()
