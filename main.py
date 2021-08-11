# A Letter
def LetterA ():
    for i in range(8):
        for j in range(6):
            if ((j == 0 or j == 5) and i != 0) or ((i == 0 or i ==4)):
                print("*", end="")

            else:
                print(end=" ")
        print("")


LetterA()



