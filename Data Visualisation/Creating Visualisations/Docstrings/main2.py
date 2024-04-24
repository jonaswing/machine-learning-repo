class MyClass:
    something = 0
    # Sets the docstrings property of the class
    __doc__ = "This is an overview of what MyClass does."

    def my_class_function():
        # A one-line docstring for this method
        '''This is an overview of what my_class_function does'''
        print("Called MyClass function")


def my_function():
    print("Called function")

# Sets the docstrings property of the function.
my_function.__doc__ = "This is an overview of what MyFunction does."

help(MyClass)
print()
help(my_function)





