# Name: Nilesh Gorakh Bhandare
# Registration Number: ME25M026
# Language Used: Python
import numpy as np
import matplotlib.pyplot as plt
def recursive_poly_eval(x, coeffs):
    """
    Implements Task 1 & Requirement: Generate the recursive polynomial[cite: 7, 21].
    P_0 = a_0
    P_i = x * P_{i-1} + a_i
    """
    p = coeffs[0]  # This is a_0 [cite: 6]
    for i in range(1, len(coeffs)):
        p = x * p + coeffs[i]  # Recursive step [cite: 7]
    return p
# Define the set of functions required [cite: 4]
functions = {
    "sin(x)": np.sin,
    "exp(x)": np.exp,
    "cos(x)": np.cos,
    "sinh(x)": np.sinh,
    "cosh(x)": np.cosh,
    "tanh(x)": np.tanh,
    "arcsin(x)": lambda x: np.arcsin(np.clip(x, -1, 1))
}
# Parameters
x_val = np.linspace(-1, 1, 500)
degree = 6  # Degree n for the polynomial sequence
plt.figure(figsize=(25, 20))
# Loop through each function to approximate [cite: 9]
for i, (name, func) in enumerate(functions.items(), 1):
    y_true = func(x_val)
    # Task 2: Determine coefficients a_i
    # polyfit returns coefficients [a_0, a_1, ... a_n] for the recursive form
    coeffs = np.polyfit(x_val, y_true, degree)
    # Task 22: Perform the approximation
    y_approx = recursive_poly_eval(x_val, coeffs)
    # Task 4: Compute Mean Square Error
    mse = np.mean((y_true - y_approx)**2)
    print(f"Function: {name:8} | MSE: {mse:.2e}")
    # Task 3 & 23: Plotting [cite: 11, 23]
    plt.subplot(3, 3, i)
    plt.plot(x_val, y_true, 'b-', label='Original', linewidth=2)
    plt.plot(x_val, y_approx, 'r--', label='Approx')
    plt.title(f"{name}\nMSE: {mse:.2e}")
    plt.legend()
    plt.grid(True)
plt.tight_layout()
plt.show()
