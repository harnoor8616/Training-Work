# Take a string input and split it by commas and join them using semicolons.
user_input = input("Enter comma-separated values: ")
split_list = user_input.split(',')
joined_string = ';'.join(split_list)
print("Result:", joined_string)
