import math


def my_pi(target_error):
    """
    Implementation of Gauss–Legendre algorithm to approximate PI from https://en.wikipedia.org/wiki/Gauss%E2%80%93Legendre_algorithm

    :param target_error: Desired error for PI estimation
    :return: Approximation of PI to specified error bound
    """

    ### YOUR CODE HERE ###
#starting values
    a=1
    b=1/math.sqrt(2)
    t=1/4
    p=1

    #calculate the first approximation
    pi_approx=((a+b)**2)/(4*t)

    #keep calculating until the error is small enough
    while abs(math.pi-pi_approx)>=abs(target_error):

        #save the old value of a
        old_a=a

        #new values
        a=(a+b)/2
        b=math.sqrt(old_a*b)
        t=t-p*(old_a-a)**2
        p=2*p

        #calculate new approximation of pi
        pi_approx=((a+b)**2)/(4*t)

    # change this so an actual value is returned
    return pi_approx




desired_error = 1E-10

approximation = my_pi(desired_error)

print("Solution returned PI=", approximation)

error = abs(math.pi - approximation)

if error < abs(desired_error):
    print("Solution is acceptable")
else:
    print("Solution is not acceptable")
