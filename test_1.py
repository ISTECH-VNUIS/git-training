def split_name():
    # Get full name from user
    full_name = input("Please enter your full name: ").strip()
    
    # Split the name into parts
    name_parts = full_name.split()
    
    # Initialize variables
    first_name = ""
    middle_name = ""
    last_name = ""
    
    # Assign parts based on length
    if len(name_parts) >= 1:
        first_name = name_parts[0]
    if len(name_parts) >= 2:
        last_name = name_parts[-1]
    if len(name_parts) >= 3:
        middle_name = " ".join(name_parts[1:-1])
    
    # Print results
    print("\nName Details:")
    print(f"First Name: {first_name}")
    print(f"Middle Name: {middle_name}")
    print(f"Last Name: {last_name}")

# Run the function
split_name()
print("Test 1 complete.")