#PiApproximation



"""In this program we will approximate pi based on a number of terms the user inputs"""

pi = 3.14159265358979
terms = 0
pi_approx = 0

print("We are finding the minimum number of terms needed to get an approximation of pi accurate within our error tolerance.")


input_error = float(input("Input error tolerance:"))

print("Number of Terms \t\t\t Pi Approximation")

while abs(pi_approx - pi) > input_error:
    terms += 1
    
    pi_end = (4 * ((-1)**(terms + 1))) / ((2 * terms) - 1)
    
    pi_approx += pi_end

    print(f"{terms} \t\t\t {pi_approx}")

print(f"After {terms} terms, pi is appproximately {pi_approx}.")

print(f"Our error is {abs(pi_approx - pi): .6f} which is less than or equal to {input_error: .6f}")
