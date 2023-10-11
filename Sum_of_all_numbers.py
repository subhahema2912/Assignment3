def sum_numbers_from_user_input():
    while True:
        size_input = input("Enter the size of the list: ")
        if size_input.isdigit():
            size = int(size_input)
            break
        else:
            print("Invalid input. Please enter a positive integer for the size.")

    numbers = []
    for i in range(size):
        while True:
            value_input = input(f"Enter value {i + 1}: ")
            if value_input.replace(".", "", 1).isdigit():
                value = float(value_input)
                numbers.append(value)
                break
            else:
                print("Invalid input. Please enter a numeric value.")

    result = sum(numbers)
    return result

total = sum_numbers_from_user_input()
print(f"The sum of the numbers in the list is: {total}")