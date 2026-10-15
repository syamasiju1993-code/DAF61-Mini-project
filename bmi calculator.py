def calculate_bmi(weight,height):
      bmi =weight /(height ** 2)
      return bmi
weight =float(input("enter your weight in kg: "))
height =float(input("enter  your height in meters: "))
your_bmi = calculate_bmi(weight,height)
print(f"your bmi is :{your_bmi:.2f}")