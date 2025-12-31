# exception - An event that interrupts the flow of a program
#             (ZerDivisionError, TypeError, ValueError)
#              1. try 2. except , 3. finally

"""
    syntax:--->
    try:
        #try some code
    except Exception:
        # Handle an Exception
    finally:
        # Do some clean up
"""

try:
    a = int(input("Enter number: "))
    print(1/a)
except ZeroDivisionError:
    print("You dont divide number by Zero .")
except ValueError:
    print("Give an integer .")
except Exception:
    print("Something went wrong .")
finally:
    print("Do some cleanups")

