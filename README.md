# EU Fintech Insights



## _Project Overview_

Hey there, curious minds! 
Let's dive into my Internet Usage Analysis Project within the European Union (EU) and uncover the fascinating world of internet habits across EU countries, armed with some stellar data from Eurostat that I've carefully curated and polished.

<b>What’s on the Horizon</b> :
- Our mission: unraveling the fascinating web of internet habits across the EU.
- Eurostat's data is our trusty companion, guiding us through the twists and turns.
- Key demographics like age, income, and education level take center stage.
- We're keeping a close eye on everyone's online antics, especially in the fintech realm.

In this digital journey, you'll meet the <b>Synthetic Data Generator</b>, powered by <b>Python</b>, accompanied by clear visuals crafted with <b>Matplotlib</b> and <b>Seaborn</b>, showing how demographics work. The project is complemented by interactive plots crafted using <b>Power BI</b>, giving you a front-row seat to the insights.

So, get ready for an adventure where data, Python, and Power BI team up to tell a straightforward story about internet usage in the EU. <br><br>


<p align="center">
  <img src= "https://github.com/ThaliaZn/pythonProject/blob/3e998323646773936b7d5b1d46e11b56ed839b69/.idea/Percentage%20of%20Internet%20Usage%20by%20Country.PNG" alt="Project Logo" width="700"/>
</p>


<br><br>

 

## _Data Sources_

**Synthetic Dataset** 

The synthetic dataset is crafted using Python, leveraging the power of random number generation, probability distributions, and controlled randomness with Numpy. This ensures a realistic representation based on EU demographics and fintech adoption probabilities. The Python script behind this process will be shared, allowing you to dive into the mechanics of how we shaped this synthetic landscape. <br><br>


**Real-Life Data**

In parallel, I've gathered real-life insights from Eurostat, a reliable source for European statistical information. The datasets include:

- <b>Individuals using the internet for internet banking</b>: Unveiling the digital banking landscape across the EU.

- <b>Individuals - internet activities</b>: Exploring the various online activities individuals engage in, providing a closer look at internet usage trends. 

- <b>Median income</b>: Offering insights into income distribution across different EU countries.

- <b>Median income by educational attainment level</b>: Highlighting the correlation between education and income.

- <b>Population by educational attainment level</b>: Providing a comprehensive view of the educational landscape within the EU.


Additionally, you'll find a file containing all Eurostat datasets used, cleaned and presented in Excel format. These datasets, extracted from Eurostat, form the foundation of our analysis. They allow for a thorough exploration of internet usage dynamics, considering demographic influencers and the spectrum of online activities.


<br><br>



## _Directory Structure_

- /EurostatDatasets
 
     Cleaned Excel files with real-life data obtained from Eurostat<br><br>


- /Data Visualization - Jupyter.ipynb

   This Jupyter notebook includes visualizations of the generated dataset, aiming to verify its alignment with Eurostat values. It utilizes Matplotlib and Seaborn to present:
   - KDE Plot for Age Distribution
   - Boxplot for Income Distribution by Country
   - Line plot for Average Internet Usage for Banking by Age and Education Level
   - Bar plot to visualize the correlation of 'Internet Usage for Banking (%)' with other variables<br><br>


- /Data Visualization - Python.py

   The Python script equivalent to the Jupyter notebook, containing the same visualizations using Matplotlib and Seaborn. This format provides flexibility for users who prefer to work with Python scripts.<br><br>


- /Debugging - Checking Age-Education Adjustments.py

   Replace the last section of the main code with this version to gain valuable insights in your terminal. This allows you to experiment with various weight values and observe how they influence the Internet Usage values in the dataset.<br><br>


- /Exploring EU Internet Trends - Power BI Visuals.md

  Explore the interactive visualizations created using Power BI, based on the datasets collected. The report is designed to showcase insights about internet usage within the EU.
  Navigate through two informative pages, and don't forget to use the arrows at the bottom for seamless exploration. <br><br>
  

- /Synthetic Dataset Generator Fintech EU.py

   Python code for generating the synthetic dataset mimicking EU demographics and fintech adoption probabilities.<br><br>


- /SyntheticDataset.xlsx

   The synthetic dataset used for Power BI visuals<br><br>


- /Weights Code - Impact of age on income.py

   Python code used to calculate income weights based on age for the synthetic dataset<br><br>


<br><br>


## _Analysis Scripts_

### Synthetic Dataset Generator Fintech EU.py
This Python script generates a synthetic dataset that mimics the demographics and fintech adoption probabilities within the European Union (EU). The dataset is crafted using Eurostat data and introduces controlled randomness to ensure realistic representations.


#### Key Components:

#### 1. EU Country List:
- Defines a list of the 27 European Union countries for reference.

