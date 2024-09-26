# weather_advice.py

# Prompt user for the current weather
weather_condition = input("What's the weather like today? (sunny/rainy/cold): ").lower()

# Provide clothing recommendations based on the weather condition
if weather_condition == "sunny":
    print("Wear a t-shirt and sunglasses.")
elif weather_condition == "rainy":
    print("Don't forget your umbrella and a raincoat.")
elif weather_condition == "cold":
    print("Make sure to wear a warm coat and a scarf.")
else:
    print("Sorry, I don't have recommendations for this weather.")

