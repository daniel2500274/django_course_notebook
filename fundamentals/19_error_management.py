def divide_numbers():
    try:
        a = int(input("Please enter a numerator: "))
        b = int(input("Please enter a denominator: "))
        return a / b
    except ZeroDivisionError:
        return "Cannot divide by zero"
    except Exception as error:
        print(type(error))
    else:
        pass
    finally:
        print("Thank you for using this program")
print(divide_numbers())