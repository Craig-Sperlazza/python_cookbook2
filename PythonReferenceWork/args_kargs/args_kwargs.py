# https://www.youtube.com/watch?v=j0Mxlxedff8&list=PLUDwpEzHYYLvxZO0QTnhhTP7OaBzovwW4&index=24

# *args allows us to pass variable number of arguments to the function
#**kwargs allows us to pass variable number of keyword arguments (key=value)


#create a function that sums all entered numbers
def sum(*args):
    sum_num = 0
    for i in args:
        sum_num += i
    print (f"The sum is {sum_num}")

# add in arguments from a list using *kargs as an argument for each paramter in function
# arguments must equal the number parameters in this example
def my_three(a, b, c):
    print(a, b, c)


def my_funct(**kwargs):
    for i, j in kwargs.items():
        print(i,j)



if __name__ =="__main__":
    sum(2, 3, 4, 5)

    args = [2, 4, 6]
    my_three(*args)

    #**kwargs example 1
    #when you do it this way the key must match the parameters in the function (funct(a, b, c)---keys must be a, b, c)
    arg_dict = {'a':'one', 'b': 2, 'c':[6, 7, 8]}
    my_three(**arg_dict)

    #**kwargs example 2
    my_funct(a='two', b=3, c=[8, 9, 10], red=2)

