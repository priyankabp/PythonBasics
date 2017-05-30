#General imports, like import math, make all functionality from the math package available to you.
#However, if you decide to only use a specific part of a package, you can always make your import more selective:
#from math import pi

#Perform a selective import from the math package where you only import the radians function.
#Calculate the distance travelled by the Moon over 12 degrees of its orbit. Assign the result to dist.
#You can calculate this as r * phi, where r is the radius and phi is the angle in radians.
#To convert an angle in degrees to an angle in radians, use the radians() function, which you just imported.
#Print out dist.

# Definition of radius
r = 192500
phi = 12

# Import radians function of math package
from math import radians

# Travel distance of Moon over 12 degrees. Store in dist.
dist = r*radians(phi)

# Print out dist
print(dist)


#There are several ways to import packages and modules into Python. Depending on the import call, you'll have to use different Python code.
#Suppose you want to use the function inv(), which is in the linalg subpackage of the scipy package. You want to be able to use this
#function as follows:
#my_inv([[1,2], [3,4]])
#Which import statement will you need in order to run the above code without an error?
#import scipy
#import scipy.linalg
#from scipy.linalg import my_inv
#from scipy.linalg import inv as my_inv - correct answer