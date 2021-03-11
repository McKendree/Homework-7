import numpy as np
import matplotlib.pyplot as plt
import time

def function_to_relax(x, c=2):
    return 1-np.exp(-1*c*x)

def relaxation(start_guess=1, func_to_relax=None,
               func_keyword_args=None, tolerance=1e-6):
    '''Uses relaxation method to find root of func_to_relax
    start_guess = the first guess to use
    func_keyword_args = extra keyword arguments to put into the function via a dictionary
    tolerance = the tolerance that relaxation will run until reaching'''
    difference=tolerance+1
    args=func_keyword_args
    args['x'] = start_guess
    while difference > tolerance:
        difference = abs(args['x']-func_to_relax(**args))
        args['x'] = func_to_relax(**args)
    return args['x']

if __name__ == "__main__":
    print("The solution for part a is:")
    print(relaxation(func_to_relax=function_to_relax,
                     func_keyword_args={'c':2}))

    #loop over r0 values from 0 to 5
    r0_values = np.arange(0, 5.0, 0.01)
    solutions = []
    for r0 in r0_values:
        answer = relaxation(func_to_relax=function_to_relax,
                            func_keyword_args={'c':r0})
        solutions.append(answer)

    #save the output data
    output_textfile = 'problem7_1_data.txt'
    np.savetxt(output_textfile,
               np.array(np.vstack((r0_values, solutions))).T,
               delimiter = ', ', header='R_0, Probability of epidemic',
               fmt = ('%.2f', '%.3e'))

    #plot the data
    plt.plot(r0_values, solutions)
    plt.title("Epidemic Threshold")
    plt.xlabel("Average Number of People Infected by One Sick Individual")
    plt.ylabel("Probability of Epidemic")
    plt.savefig("problem7_1_plot.png")
    plt.show()
