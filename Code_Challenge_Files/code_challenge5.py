
def code5():
    print("Farenheit to Celsius Converter Program!")
    fahrenheit = eval(input("Enter temperature in Fahrenheit: "))
    celsius = (fahrenheit - 32) * 5 / 9
    print(f" {fahrenheit}degrees Fahrenheit converter to celsius is {celsius} degrees")
    print(round(celsius, 2))