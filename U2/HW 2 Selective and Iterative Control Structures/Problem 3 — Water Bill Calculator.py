def water_bill_calculator():
    print("Water Bill Calculator — Enter monthly consumption. Type 'exit' to stop.")
    
    total_accumulated_charge = 0.0
    
    while True:
        user_input = input("\nEnter m³ consumed (or type 'exit'): ").strip().lower()
        
        if user_input == 'exit':
            break
            
        try:
            m3 = float(user_input)
            
            if m3 < 0:
                print("Consumption cannot be negative.")
                continue
                
           
            if m3 <= 10:
                rate = 8.00
            elif m3 <= 20:
                rate = 12.00
            else:
                rate = 18.00
                
           
            month_charge = m3 * rate
            total_accumulated_charge += month_charge
            
            print(f"Month charge: ${month_charge:.2f} MXN")
            
        except ValueError:
            print("Invalid input. Please enter a valid number or 'exit'.")

    print(f"Total: ${total_accumulated_charge:.2f} MXN")
water_bill_calculator()