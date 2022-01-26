sList=[]
def add(vall):
    # = input("Enter value: ")
    if vall in sList:
        print("Duplicate found")
    else:
        sList.append(vall)
        print("Value added")
    print(sList)

                
add(1) 
add(2)
add(3)
add(4) 
add(2)

