# Author: CRS 01/14/22
temperature = int(input("Input a temperature."))
temperature_scale = str(input("Are you trying to find the temperature in celcius or farenheit? (c/f)"))
if temperature_scale == "c":
    try:
        answer1 = (temperature - 32) * (5/9)
        print(answer1)
    except:
        print("Temperature must be a number.")
    finally:
        answer3 = input("Find another temperature? (y/n)")
        if answer3 == "y":
            temperature
        else:
            print("Have a good day!")
elif temperature_scale == "f":
    try:
        answer1 = (temperature * 9/5) + 32
        print(answer1)
    except:
        print("Temperature must be a number.")
    finally:
        answer3 = input("Find another temperature? (y/n)")
        if answer3 == "y":
            temperature
        else:
            print("Have a good day!")
else:
    print("Input a number.")