def is_balanced(input_string):
    # initialize an empty list as the stack
    stack = []

    # iterate over each character in the string
    for i in input_string:
        if len(input_string) == 0:
            print("0 length is balanced")
            print("True")
            return True
        else:
            #print(stack)
            if i == "[" or i == "{" or i == "(":
                stack.append(i)
            if i == "]":
                if stack == []:
                    return False
                elif stack[-1] != "[":
                    #print("False, [")
                    return False
                elif stack[-1] == "[":
                    #print("balanced thus far []")
                    stack.pop()

            if i == "}":
                if stack == []:
                    return False
                elif stack[-1] != "{":
                    #print("False, }")
                    return False
                elif stack[-1] == "{":
                    #print("balanced thus far {}")
                    stack.pop()
            if i == ")":
                if stack == []:
                    return False
                elif stack[-1] != "(":
                    #print("False, ()")
                    return False
                elif stack[-1] == "(":
                    #print("balanced thus far ()")
                    stack.pop()
    if len(stack) != 0:
        return False
    else:
        return True

print(is_balanced("(x + y)"))
print(is_balanced("{x + (y + z)}"))
print(is_balanced("(x+y"))
print(is_balanced("[x + (y+ z])"))
print(is_balanced(""))
print(is_balanced("asd)"))
print(is_balanced("asdfgh"))

