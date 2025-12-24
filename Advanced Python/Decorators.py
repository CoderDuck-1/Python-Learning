# Decorators add extra features to functions without modifying original function code.
# Commonly used for logging, authentication, timing how long a function takes, adding checks

# Decorators allow us to wrap a function in another function.
# example: Measuring the time a function took to calculate squares.

import time

def time_it(func):
  def wrapper(*args, **kwargs):
      start = time.time()
      result = func(*args, **kwargs)
      end = time.time()
      print(func.__name__ + " took " + str((end - start) * 1000) + " seconds")
      return result
  return wrapper

@time_it
def calc_squares(nums):
    #start = time.time()
    result = []
    for num in nums:
        result.append(num * num)
    #end=time.time()
    #print("calculating square took: "+ str((end - start)*1000 )+" seconds") #time.time measures in milliseconds
    return result

if __name__ == '__main__':
    print(calc_squares([1,2,3,4,5]))

