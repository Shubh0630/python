for numbers in range(1, 101):
    if numbers % 3 == 0 and numbers % 7 == 0:
        print("FizzBuzz")
    elif numbers % 3 == 0:
        print("Buzz")
    elif numbers % 7 == 0:
        print("Fizz")
    else:
        print(numbers)