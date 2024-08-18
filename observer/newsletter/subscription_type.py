from enum import Enum, auto

class SubscriptionType(Enum): 
    NEW_BLOGS = auto()
    NEWSLETTER = auto()

"""
>>Notes about Enum in python<<
In Python, an Enum (enumeration) is a set of named constants. 
It's useful for creating a group of related, unchangeable values that can be used to represent a fixed number of choices or categories. 
Enums provide a way to create more readable and self-documenting code by giving meaningful names to constant values.

Key points about Enums in Python:

Defined using the class keyword and inheriting from enum.Enum
Members are constants with unique values
Can be iterated over
Support comparison and hashing
Prevent accidental creation of new members

Enums are particularly useful when you have a fixed set of options or states in your program, 
like days of the week, card suits, or status codes.
"""