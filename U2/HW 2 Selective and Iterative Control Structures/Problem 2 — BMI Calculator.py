#Problem 2:
def calculate_grades():
    grades= []
    print("Enter student grades one by one. Type 'done' when finished.")
    while True:
        user_input = input("Enter grade (or 'done'): ").strip().lower() 
        if user_input == 'done':
            break     
        try:
         grade = float(user_input)
         grades.append(grade)
        except ValueError:
            print("Invalid input. Please enter a valid number or 'done'.")
    if not grades:
        print("No grades entered. Please enter at least one grade.")
        return
    average = sum(grades) / len(grades)
    status = "Passed" if average >= 7.0 else "Failed"
    print(f"Average: {average:.2f} — {status}")
calculate_grades()
