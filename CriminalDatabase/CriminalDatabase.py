
val = 1
while val:
    addharNumber = input('Add another Criminal or Check for Criminal History enter criminal IDs: ')

    if len(addharNumber) == 12:
        with open('Database.txt','r') as p:
            data = p.read()
            
            if str(addharNumber) in data:
                print('\n')
                print("🚨🚨🚨 Person has already facing criminal charges...")
                print('\n')
                choise = int(input(f'Press 1 show every criminal charges on {addharNumber}... \nPress 2 for add additional charges about {addharNumber} to database... \nPress 3 for exit... '))
                if choise == 1:
                    with open (f'Criminal ID  {addharNumber}.txt','r') as p:
                        data = p.read()
                        print('\n')
                        print(data)
                elif choise == 2:
                    with open (f'Criminal ID  {addharNumber}.txt','a') as p:
                        n = int(input('Enter number of charges u wanna add: '))
                        for i in range(n):
                            charges = input("Enter the criminal charge: ")
                            charges = charges.upper()
                            p.write(f'Criminal charge: {charges}')
                            p.write('\n')
                elif choise == 3:
                    exit()
                else:
                    pass
            else:
                print("No Criminal Record Found...")
                print("\n")
                c = int (input(' Press 0 for exit: \n Press 1-9 for add charges:'))
                if c == 0 :
                    exit()
                else:
                    name = input('Enter the name of the criminal: ')
                    dob = input('Enter the date of birth of the criminal: ')
                    fname = input("Enter the father's name of the criminal: ")
                    mname = input("Enter the mother's name of the criminal: ")
                    hno = input("Enter the house number: ")
                    address = input('Enter the address of the criminal: ')
                    pin = input("Enter the pin code of the address: ")
                    name = name.upper()
                    fname = fname.upper()
                    mname = mname.upper()
                    address = address.upper()
                    
                    address = hno+' '+address + ' ' + pin
                    with open('Database.txt','a') as p:
                        p.write(f"Criminal ID: {str(addharNumber)}")
                        p.write('\n')
                    with open (f'Criminal ID  {addharNumber}.txt','a') as  p:
                        p.write(f'Name: {name.upper()}\nAddhar Number: {addharNumber}\nDate of Birth: {dob}\nFather Name: {fname}\nMother Name: {mname}\nAddress: {address}\n')
                        n = int(input('Enter number of charges u wanna add: '))
                        for i in range(n):
                            charges = input("🚨Enter the criminal charge: ")
                            charges = charges.upper()
                            p.write(f'Criminal charge: {charges}')
                            p.write('\n')
    else:
        print('Invalid Criminal ID...')
        print()
        
    
    val = int(input('Press 0 for Exit & 1 for continue...'))
    print()