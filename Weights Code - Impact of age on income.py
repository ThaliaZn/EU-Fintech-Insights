# Median equivalised net income of the EU 27 countries for 2022, for 4 age groups: 18-24, 25-49, 50-64, 65+
# Data from eurostat: https://ec.europa.eu/eurostat/databrowser/view/ilc_di03/default/table?lang=en
ageGroups = ['18-24', '25-49', '50-64', '65+']
medianIncomes = [17845, 19888, 21282, 17342]

# Calculate total income across all age groups
totalIncome = sum(medianIncomes)

# Calculate percentages for each age group's contribution to total income
ageWeightsFromIncome = [round((income / totalIncome) * 100, 2) for income in medianIncomes]

# Display the calculated age weights based on income distributions
print("Estimated age weights based on income distributions:")
for i, age_group in enumerate(ageGroups):
    print(f"{age_group}: {ageWeightsFromIncome[i]}%")
