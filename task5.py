TASK-5
contact={ }
print("1.add contact")
print(" 2.To view contact list")
print("3.search contact")
print("4.update contact")
print("5.Delete contact")
def display():
    print("name\t\tcontact_number")
    for key in contact:

     print("{}\t\t{}".format(key,contact.get(key)))

while True:
    choice=int(input("Enter choice-1/2/3/4/5:"))
    if choice==1:
        name=str(input("enter the contact name"))
        contact_number=int(input("enter the contact number"))
        contact[name]=contact_number
    elif (choice==2):
        display()
    elif (choice==3):
        search=str(input("enter the searching name/number"))
        if search in contact:
            print(search,contact_number)
        else:
            print("the name is not present in your contact list!!")
    elif (choice==4):
        edit_contact= input(" enter the contact to be edited")
        if edit_contact in  contact:
         phone=input(" enter the mobile number")
        contact[edit_contact]=phone
        print("contact updated")
        display()
    else:
        print("Name is not found in contact book")
