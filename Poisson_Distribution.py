import pandas as pd
from scipy.stats import poisson


file_path = '/content/Road-Accidents-2018-Annexure-19.csv'  # Load the dataset
data = pd.read_csv(file_path)

st=input("Enter the State name : ") # Get input from the user


state_data = data[data['State/UT']== st].iloc[0]  # Selecting data for state name from the user (first row)

# Calculate the mean number of fatal accidents for 2016 and 2017 to use as the average rate (λ)
mean_fatal_accidents = (state_data['Fatal Accidents - 2016'] + state_data['Fatal Accidents - 2017']) / 2

# Display the calculated average rate (λ)
print("=== Poisson Distribution Calculator ===")
print(f"State:{st}")
print(f"Average Number of Fatal Accidents (λ) for 2016 and 2017: {mean_fatal_accidents:.2f}\n")

# Define key k values for which probabilities will be displayed (number of accidents)

k_values = [
    int(mean_fatal_accidents),                # Exactly λ accidents
    int(mean_fatal_accidents) - 1,            # λ - 1 accidents
    int(mean_fatal_accidents) + 1,            # λ + 1 accidents
    int(mean_fatal_accidents // 2),           # Half of λ accidents
    int(mean_fatal_accidents * 2)             # Double λ accidents
]

# Ensure k_values are within a valid range

k_values = [k for k in k_values if k >= 0]

# Calculate and display probabilities using the Poisson distribution

print("=== Probability Results (Poisson Distribution) ===")
for k in k_values:
    prob = poisson.pmf(k, mean_fatal_accidents)
    print(f"P(X = {k}) = {prob:.6f} or {prob*100:.4f}%")

# Calculate cumulative probability up to λ accidents

cumulative_prob = poisson.cdf(int(mean_fatal_accidents), mean_fatal_accidents) 

# Display cumulative probability up to λ accidents

print(f"\nCumulative Probability P(X ≤ {int(mean_fatal_accidents)}) = {cumulative_prob:.6f} or {cumulative_prob*100:.4f}%")
