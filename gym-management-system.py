members ={}
member_count = 1

while  True:
    print("\n ==== Gym management System ====")
    print("1.' Add Members' \n 2. 'View Members'\n 3. 'Search Member' \n 4.'Delete Member'\n 5.'Exit'")
    
    choice  = input("Enter your choice:")
    
    if choice =="1":
        name = input("Enter member name:")
        age = int(input("Enter age:"))
        plan = input("Enter membership plan:")
        
        member_id = "M"+ str(member_count)
        member_count += 1
        
        members[member_id] ={
            "name": name,
            "age": age,
            "plan": plan
        }
        print("\n Member added successfully!")
        print("Member ID:", member_id)
        
    elif choice =="2":
        if not members:
            print("No members found!")
        else:
            print("\n === Gym Members===")
            for member_id,member in members.items():
                print("\n Member ID:",member_id)
                print("Name:",member["name"])
                print("Age:",member["age"])
                print("Plan:",member["plan"])
        
    elif choice =="3":
        member_id = input("Enter member ID:")
        
        if member_id in members:
            member= members[member_id]
            print("\n === Member Found ===")
            print("Member ID:",member_id)
            print("Name:",member["name"])
            print("Age:",member["age"])
            print("Plan:",member["plan"])
            
        else:
            print("Member not found!")
            
    elif choice =="4":
        member_id = input("Enter member ID to delete:")
        
        if member_id in members:
            del members[member_id]
            print("Member deleted successfully!")
            
        else:
            print("Member not found!")
            
    elif choice =="5":
        print("Thank you for using Gym Management System!")
        break
    
    else:
        print("Invalid choice!")
                    
              