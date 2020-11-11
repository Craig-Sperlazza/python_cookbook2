import matplotlib.pyplot as plt

def graph_operation(x, y):
    print(f"This is a function that graphs {x} and {y}")
    plt.plot(x,y)
    plt.show()

#the first way is better
x1 = [1, 2, 3]
y1 = [4, 5, 6]

graph_operation(x1, y1)

#not a great way but you can pass it this way
graph_me = [x1, y1]
graph_operation(*graph_me)