def pos_nos(a, b, c):
    positive_count = 0 #this is the initial pos count which is declared as 0
    
    # checks if the input number is positive (>0) and then add it to the positive count
    if a > 0:
        positive_count += 1
    if b > 0:
        positive_count += 1
    if c > 0:
        positive_count += 1
        
    return positive_count == 2 #returns tru only for two positive inputs, else returns false

try:
    a, b, c = map(int, input("Enter the numbers (a, b, c): ").split(","))
    
    answer = pos_nos(a, b, c)
    
    print(answer)
    
except ValueError: #exception to handle any runtime error incurred 
    print("Invalid input. Please enter three integers separated by commas.")
