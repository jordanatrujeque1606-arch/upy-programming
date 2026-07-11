def season_classifier():
    print("Season Classifier — Enter month numbers (1-12). Type 'exit' to stop.")
    
    while True:
        user_input = input("\nEnter month number (or type 'exit'): ").strip().lower()
        
        if user_input == 'exit':
            print("Exiting program.")
            break
            
        try:
            month = int(user_input)
            
           
            if month < 1 or month > 12:
                print("Invalid month. Please enter a number between 1 and 12.")
                continue
                
           
            if month in [12, 1, 2]:
                season = "Winter"
            elif month in [3, 4, 5]:
                season = "Spring"
            elif month in [6, 7, 8]:
                season = "Summer"
            else:
                season = "Fall"
                
            print(season)
            
        except ValueError:
            print("Invalid input. Please enter a valid number or 'exit'.")
season_classifier()