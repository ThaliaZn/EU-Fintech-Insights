""" 
DEBUGGING SECTION: Replace the last section of the main code "Synthetic Dataset Generator Fintech EU.py" (from line 176) with the following version.
This will provide insights into how weights (lines 195-225) impact internet usage values.
Experiment with different weight values and observe their effects on the output in your terminal.
"""

# Function to generate synthetic dataset
def generateSyntheticData(numRecords):
    syntheticData = []
    for _ in range(numRecords):
        # Generate random person details
        country = random.choice(euCountries)
        age = random.randint(18, 80)
        educationLevel = generateRandomEducationLevel(country)

        # Calculate base internet usage for banking based on country
        baseInternetUsage = internetBankingUsage[country]

        # Adjustments of internet usage for banking based on age and education
        ageAdjustment = 0
        educationAdjustment = 0

        # Age group adjustment (weights try to approximate the average from eurostat's data: https://ec.europa.eu/eurostat/databrowser/view/isoc_ci_ac_i/default/table?lang=en)
        # Data: Individuals - internet activities (banking), EU total: 63.87%, below 25: 61.46%, 25-50: 73.23%, 50-65: 57.51%, above 65:41.52%
        if age < 25:
            ageAdjustment = -random.uniform(5.0, 8.0)
            if educationLevel == 'Lower secondary':
                educationAdjustment = -random.uniform(4.0, 6.0)
            elif educationLevel == 'Upper secondary':
                educationAdjustment = random.uniform(0.5, 1.5)
            elif educationLevel == 'Tertiary':
                educationAdjustment = random.uniform(1.0, 3.0)
        elif 25 <= age < 50:
            ageAdjustment = random.uniform(2.5, 5.0)
            if educationLevel == 'Lower secondary':
                educationAdjustment = -random.uniform(4.0, 6.0)
            elif educationLevel == 'Upper secondary':
                educationAdjustment = random.uniform(0.5, 1.5)
            elif educationLevel == 'Tertiary':
                educationAdjustment = random.uniform(2.0, 4.0)
        elif 50 <= age < 65:
            ageAdjustment = -random.uniform(7.0, 9.0)
            if educationLevel == 'Lower secondary':
                educationAdjustment = -random.uniform(4.0, 6.0)
            elif educationLevel == 'Upper secondary':
                educationAdjustment = random.uniform(0.5, 1.5)
            elif educationLevel == 'Tertiary':
                educationAdjustment = random.uniform(1.0, 4.0)
        else:
            ageAdjustment = -random.uniform(10.0, 25.0)
            if educationLevel == 'Lower secondary':
                educationAdjustment = -random.uniform(4.0, 6.0)
            elif educationLevel == 'Upper secondary':
                educationAdjustment = random.uniform(0.5, 1.5)
            elif educationLevel == 'Tertiary':
                educationAdjustment = random.uniform(1.0, 4.0)

        # Apply adjustments to internet usage
        internetUsage = baseInternetUsage + ageAdjustment + educationAdjustment

        # Cap the internet usage at 100% and set a minimum of 0%
        internetUsage = max(0, min(100, internetUsage))

        # Round the internet usage to integers
        internetUsage = round(internetUsage)

        
        income = calculateIncome(country, age, educationLevel)
        
        # Rename education levels to improve readability
        if educationLevel == 'Lower secondary':
            educationLevel = 'Basic'
        elif educationLevel == 'Upper secondary':
            educationLevel = 'Advanced'
        elif educationLevel == 'Tertiary':
            educationLevel = 'Higher'

        # Append generated data to the synthetic dataset
        syntheticData.append({
            'Country': country,
            'Income': income,
            'Age': age,
            'Education Level': educationLevel,
            'Internet Usage for Banking (%)': internetUsage
        })

    # Debugging: Print out information
    print(f"Age: {age}, Education Level: {educationLevel}")
    print(f"Original Internet Usage: {internetBankingUsage[country]}")
    print(f"Age Adjustment: {ageAdjustment}, Education Adjustment: {educationAdjustment}")
    print(f"Final Internet Usage: {internetUsage}")
    

    return syntheticData


# Generate x number of synthetic records
syntheticDataset = generateSyntheticData(5000)

# Convert the synthetic dataset to a DataFrame
df = pd.DataFrame(syntheticDataset)

# Calculate and print the average internet usage for different age groups
average_usage_under_25 = df[df['Age'] < 25]['Internet Usage for Banking (%)'].mean()
average_usage_25_50 = df[(df['Age'] >= 25) & (df['Age'] < 50)]['Internet Usage for Banking (%)'].mean()
average_usage_50_65 = df[(df['Age'] >= 50) & (df['Age'] < 65)]['Internet Usage for Banking (%)'].mean()
average_usage_over_65 = df[df['Age'] >= 65]['Internet Usage for Banking (%)'].mean()

print(f"Average Internet Usage for people under 25: {average_usage_under_25}")
print(f"Average Internet Usage for people 25-50: {average_usage_25_50}")
print(f"Average Internet Usage for people 50-65: {average_usage_50_65}")
print(f"Average Internet Usage for people over 65: {average_usage_over_65}")
