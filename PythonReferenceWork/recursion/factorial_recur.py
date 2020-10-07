def factorial(num):
    """
    Returns the factorial of num
    """
    if num == 0:
        return 1
    else:
        return num * factorial(num-1)

print(factorial(5))

"""
Can write it either way
"""
"""
def factorial(num):    
  """    
  #Returns the factorial of num    
  """    
  if num == 0:        
    return 1    
    
  return num * factorial(num-1)
"""
