#The MLB also offers to let you analyze their weight data. Again, both are available as regular Python lists: height and weight.
#height is in inches and weight is in pounds.
#It's now possible to calculate the BMI of each baseball player. Python code to convert height to a Numpy array with the correct units is ' \
#  'already available in the workspace. Follow the instructions step by step and finish the game!

#Instructions
#Create a Numpy array from the weight list with the correct units. Multiply by 0.453592 to go from pounds to kilograms.
# Store the resulting Numpy array as np_weight_kg.
#Use np_height_m and np_weight_kg to calculate the BMI of each player. Use the following equation:
#BMI=weight(kg)height(m)2
#BMI=weight(kg)/height(m)**2
#Save the resulting numpy array as bmi.
#Print out bmi.

# height and weight are available as a regular lists
height = [5.5,5.11]
weight = [120,170]
# Import numpy
import numpy as np

# Create array from height with correct units: np_height_m
np_height_m = np.array(height) * 0.0254

# Create array from weight with correct units: np_weight_kg
np_weight_kg = np.array(weight) * 0.453592

# Calculate the BMI: bmi
bmi = np_weight_kg/np_height_m**2

# Print out bmi
print(bmi)