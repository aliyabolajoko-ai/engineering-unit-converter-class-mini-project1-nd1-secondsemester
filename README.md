# Engineering Unit Converter

## Project Description

A beginner-friendly Python program that converts values between common engineering units.

## Features

- Length: millimetres and inches
- Temperature: Celsius and Fahrenheit
- Mass: kilograms and pounds
- Speed: kilometres per hour and metres per second
- Conversion history while the program is running
- Bonus: pressure conversion between kilopascals and bar
- Basic input validation, including negative temperatures

## How to Run

• Download or clone this repository.

• Open the engineering_unit_converter.py file in an environment that supports Python 3.

• Run the program.

If you are using a terminal, you can run it with:

   `python engineering_unit_converter.py`

Note: No specific application is required. You can use any environment that supports Python.

## Conversion Formulas

| Conversion | Formula |
|---|---|
| Millimetres to inches | mm / 25.4 |
| Inches to millimetres | inches * 25.4 |
| Celsius to Fahrenheit | (C * 9/5) + 32 |
| Fahrenheit to Celsius | (F - 32) * 5/9 |
| Kilograms to pounds | kg * 2.20462 |
| Pounds to kilograms | lb / 2.20462 |
| km/h to m/s | km/h / 3.6 |
| m/s to km/h | m/s * 3.6 |
| kPa to bar | kPa / 100 |
| bar to kPa | bar * 100 |

## Python Concepts Used

- Functions
- Dictionaries
- Lists and tuples
- `while` and `for` loops
- Conditional statements (`if`, `elif`, `else`)
- User input and conversion with `float()`
- Basic input validation

## Conversion History

The program stores conversions in a list while it is running. The history is cleared when the program is closed.
