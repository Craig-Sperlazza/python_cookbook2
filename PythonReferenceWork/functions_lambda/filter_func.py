# https://www.youtube.com/watch?v=09XRMXcCofM&list=PLzMcBGfZo4-nhWva-6OVh1yKWHBs4o_tv&index=4

# commonly used back to back with map function

def add7(x):
    return x + 7


def is_odd(x):
    return x % 2 != 0


lst = [1, 2, 3, 4, 5, 6, 7, 8, 9]

new_lst = list(filter(is_odd, lst))

# follow filter with map ----we filter it and then we change it
c = list(map(add7, new_lst))

print(c)

# note we can do it in the same line
d = list(map(add7, filter(is_odd, lst)))

print(d)