#### 2. Internet Banking Usage:
- Includes the percentage of individuals using the internet for banking in each EU country, sourced from Eurostat.

#### 3. Education Data:
- Provides the percentage distribution of the population by education level in each EU country, based on Eurostat data.

#### 4. Education Income:
- Specifies the median net income in each EU country according to different education levels, using Eurostat data.

#### 5. Age Weights:
- Adjusted weights for age groups based on their impact on income (weights' calculations based on Eurostat data).

#### 6. Functions:
   - `calculateIncome`: Calculates income based on country, age, and education level, incorporating controlled randomness.
   - `generateRandomEducationLevel`: Randomly selects an education level based on the distribution in educationData.
   - `generateSyntheticData`: Generates a synthetic dataset with specified demographic and fintech adoption features.

#### 7. Dataset Generation:
- Utilizes the defined functions to generate a synthetic dataset of 5000 records.
- Controls adjustments for age and education impact on internet usage for banking, maintaining realism.
- Caps internet usage at 100% and sets a minimum of 0%.

#### 8. Output:
- Exports the synthetic dataset to an Excel file named 'projectDataset.xlsx'.

This script acts as a powerful tool for creating a representative dataset, enabling exploration of EU fintech trends and analysis of internet usage patterns across different demographic factors.


<br><br>


### Weights Code - Impact of age on income.py
This Python script calculates income weights based on the median equivalised net income of the EU 27 countries for the year 2022, categorized into four age groups: 18-24, 25-49, 50-64, and 65+.

#### Key Components:

#### 1. Age Groups and Median Incomes:
- Defines age groups and their corresponding median equivalised net incomes based on Eurostat data.

#### 2. Total Income Calculation:
- Computes the total income across all age groups.

#### 3. Age Weights Calculation:
- Calculates the percentage contribution of each age group's income to the total income.
- Provides insights into how each age group contributes to the overall income distribution.

#### 4. Terminal Output:
- Prints the calculated age weights based on income distributions.

#### Example Output

```
Estimated age weights based on income distributions:
18-24: 23.37%
25-49: 26.05%
50-64: 27.87%
65+: 22.71%
```

This script serves as a crucial component for understanding the impact of age on income distributions within the EU. The displayed age weights offer valuable insights for further trend analysis, enabling a comprehensive examination of the relationship between age demographics and income trends.


<br><br>


### Debugging - Checking Age-Education Adjustments.py
This script is designed to provide valuable insights into the impact of weights on internet usage values within the synthetic dataset. The script allows for experimentation with various weight values to observe how they influence the output.

#### How to Use
To gain insights into the effects of age and education level adjustments on internet usage, follow these steps:

#### 1. Replace the Main Code:
Replace the last section of the main code in "Synthetic Dataset Generator Fintech EU.py" (from line 176) with the provided version in this script.

#### 2. Run the Script:
Execute the modified script to generate a synthetic dataset. During the process, the script will print detailed information for each generated record, including age, education level, original internet usage, age adjustment, education adjustment, and the final internet usage.

#### 3.Experiment with Weights:
Experiment with different weight values in the age and education adjustment sections (lines 195-225) to observe their impact on the internet usage values. Adjust weights and observe how the changes affect the final internet usage percentages.

#### 4.Terminal Output:
Monitor the terminal output to gain insights into how age and education adjustments influence internet usage. The script also calculates and prints the average internet usage for different age groups, providing a summary of the dataset.

#### Example Output

```
Age: 25, Education Level: Advanced
Original Internet Usage: 71.45
Age Adjustment: 2.8307014531357324, Education Adjustment: 1.0594935291138918
Final Internet Usage: 75
Average Internet Usage for people under 25: 62.23034734917733
Average Internet Usage for people 25-50: 72.85337972166998
Average Internet Usage for people 50-65: 60.98571428571429
Average Internet Usage for people over 65: 52.113509192645886
```
 
 
 <br><br>




## _Visualization_

### Data Visualization (Python and Jupyter)
A set of visualizations crafted to scrutinize the validity and realism of the synthetic data outputs. These visual insights delve into age distribution, income disparities by country, average internet usage patterns, and the correlation of 'Internet Usage for Banking (%)' with key variables, ensuring the synthetic dataset closely mirrors real-life data dynamics.
 
 <br><br>

### Power BI Dashboards   
Visualizations showcasing insights, trends, and correlations derived from the datasets.


<br><br>



## _Acknowledgments_

Eurostat Datasets: Valuable sources of real-life EU demographic and fintech adoption data, pivotal for this analysis.

ChatGPT: Provided assistance and insights throughout the project.

Power BI: Employed for data visualization and analysis, enhancing the project's visual presentation.


<br><br>



## _Contributions_

Feel free to fork the repository and explore the code. Feedback and suggestions are always welcome! However, please note that pull requests are not being accepted at the moment.

