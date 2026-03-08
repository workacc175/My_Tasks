import matplotlib.pyplot as plt

# 1. Define the data
days = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
temperatures = [22, 24, 21, 25, 28, 26, 23] # Example data in Celsius

# 2. Create the line plot
plt.plot(days, temperatures, marker='o', linestyle='-', color='b')

# 3. Add labels and title
plt.xlabel('Days of the Week')
plt.ylabel('Temperature (°C)')
plt.title('Temperature Variation Over a Week')

# 4. Display the plot
plt.grid(True) # Adds a grid for better readability
plt.show()
