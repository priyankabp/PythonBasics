#Import the numpy package as np, so that you can refer to numpy with np.
#Use np.array() to create a Numpy array from baseball. Name this array np_baseball.
#Print out the type of np_baseball to check that you got it right.

# Create list baseball
baseball = [180, 215, 210, 210, 188, 176, 209, 200]

# Import the numpy package as np
import numpy as np

# Create a Numpy array from baseball: np_baseball
np_baseball = np.array(baseball)

# Print out type of np_baseball
print(type(np_baseball))