import pandas as pd
import numpy as np
import random


# List of the 27 European Union countries
euCountries = [
    'Austria', 'Belgium', 'Bulgaria', 'Croatia', 'Cyprus', 'Czechia', 'Denmark',
    'Estonia', 'Finland', 'France', 'Germany', 'Greece', 'Hungary', 'Ireland', 'Italy', 'Latvia',
    'Lithuania', 'Luxembourg', 'Malta', 'Netherlands', 'Poland', 'Portugal', 'Romania', 'Slovakia',
    'Slovenia', 'Spain', 'Sweden'
]


# Percentage of individuals using the internet for internet banking by country (data from eurostat: https://ec.europa.eu/eurostat/databrowser/view/tin00099/default/table?lang=en)
# Using the most recent data of 2023

internetBankingUsage = {
    'Austria': 77.17,
    'Belgium': 79.6,
    'Bulgaria': 23.43,
    'Croatia': 61.88,
    'Cyprus': 70.86,
    'Czechia': 79.84,
    'Denmark': 96.22,
    'Estonia': 84.89,
    'Finland': 94.48,
    'France': 72.41,
    'Germany': 57.22,
    'Greece': 52.01,
    'Hungary': 65.52,
    'Ireland': 84.85,
    'Italy': 51.55,
    'Latvia': 83.74,
    'Lithuania': 75.73,
    'Luxembourg': 71.14,
    'Malta': 67.38,
    'Netherlands': 95.13,
    'Poland': 59.09,
    'Portugal': 58.88,
    'Romania': 21.89,
    'Slovakia': 57.72,
    'Slovenia': 60.69,
    'Spain': 71.45,
    'Sweden': 84.49
}


# Percentage of population by education level by country
# Using the most recent data of 2022  (data from eurostat: https://ec.europa.eu/eurostat/databrowser/view/edat_lfs_9903/default/table?lang=en)

educationData = {
    'Austria': {'Lower secondary': 18.6, 'Upper secondary': 48.9, 'Tertiary': 32.5},
    'Belgium': {'Lower secondary': 21.7, 'Upper secondary': 38.1, 'Tertiary': 40.2},
    'Bulgaria': {'Lower secondary': 20.0, 'Upper secondary': 54.0, 'Tertiary': 26.0},
    'Croatia': {'Lower secondary': 16.1, 'Upper secondary': 61.7, 'Tertiary': 22.2},
    'Cyprus': {'Lower secondary': 18.9, 'Upper secondary': 37.8, 'Tertiary': 43.3},
    'Czechia': {'Lower secondary': 12.3, 'Upper secondary': 64.2, 'Tertiary': 23.5},
    'Denmark': {'Lower secondary': 25.8, 'Upper secondary': 39.2, 'Tertiary': 35.0},
    'Estonia': {'Lower secondary': 16.9, 'Upper secondary': 46.4, 'Tertiary': 36.7},
    'Finland': {'Lower secondary': 18.1, 'Upper secondary': 46.0, 'Tertiary': 35.9},
    'France': {'Lower secondary': 21.3, 'Upper secondary': 41.8, 'Tertiary': 36.9},
    'Germany': {'Lower secondary': 23.0, 'Upper secondary': 48.8, 'Tertiary': 28.2},
    'Greece': {'Lower secondary': 22.7, 'Upper secondary': 46.8, 'Tertiary': 30.5},
    'Hungary': {'Lower secondary': 18.7, 'Upper secondary': 55.8, 'Tertiary': 25.5},
    'Ireland': {'Lower secondary': 17.5, 'Upper secondary': 36.7, 'Tertiary': 45.8},
    'Italy': {'Lower secondary': 38.8, 'Upper secondary': 43.1, 'Tertiary': 18.1},
    'Latvia': {'Lower secondary': 14.9, 'Upper secondary': 50.6, 'Tertiary': 34.5},
    'Lithuania': {'Lower secondary': 11.3, 'Upper secondary': 47.4, 'Tertiary': 41.3},
    'Luxembourg': {'Lower secondary': 24.2, 'Upper secondary': 29.8, 'Tertiary': 46.0},
    'Malta': {'Lower secondary': 33.1, 'Upper secondary': 38.0, 'Tertiary': 28.9},
    'Netherlands': {'Lower secondary': 23.0, 'Upper secondary': 38.2, 'Tertiary': 38.8},
    'Poland': {'Lower secondary': 12.9, 'Upper secondary': 57.5, 'Tertiary': 29.6},
    'Portugal': {'Lower secondary': 39.6, 'Upper secondary': 31.8, 'Tertiary': 28.6},
    'Romania': {'Lower secondary': 20.7, 'Upper secondary': 62.2, 'Tertiary': 17.1},
    'Slovakia': {'Lower secondary': 12.8, 'Upper secondary': 61.2, 'Tertiary': 26.0},
    'Slovenia': {'Lower secondary': 13.8, 'Upper secondary': 51.1, 'Tertiary': 35.1},
    'Spain': {'Lower secondary': 37.7, 'Upper secondary': 25.5, 'Tertiary': 36.8},
    'Sweden': {'Lower secondary': 19.5, 'Upper secondary': 39.4, 'Tertiary': 41.1}
}


# Median net income of the EU 27 countries by educational attainment level
# Using the most recent data of 2022 (data from eurostat: https://ec.europa.eu/eurostat/databrowser/view/ilc_di08/default/table?lang=en)

