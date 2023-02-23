def cod1():
    try:
        totalValue  = float(input("Enter total value: "))
        value = float(input("Enter value: "))
        print("That is", ((value / totalValue)* 100), "%")
    except:
        print("You need to enter a number. Run the program again.")

def cod2():
    try:
        totalValue  = float(input("Enter total value: "))
        value = float(input("Enter value: "))
        print("That is", ((value / totalValue)* 100), "%")
    except ZeroDivisionError:
        print("Your total value canot be zero")

    except:
        print("You need to enter a number. Run the program again.")

if __name__ == "__main__":
    cod2()
    



