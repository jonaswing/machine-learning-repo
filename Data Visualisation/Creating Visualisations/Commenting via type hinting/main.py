# Comments may be negated by writing self-documenting code.
# One way of doing this is using type hinting to provide insights into code.
# Type hinting represents code annotations that may be used to check if
# you’re using the code correctly and may be read by external tooling (Lanzani, 2019).
#
# It allows a user to add details to the parameters of a method or function by
# adding a colon (:) and specifying the specific parameter type.
# The reader will immediately know which type of argument should be passed to this parameter.
#
# The function’s return type may also be indicated by typing -> and the return
# type before the final colon of the method or function header.

# In the following example, type hinting demonstrates that the method
# should receive an integer parameter for age and a string parameter for name.
# The return type is a string.
def demo_function(age: int, name: str) -> str:
    return("My name is {0} and I am {1} years old.".format(age,name))
