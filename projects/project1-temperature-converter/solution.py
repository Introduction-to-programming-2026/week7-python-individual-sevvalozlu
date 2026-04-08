# Project 1 — Temperature Converter
# Author: Şevval Özlü
# Date:   8 April 2026
#
# Instructions:
#   1. Read the README.md in this folder first.
#   2. Fill in the missing lines below.
#   3. Test with: 0°C → 32°F | 100°C → 212°F | -40°C → -40°F

# ── Your solution goes here ───────────────────────────────────────────────────

#celsius = float(input("Enter temperature in Celsius: "))

# TODO: calculate fahrenheit using the formula F = (C × 9/5) + 32
# fahrenheit = (celsius * 9/5) + 32

# TODO: print the result using an f-string
# print(f"{celsius}°C = {fahrenheit}°F")
# 
# 

# ── Bonus (optional) ─────────────────────────────────────────────────────────
choice = input("Convert: (1) Celsius to Fahrenheit  (2) Fahrenheit to Celsius: ")

if choice == "1":
    celsius = float(input("Enter temperature in Celsius: "))
    fahrenheit = (celsius * 9/5) + 32
    print(f"{celsius}°C = {fahrenheit}°F")

elif choice == "2":
    fahrenheit = float(input("Enter temperature in Fahrenheit: "))
    celsius = (fahrenheit - 32) * 5/9
    print(f"{fahrenheit}°F = {celsius}°C")
# Add a direction menu (C→F or F→C)
