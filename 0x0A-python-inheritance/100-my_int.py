#!/usr/bin/python3
"""
my_int Class
"""


class MyInt(int):
    """Defines MyInt class"""
    def __eq__(self, self2):
        """invert equality"""
        return super().__ne__(self2)

    def __ne__(self, self2):
        """invert inequality"""
        return super().__eq__(self2)
