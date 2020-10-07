# project-2b

# Author: Craig Sperlazza
# Date: 10/7/2019
# Description: Asks the user for a temperature in Celsius and converts it to Fahrenheit

print("Please enter a Celsius temperature.")
celsius_temp = float(input())

fahrenheit_temp = ((9/5) * celsius_temp) + 32
print("The equivalent Fahrenheit temperature is:")
print(fahrenheit_temp)