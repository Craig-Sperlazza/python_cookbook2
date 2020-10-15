import first_module 

#if you run this file it will run first module and return (as long as print is uncommented):
# first_module's __name__ is equal to: first_module
# (if you run the other file it returns: first_module's __name__ is equal to:__main__)

#will return __main for second module
print(f"second_module's __name__ is equal to: {__name__}")

#now the program returns as long as the print() in module 1 is uncommented----the iff will not run here:
# first_module's __name__ is equal to: first_module
# second_module's __name__ is equal to: __main__

# note: you can call the main directly even if it doesnt run on execution
first_module.main()