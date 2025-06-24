# Create a function that accepts any number of arguments and returns their average.
def average(*numbers):
    if len(numbers) == 0:
        return 0 
    return sum(numbers) / len(numbers)
print("Average:", average(10, 20, 30))         
print("Average:", average(5, 15))              
print("Average:", average())                  
print("Average:", average(1, 2, 3, 4, 5, 6))    
