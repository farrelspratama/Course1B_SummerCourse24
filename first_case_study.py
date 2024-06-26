def main():
    total_miles = 0.0
    total_gallons = 0.0
    
    while True:
        gallons = float(input("Enter the gallons used (-1 to end): "))
        if gallons == -1:
            break
        miles = float(input("Enter the miles driven: "))
        
        miles_per_gallon = miles / gallons
        print(f"The miles/gallon for this tank was {miles_per_gallon:.6f}")
        
        total_miles += miles
        total_gallons += gallons
    
    if total_gallons != 0:
        overall_miles_per_gallon = total_miles / total_gallons
        print(f"The overall average miles/gallon was {overall_miles_per_gallon:.6f}")
    else:
        print("No data to calculate overall miles per gallon.")

main()