import numpy

def L1(r):
    '''L1 point equation'''
    G = 6.674e-11
    M = 1.989e30
    m = 5.972e24
    R = 1.496e11
    omega = 1.991e-7
    return (G*M/r**2)-(G*m/(R-r)**2)-omega**2*r

def L1_deriv(r):
    '''L1 point equation derivative'''
    G = 6.674e-11
    M = 1.989e30
    m = 5.972e24
    R = 1.496e11
    omega = 1.991e-7
    return (-2*G*M/r**3)-(2*G*m/(R-r)**3)-omega**2

def L2(r):
    '''L2 point equation'''
    G = 6.674e-11
    M = 1.989e30
    m = 5.972e24
    R = 1.496e11
    omega = 1.991e-7
    return (G*M/r**2)+(G*m/(R-r)**2)-omega**2*r

def L2_deriv(r):
    '''L2 point equation derivative'''
    G = 6.674e-11
    M = 1.989e30
    m = 5.972e24
    R = 1.496e11
    omega = 1.991e-7
    return (-2*G*M/r**3)+(2*G*m/(R-r)**3)-omega**2

def newtonsMethod(func=None, deriv=None, firstGuess=None, maxIterations=100):
    '''Uses Newtons method to calculate root of func
    func = function to find root of
    deriv = derivative of function
    firstGuess = the first guess value to try
    maxIterations = the number of iterations to use'''
    guess = firstGuess
    for i in range(maxIterations):
        guess = guess - (func(guess)/deriv(guess))
    return guess

def secantMethod(func=None, point1=None, point2=None, maxIterations=100):
    '''Uses secant method to calculate root of func
    func = function to find root of
    point1 = one of the two first point to try
    point2 = second of the two first point to try
    maxIterations = the number of iterations to use'''
    for i in range(maxIterations):
        point3 = point1-func(point1)*(point2-point1)/(func(point2)-func(point1))
        point2 = point1
        point1 = point3
    return point1

if __name__ == "__main__":
    R = 1.496e11 #distance between the Sun and Earth
    print("L2 distance (m) from the Earth, away from the Sun, according to Newton's method:\n", abs(R-newtonsMethod(L2,L2_deriv,1)))
    print("L2 distance (m) from the Earth, away from the Sun, according to secant method:\n" , abs(R-secantMethod(L2,1,2)))
    print("\nL1 distance (m) from the Earth, towards the Sun, according to Newton's method:\n", abs(R-newtonsMethod(L1,L1_deriv,1)))
    print("L1 distance (m) from the Earth, towards the Sun, according to secant method:\n" , abs(R-secantMethod(L1,1,2)))
