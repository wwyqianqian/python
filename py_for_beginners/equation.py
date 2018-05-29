# import math
# def main():
#     print("quadratic")
#     try:
#         a, b, c = eval(input("enter the coefficients: a b c"))
#         discroot = math.sqrt(b * b - 4 * a * c)
#         root1 = (-b + discroot) / (2 * a)
#         root2 = (-b - discroot) / (2 * a)
#         print("\nThe solutions are:", root1, root2)
#     except ValueError as excObj:
#         if str(excObj) == "math domain error":
#             print("No real roots.")
#         else:
#             print("You have not give me the right number.")
#     except NameError:
#         print("\nYou did not enter 3 numbers.")
#     except TypeError:
#         print("\nYour inputs were not all numbers.")
#     except SyntaxError:
#         print("\nYour inputs was SyntaxError.")
#     except:
#         print("Sth went wrong……")
# main()

import math


def main():
    a, b, c = eval(input("a, b, c"))
    delta = b * b - 4 * a * c
    if a == 0:
        x = -b / c
        print("\nThere is only one solution", x)
    elif delta < 0:
        print("\nThe equation has no real roots.")
    elif delta == 0:
        x = -b / (2 * a)
        print("\nThere is a double root at:", x)
    else:
        disc = math.sqrt(delta)
        x1 = (-b + disc) / 2 * a
        x2 = (-b - disc) / 2 * a
        print("\nThe solutions are:", x1, x2)


main()
