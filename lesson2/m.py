# m.py
def m():
    mySum = 0
    myProduct = 1
    myDifference = 0
    myQuotient = -0.1
    print(" ")
#    print "%s, %s, %s, %s," % (mySum, myProduct, myDifference, myQuotient,)
    for i in range(1, 13, 2):
        mySum += i
        myProduct *= i
        myDifference -= i
        myQuotient /= i
        if myProduct == 1:
            print(str(myProduct) + " this was the if for myProduct")
            if mySum == 1:
                print(str(mySum) + " this was the if for mySum")
                if myDifference == -1:
                    print(str(myDifference) + " this was the if for myDifference")
                    if myQuotient == -0.1:
                        print(str(myQuotient) + " this was the if for myQuotient"), print(" ")
        elif myProduct == 3:
            print(str(myProduct) + " this was the 2nd if for myProduct")
            if mySum == 4:
                print(str(mySum) + " this was the 2nd if for mySum")
                if myDifference == -4:
                    print(str(myDifference) + " this was the 2nd if for myDifference")
                    if myQuotient == -0.03333333333333333:
                        print(str(myQuotient) + " this was the 2nd if for myQuotient"), print(" ")
        elif myProduct == 15:
            print(str(myProduct) + " this was the 3rd if for myProduct")
            if mySum == 9:
                print(str(mySum) + " this was the 3rd if for mySum")
                if myDifference == -9:
                    print(str(myDifference) + " this was the 3rd if for myDifference")
                    if myQuotient == -0.006666666666666666:
                        print(str(myQuotient) + " this was the 3rd if for myQuotient"), print(" ")
        elif myProduct == 105:
            print(str(myProduct) + " this was the 4th if for myProduct")
            if mySum == 16:
                print(str(mySum) + " this was the 4th if for mySum")
                if myDifference == -16:
                    print(str(myDifference) + " this was the 4th if for myDifference")
                    if myQuotient == -0.0009523809523809523:
                        print(str(myQuotient) + " this was the 4th if for myQuotient"), print(" ")
        elif myProduct == 945:
            print(str(myProduct) + " this was the 5th if for myProduct")
            if mySum == 25:
                print(str(mySum) + " this was the 5th if for mySum")
                if myDifference == -25:
                    print(str(myDifference) + " this was the 5th if for myDifference")
                    if myQuotient == -0.00010582010582010581:
                        print(str(myQuotient) + " this was the 5th if for myQuotient"), print(" ")
        else:
            print("blimey got it wrong, Josh")
            break
#        print(myProduct, mySum, myDifference, myQuotient)
m()