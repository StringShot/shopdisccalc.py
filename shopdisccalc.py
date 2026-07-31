valid = False
 
while not valid:
    try:
        billamount, discountpercent, people = input("Enter bill amount, discount percent, and people separated by commas: ").split(",")
 
        billamount = float(billamount)
        discountpercent = float(discountpercent)
        people = int(people)
 
        if billamount <= 0 or discountpercent < 0 or people < 0:
            raise ValueError
 
        discountamount = billamount * discountpercent / 100
        finalamount = billamount - discountamount
 
        amountperperson = finalamount / people
 
    except ValueError:
        print("Invalid input! Enter values like this: 1000, 10, 2")
 
    except ZeroDivisionError:
        print("People cannot be 0. Please enter at least 1 person.")
 
    else:
        print("Shopping Summary")
        print("Original Bill:", billamount)
        print("Discount Percent:", discountpercent)
        print("Discount Amount:", discountamount)
        print("Final Amount:", finalamount)
        print("Amount Per Person:", round(amountperperson, 2))
        valid = True
 
    finally:
        print("The discount check has been completed.")
