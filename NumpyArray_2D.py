#Before working on the actual MLB data, let's try to create a 2D Numpy array from a small list of lists.
#In this exercise, baseball is a list of lists. The main list contains 4 elements. Each of these elements is a list containing
#the height and the weight of 4 baseball players, in this order. baseball is already coded for you in the script.

#Instructions
#Use np.array() to create a 2D Numpy array from baseball. Name it np_baseball.
#Print out the type of np_baseball.
#Print out the shape attribute of np_baseball. Use np_baseball.shape.

# Create baseball, a list of lists
baseball = [[180, 78.4],
            [215, 102.7],
            [210, 98.5],
            [188, 75.2]]

# Import numpy
import numpy as np

# Create a 2D Numpy array from baseball: np_baseball
np_baseball = np.array(baseball)

# Print out the type of np_baseball
print(type(np_baseball))

# Print out the shape of np_baseball
print(np_baseball.shape)

#Baseball data in 2D form
#You have another look at the MLB data and realize that it makes more sense to restructure all this information in a 2D Numpy array.
# This array should have 1015 rows, corresponding to the 1015 baseball players you have information on, and 2 columns (for height and weight).
#The MLB was, again, very helpful and passed you the data in a different structure, a Python list of lists. In this list of lists,
#each sublist represents the height and weight of a single baseball player. The name of this embedded list is baseball.
#Can you store the data as a 2D array to unlock Numpy's extra functionality?

#Instructions
#Use np.array() to create a 2D Numpy array from baseball. Name it np_baseball.
#Print out the shape attribute of np_baseball.

# baseball is available as a regular list of lists

# Import numpy package
import numpy as np

# Create a 2D Numpy array from baseball: np_baseball
np_baseball = np.array(baseball)

# Print out the shape of np_baseball
print(np_baseball.shape)

#Output
#<script.py> output:
#    (1015, 2)