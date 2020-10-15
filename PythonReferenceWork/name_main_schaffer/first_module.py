# https://www.youtube.com/watch?v=sugvnHA7ElY

# when python runs a file directly it sets the __name__ variable equal to '__main__'
# so if you run the script directly then name == main, it will execute anything you run in your: if __name__ = '__main__':
# if you dont run it directly, i.e. import it for functions or whatver, name will not equal main and the if __name__ = '__main__': will NOT run
# if you import a module, its going to set the name variable to the name of the file 

# print(f"first_module's __name__ is equal to: {__name__}") # returns first_module's __name__ is equal to: __main__

print("this will always be run")

def main():
    print(f"first_module's __name__ is equal to: {__name__}") 
    # returns first_module's __name__ is equal to: __main__


if __name__ == '__main__':
    main()
else:
    print("I am imported")