educationIncome = {
    'Austria': {'Lower secondary': 21587, 'Upper secondary': 28829, 'Tertiary': 33620},
    'Belgium': {'Lower secondary': 20241, 'Upper secondary': 27119, 'Tertiary': 34003},
    'Bulgaria': {'Lower secondary': 3046, 'Upper secondary': 6004, 'Tertiary': 9248},
    'Croatia': {'Lower secondary': 6610, 'Upper secondary': 9246, 'Tertiary': 12610},
    'Cyprus': {'Lower secondary': 13641, 'Upper secondary': 17155, 'Tertiary': 22965},
    'Czechia': {'Lower secondary': 10889, 'Upper secondary': 12922, 'Tertiary': 16560},
    'Denmark': {'Lower secondary': 30407, 'Upper secondary': 34546, 'Tertiary': 38619},
    'Estonia': {'Lower secondary': 12146, 'Upper secondary': 15057, 'Tertiary': 19754},
    'Finland': {'Lower secondary': 24316, 'Upper secondary': 26320, 'Tertiary': 33794},
    'France': {'Lower secondary': 18170, 'Upper secondary': 22453, 'Tertiary': 30231},
    'Germany': {'Lower secondary': 20272, 'Upper secondary': 25987, 'Tertiary': 34334},
    'Greece': {'Lower secondary': 7300, 'Upper secondary': 9339, 'Tertiary': 12496},
    'Hungary': {'Lower secondary': 5446, 'Upper secondary': 7059, 'Tertiary': 9150},
    'Ireland': {'Lower secondary': 22041, 'Upper secondary': 28989, 'Tertiary': 36195},
    'Italy': {'Lower secondary': 15252, 'Upper secondary': 19509, 'Tertiary': 24770},
    'Latvia': {'Lower secondary': 7654, 'Upper secondary': 9992, 'Tertiary': 14852},
    'Lithuania': {'Lower secondary': 8226, 'Upper secondary': 9761, 'Tertiary': 14869},
    'Luxembourg': {'Lower secondary': 34043, 'Upper secondary': 41936, 'Tertiary': 55526},
    'Malta': {'Lower secondary': 15633, 'Upper secondary': 20523, 'Tertiary': 28323},
    'Netherlands': {'Lower secondary': 26394, 'Upper secondary': 29517, 'Tertiary': 35007},
    'Poland': {'Lower secondary': 7230, 'Upper secondary': 8611, 'Tertiary': 11782},
    'Portugal': {'Lower secondary': 9333, 'Upper secondary': 11123, 'Tertiary': 15704},
    'Romania': {'Lower secondary': 3269, 'Upper secondary': 5670, 'Tertiary': 9591},
    'Slovakia': {'Lower secondary': 5615, 'Upper secondary': 9171, 'Tertiary': 10431},
    'Slovenia': {'Lower secondary': 13648, 'Upper secondary': 16287, 'Tertiary': 20326},
    'Spain': {'Lower secondary': 13556, 'Upper secondary': 16320, 'Tertiary': 22300},
    'Sweden': {'Lower secondary': 21566, 'Upper secondary': 29342, 'Tertiary': 32875}
}




# Adjusted weights for age groups based on their impact on income  (data from eurostat : https://ec.europa.eu/eurostat/databrowser/view/ilc_di03$defaultview/default/table?lang=en)
# Code for calculating age weights is at: Weights Code - Impact of age on income.py
# Using the median net income of the EU 27 countries for 2022, for 18-24, 25-49, 50-64, 65+ age groups
ageWeights = [23.37, 26.05, 27.87, 22.71]





# Function for income generator
def calculateIncome(country, age, educationLevel):
    global educationIncome, ageWeights
    
    # Get the median income for the specified education level and country
    medianIncome = educationIncome.get(country, {}).get(educationLevel, None)
    
    if medianIncome is None:
        # Handle the case where the median income data is not available
        raise ValueError(f"Median income data not available for {country}, {educationLevel}")
    
    # Calculate the age factor based on the age group weights with limited randomness
    if age < 25:
        ageFactor = ageWeights[0] * np.random.uniform(0.9, 1.1)  # Adding controlled randomness for 18-24 age group
    elif 25 <= age < 50:
        ageFactor = ageWeights[1] * np.random.uniform(0.9, 1.1)  # Adding controlled randomness for 25-49 age group
    elif 50 <= age < 65:
        ageFactor = ageWeights[2] * np.random.uniform(0.9, 1.1)  # Adding controlled randomness for 50-64 age group
    else:
        ageFactor = ageWeights[3] * np.random.uniform(0.9, 1.1)  # Adding controlled randomness for 65+ age group
    
    # Adding controlled randomness on income based on education level and their respective values
    educationFactor = 1.0
    if educationLevel == 'Lower secondary':
        educationFactor = np.random.uniform(0.7, 1.0)           # Adding controlled randomness for lower secondary education
    elif educationLevel == 'Upper secondary':
        educationFactor = np.random.uniform(0.7, 1.0)           # Adding controlled randomness for upper secondary education
    else:
        educationFactor = np.random.uniform(0.7, 0.9)           # Adding controlled randomness for tertiary education with a narrower range
    
    # Calculate the final income based on factors and values
    incomeAdjustment = medianIncome * (1 + ageFactor / 100) * educationFactor
    
    # Ensure income doesn't become negative
    income = max(0, incomeAdjustment)
    
    return int(income)




# Generate random education level based on the distribution in educationData dictionary
def generateRandomEducationLevel(country):
    eduLevels = list(educationData[country].keys())
    percentages = list(educationData[country].values())

    return random.choices(eduLevels, weights=percentages)[0]

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


    return syntheticData


# Generate x number of synthetic records
syntheticDataset = generateSyntheticData(5000)

# Convert the synthetic dataset to a DataFrame
df = pd.DataFrame(syntheticDataset)


# Export DataFrame to Excel
df.to_excel('projectDataset.xlsx', index=False)
