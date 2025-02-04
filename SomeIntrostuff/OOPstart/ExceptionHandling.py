#try except final,  zero div,type erro,val error


try:
    number = int(input("Enter a number: "))
    print(1/number)
except ZeroDivisionError:
    print("You cannot divide by zero")
except ValueError:
    print("Numbers only please to be entered.")
except Exception:
    print("something went wrong")
finally:
    print("Always will execute !")
#only doing except Exception bad pract.

