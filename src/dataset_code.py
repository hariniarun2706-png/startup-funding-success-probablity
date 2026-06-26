import pandas as pd
import random

# Define possible industries and cities
industries = ["AI", "FinTech", "HealthTech", "EdTech", "E-Commerce", "AgriTech", "CleanTech"]
cities = ["Bangalore", "Mumbai", "Delhi", "Chennai", "Hyderabad", "Pune", "Kolkata"]

# Generate synthetic data
data = []
for i in range(1, 5000):  # 120 startups
    team_size = random.randint(2, 20)
    founder_experience = random.randint(0, 15)  # years
    startup_age = random.randint(1, 10)  # years
    industry = random.choice(industries)
    city = random.choice(cities)
    funding_goal = random.randint(50000, 2000000)
    funding_raised = random.randint(20000, 2500000)
    funding_success = "Yes" if funding_raised >= funding_goal else "No"
    
    data.append([i, team_size, founder_experience, startup_age, industry, city,
                 funding_goal, funding_raised, funding_success])

# Create DataFrame
df = pd.DataFrame(data, columns=[
    "Startup_ID", "Team_Size", "Founder_Experience_Years", "Startup_Age_Years",
    "Industry", "City", "Funding_Goal", "Funding_Raised", "Funding_Success"
])

# Save to CSV
df.to_csv("dataset_synthetic.csv", index=False)

print(df.head())
print("Synthetic dataset with", len(df), "rows created!")
