def cat():
    categories = []
    while True:
        try:
            q = int(input("How many Categories do you have?\n"))
            break
        except:
            print("That is not a valid Answer")


    for i in range (0,q):
        x = input("What is Category {} ?\n".format(i+1))
        categories.append(x)
    with open('categories.txt', 'w') as myFile:
        for i in range(0,len(categories)):
            myFile.write(categories[i] + "\n")
    with open('num.txt', 'w') as y:
        for i in range(0,len(categories)):
            y.write("0\n")
    main()


def start():
    while True:
        temp = input("Do you Have categories already?\n")
        if (temp.lower() == "y" or temp.lower == "yes"):
            main()
        elif(temp.lower() == "n" or temp.lower == "no"):
            cat()
        else:
            print("Please enter y/n")


def main():
    list = ["What would you like to do?", "Edit Categories", "Add a Payment",
            "See Totals", "Exit"]
    while True:
        for i in range(0,len(list)):
            if i > 0:
                print(i,list[i])
            else:
                print(list[i])
            
        try:
            x = int(input(""))
            break
        except:
            print("Invalid Input")
    if (x==1 or x==2):
        reading(x)
    if(x==4):
        exit()
    
        
def reading(PassX):
    with open('categories.txt', 'r') as myFile:
        Lines = myFile.readlines()
        temp = []
        for x in Lines:

            
            x = temp.append(str(x).strip("\n"))

        for x in range(0,len(temp)):
            print(x+1,temp[x])
    if (PassX == 1):
        while True:
            with open('categories.txt', 'w') as myFile:
                x = int(input("Which one would you like to edit?\n"))
                edit = input("What would you like it to be?\n")
                edit += "\n"
                for i in range (0, len(Lines)):
                    if x == i+1:
                        myFile.write(edit)
                    else:
                        myFile.write(Lines[i])
            with open('categories.txt', 'r') as myFile:
                Lines = myFile.readlines()
                print("Here is the new List:")
                for i in range (0, len(Lines)):
                    print(i+1, Lines[i].strip("\n"))
            yOrN(PassX)
    if(PassX==2):
        counting()

            
def yOrN(PassX):
    while True:
        temp = input("Are there any other categories to change?\n")
        if (temp.lower() == "y" or temp.lower == "yes"):
            reading(PassX)
        elif(temp.lower() == "n" or temp.lower == "no"):
            main()
        else:
            print("Please enter y/n")

def counting():
    with open('categories.txt', 'r') as myFile:
        Lines = myFile.readlines()
    with open('num.txt', 'r+') as num:
        numLines = num.readlines()
        if numLines == '':
            with open('num.txt', 'w') as num:
                for i in range (0,len(Lines)):
                    print(Lines[i].strip("\n"))


start()

