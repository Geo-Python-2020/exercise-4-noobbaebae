def fahr_to_celsius(temp_fahrenheit):
    converted_temp = (temp_fahrenheit - 32) / 1.8
    return converted_temp

def temp_classifier(temp_celsius):
    if temp_celsius < -2:
        print(0)
    elif -2 <= temp_celsius <= 2:
        print(1)
    elif 2 <= temp_celsius <= 15:
        print(2)
    elif temp_celsius > 15:
        print(3)