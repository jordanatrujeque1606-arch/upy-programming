def shipping_cost_calculator():
    print("Shipping Cost Calculator — Enter package details. Type 'exit' to stop.")
    
    total_accumulated_cost = 0.0
    
    while True:
       
        weight_input = input("\nEnter weight in kg (or type 'exit'): ").strip().lower()
        
        if weight_input == 'exit':
            break
            
        try:
            weight = float(weight_input)
            
           
            distance_input = input("Enter distance in km: ").strip()
            distance = float(distance_input)
            
            if weight <= 0 or distance <= 0:
                print("Weight and distance must be greater than 0.")
                continue
                
            
            if distance <= 100:
                if weight <= 5:
                    cost = 50.00
                else:
                    cost = 80.00
            else:
                if weight <= 5:
                    cost = 120.00
                else:
                    cost = 200.00
                    
           
            total_accumulated_cost += cost
            print(f"Shipping cost: ${cost:.2f} MXN")
            
        except ValueError:
            print("Invalid input. Please enter numbers or type 'exit'.")
            
    
    print(f"Total: ${total_accumulated_cost:.2f} MXN")

shipping_cost_calculator()