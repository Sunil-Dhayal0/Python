try:
    name = input("Enter Employee Name: ")
    age_input = input("Enter Employee Age: ")

    age = int(age_input)

    if age < 18:
        raise Exception("Employee must be at least 18 years old to be eligible.")

    print(f"Success! Employee {name} is eligible.")

except ValueError:
    print("Error: Age must be a numeric value (number).")

except Exception as e:
    print(f"Error: {e}")
