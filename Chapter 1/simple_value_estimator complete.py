def estimate_home_value(size_in_sqft, number_of_bedrooms):

    # Assume all homes are worth at least $50,000
    value1 = 50000

    # Adjust the value estimate based on the size of the house
    value1 = value1 + (size_in_sqft * 92)

    # Adjust the value estimate based on the number of bedrooms
    value1 = value1 + (number_of_bedrooms * 10000)

    return value1

# Estimate the value of our house:
# - 5 bedrooms
# - 3800 sq ft
# Actual value: $450,000

value1 = estimate_home_value(3800, 5)

print("Estimated valued:")
print(value1)