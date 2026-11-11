# Engineering Unit Converter
# A simple Python program for converting engineering units.

def mm_to_inches(value):
    return value / 25.4

def inches_to_mm(value):
    return value * 25.4

def celsius_to_fahrenheit(value):
    return (value * 9 / 5) + 32

def fahrenheit_to_celsius(value):
    return (value - 32) * 5 / 9

def kg_to_pounds(value):
    return value * 2.20462

def pounds_to_kg(value):
    return value / 2.20462

def kmh_to_ms(value):
    return value / 3.6

def ms_to_kmh(value):
    return value * 3.6

def kpa_to_bar(value):
    return value / 100

def bar_to_kpa(value):
    return value * 100


# Each option stores its name, units, conversion function and minimum value.
CONVERSIONS = {
    "Length": [
        ("Millimetres to Inches", "mm", "in", mm_to_inches, 0),
        ("Inches to Millimetres", "in", "mm", inches_to_mm, 0)
    ],
    "Temperature": [
        ("Celsius to Fahrenheit", "C", "F", celsius_to_fahrenheit, -273.15),
        ("Fahrenheit to Celsius", "F", "C", fahrenheit_to_celsius, -459.67)
    ],
    "Mass": [
        ("Kilograms to Pounds", "kg", "lb", kg_to_pounds, 0),
        ("Pounds to Kilograms", "lb", "kg", pounds_to_kg, 0)
    ],
    "Speed": [
        ("Kilometres per hour to Metres per second", "km/h", "m/s", kmh_to_ms, 0),
        ("Metres per second to Kilometres per hour", "m/s", "km/h", ms_to_kmh, 0)
    ],
    "Pressure": [
        ("Kilopascals to Bar", "kPa", "bar", kpa_to_bar, 0),
        ("Bar to Kilopascals", "bar", "kPa", bar_to_kpa, 0)
    ]
}

conversion_history = []


def is_number(value):
    value = value.strip()

    if value.startswith("-"):
        value = value[1:]

    return value.replace(".", "", 1).isdigit()


def do_conversion(category):
    options = CONVERSIONS[category]

    print("\n" + category + " Conversion")
    for number in range(len(options)):
        print(str(number + 1) + ". " + options[number][0])

    choice = input("Choose a conversion (1 or 2): ")

    while choice != "1" and choice != "2":
        print("Invalid choice. Please enter 1 or 2.")
        choice = input("Choose a conversion (1 or 2): ")

    option = options[int(choice) - 1]
    from_unit = option[1]
    to_unit = option[2]
    formula = option[3]
    minimum = option[4]

    while True:
        raw_value = input("Enter value in " + from_unit + ": ")

        if is_number(raw_value):
            value = float(raw_value)

            if value >= minimum:
                break
            else:
                print("Value is below the allowed minimum.")
        else:
            print("Please enter a valid number.")

    result = formula(value)
    print("Result:", round(result, 4), to_unit)

    record = str(value) + " " + from_unit + " = " + str(round(result, 4)) + " " + to_unit
    conversion_history.append(record)


def show_history():
    print("\nConversion History")

    if len(conversion_history) == 0:
        print("No conversions have been made yet.")
    else:
        number = 1
        for record in conversion_history:
            print(str(number) + ". " + record)
            number += 1


# Main menu
while True:
    print("\nENGINEERING UNIT CONVERTER")
    print("1. Length")
    print("2. Temperature")
    print("3. Mass")
    print("4. Speed")
    print("5. Conversion History")
    print("6. Pressure (Bonus)")
    print("7. Exit")

    menu_choice = input("Enter your choice: ")

    if menu_choice == "1":
        do_conversion("Length")
    elif menu_choice == "2":
        do_conversion("Temperature")
    elif menu_choice == "3":
        do_conversion("Mass")
    elif menu_choice == "4":
        do_conversion("Speed")
    elif menu_choice == "5":
        show_history()
    elif menu_choice == "6":
        do_conversion("Pressure")
    elif menu_choice == "7":
        print("Thank you for using the Engineering Unit Converter.")
        break
    else:
        print("Invalid menu choice. Please try again.")
