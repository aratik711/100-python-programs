"""

Define a custom exception class which takes a string message as attribute.

Hints:

To define a custom exception, we need to define a class inherited from Exception.

"""


class myError(Exception):

    """My own exception class

        Attributes:
            msg  -- explanation of the error
        """
    def __init__(self, msg):
        self.msg = msg


try:
    raise myError("Something went wrong")
except myError as err:
    print(err.msg)
