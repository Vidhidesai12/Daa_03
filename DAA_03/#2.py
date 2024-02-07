import numpy as np
import matplotlib.pyplot as plt
import time

def f(n):
    x = 1
    y=1
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            x = x + 1
            y=i+j
    return x

values_of_n = np.arange(1, 1001,10)  # Values of n from 1 to 100
runtime = np.zeros(len(values_of_n))

for idx, n in enumerate(values_of_n):
    starting_time = time.time()  # Start timing
    result = f(n)  # Call the function
    ending_time = time.time()  # Stop timing
    runtime[idx] = ending_time - starting_time  # Record elapsed time

# Fit a polynomial curve (quadratic) to the data
coefficient = np.polyfit(values_of_n, runtime, 2)
fitting_curve = np.polyval(coefficient, values_of_n)

# Calculate upper and lower bounds based on the leading term of the fitted polynomial
up_bound = 1.1 * np.polyval(coefficient, values_of_n)  # Adjust the constant factor as needed
low_bound = 0.9 * np.polyval(coefficient, values_of_n)  # Adjust the constant factor as needed



# Plotting time vs n with different colors for curves
plt.figure()
plt.plot(values_of_n, runtime, 'o-',linewidth=2, label='Actual Data')
plt.plot(values_of_n, fitting_curve,  linewidth=2, label='Polynomial Fit')
plt.plot(values_of_n, up_bound,  linewidth=2, label='Upper Bound (O(n^2))', color='green')
plt.plot(values_of_n, low_bound,  linewidth=2, label='Lower Bound (Ω(n^2))', color='purple')
n_0=90
plt.scatter(n_0, np.polyval(coefficient, n_0), s=50, c='red', marker='s', label=r'n_0')
plt.text(n_0, np.polyval(coefficient, n_0), r'n_0', ha='right', va='bottom')
plt.xlabel('n')
plt.ylabel('Time (seconds)')
plt.title('Runtime vs n')
plt.legend()

# Display the coefficients of the fitted polynomial (for reference)
print("Coefficients of the fitted polynomial:", coefficient)

plt.show()