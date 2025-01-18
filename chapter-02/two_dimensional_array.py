# Define the two-dimensional array of months
months = [
    ['January', 'February', 'March', 'April'],
    ['May', 'June', 'July', 'August'],
    ['September', 'October', 'November', 'December']
]

# Use a double loop to output the months
for row in months:       # Outer loop iterates over each row in the array
    for month in row:    # Inner loop iterates over each month in the row
        print(month)     # Print each month on a new line