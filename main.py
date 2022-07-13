import sys
import matplotlib.pyplot as plt
import numpy as np

epsilon = sys.float_info.epsilon #initialize the value of espilon
def f(x):
    return x**3-x+6 #The function on which we will examine the root

def regulaFalsi(a,b):
    """
    :param a:User guessing to the edge 1
    :param b:User guessing to the edge 2
    :return: The root of the function
    """
    c = 0
    stage = 1
    while abs(f(c)) > epsilon: #We will check if the value is equal to 0
        c = b - (f(b) * (b - a)) / (f(b) - f(a)) #Calculate new approximated root
        print(f'Iteration {stage} : a = {a} , b = {b} ,c = {c}')
        if f(a) * f(c) < 0:
            b = c
        elif f(b) * f(c) < 0:
            a = c
        stage += 1 #Increase the number of stage(iterations) by 1
    return c #return the root

def main():
  a =  float(input("Enter the first guess ")) #We will ask the user to enter an edge value
  b = float(input("Enter the second guess ")) #We will ask the user to enter an edge value
  if f(a)*f(b) > 0: #We will check if the result obtained is less than zero
      print("you enter wrong guess try again")
      main() #Since a result not less than 0 we will enter the function again
  else:
    result = regulaFalsi(a,b)
    print(f'The root is : {result}') #Calling a function and printing a return value
  y = np.linspace(a,b)
  plt.plot(y, f(y))
  plt.annotate("Root",(result,f(result)))
  plt.plot(result,f(result,),"-ro",label = 'marker only')
  plt.show()

if __name__ == "__main__": #main function
    main()






