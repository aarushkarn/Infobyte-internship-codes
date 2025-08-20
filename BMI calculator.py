def calculate_bmi(weight_kg, height_cm):
    height_m = height_cm / 100
    bmi = weight / (height_m ** 2)
    return bmi

if __name__ == "__main__":
    try:
        weight = float(input("Enter your weight in kilograms: "))
        height = float(input("Enter your height in centimeters: "))
        bmi = calculate_bmi(weight, height)
        print(f"Your BMI is: {bmi:.2f}")

        # BMI Categories
        if bmi < 18.5:
            print("Category: Underweight")
        elif 18.5 <= bmi < 24.9:
            print("Category: Normal weight")
        elif 25 <= bmi < 29.9:
            print("Category: Overweight")
        else:
            print("Category: Obesity")
    except ValueError:
        print("Please enter valid numbers for weight and height.")
