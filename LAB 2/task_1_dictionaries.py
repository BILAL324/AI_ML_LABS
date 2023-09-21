student_dict = {
    "FA20BCE010": {"name": "Muhammad Bilal", "email": "bilal@gmail.com", "gender": "male"},
    "FA20BCE020": {"name": "Abdullah", "email": "abdullah@gmail.com", "gender": "male"}
}

def create_record():
    
    key = input("Enter Id: ")
    name = input("Enter Name: ")
    email = input("Enter Email: ")
    gender = input("Enter Gender: ")

    student_dict[key] = {
        "name": name,
        "email": email,
        "gender": gender
    }
    print("Data is Entered Successfully.")

#create_record()
print("Updated Student Dictionary:")
print(student_dict)


def delete_record():
    
    key = input("Enter the Registration Number to delete record:")
    if key in student_dict:
        del student_dict[key]
        print("record Deleted")
        
    else:
       print("no record found")
    

print(student_dict)





def update_record():
    key = input("Enter the Registration Number to update record: ")
    if key in student_dict:
        name = input("Enter updated Name: ")
        email = input("Enter updated Email: ")
        gender = input("Enter updated Gender: ")
        
        student_dict[key]["name"] = name
        student_dict[key]["email"] = email
        student_dict[key]["gender"] = gender
        print("Record  updated successfully.")
    else:
        print("No record found with registration number")
        
  
        
  
    
def manage_records():
    while True:
        print("\nOptions:")
        print("1. Create a record")
        print("2. Delete a record")
        print("3. Update a record")
        print("4. Exit")
        
        choice = input("Enter your choice (1-4): ")
        
        if choice == '1':
            create_record()
        elif choice == '2':
            delete_record()
        elif choice == '3':
            update_record()
        elif choice == '4':
            break
        else:
            print("Invalid choice. Please try again.")
        
        
        

