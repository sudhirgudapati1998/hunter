contact=dict()
b=0
while b!=6:
    print("press 1-add  2-delete  3-search  4-diplay 5-update 6-quit")
    a=int(input())
    b=a
    if(a==1):
        name=input("enter the contact name")
        contact[name]=input("enter the phone number")
    elif(a==2):
        name=input("enter the contact name")
        if name in contact:
            contact.pop(name)
        else:
            print("contact name is not present")
    elif(a==3):
        name=input("enter the contact name")
        if name in contact:
            print(contact[name])
        else:
            print("contact name is not present")
    elif(a==4):
        print(contact)
    elif(a==5):
        name=input("enter the contact name")
        if name in contact:
            number=input('enter the phone number')
            contact[name]=number
        else:
            print("contact name is not present')
        
