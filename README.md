
# Project Title

## Overview

This project aims to analyze agricultural data (`MD_agric_df`) alongside weather data to explore potential correlations and test hypotheses related to weather impacts on agriculture. The key objective is to perform statistical analysis by mapping weather data to agricultural field data, calculating relevant parameters, and conducting a **t-test** to evaluate our hypothesis.

## Objectives

1. Define a null hypothesis and conduct a **t-test**.
2. Import and clean the **MD_agric_df** dataset.
3. Import supplementary weather data and map it to the agricultural dataset.
4. Calculate the mean values for relevant parameters in both datasets.
5. Compute all necessary parameters for the **t-test**.
6. Interpret the results and conclude whether the data supports or rejects the null hypothesis.

## Workflow

### Step 1: Define the Null Hypothesis
Create a testable null hypothesis that explores a specific relationship or difference between the two datasets (e.g., "There is no significant difference in average temperature between locations with high and low crop yields").

### Step 2: Data Import and Cleaning
1. Import the **MD_agric_df** dataset.
2. Perform data cleaning, including handling missing values, outliers, and ensuring data consistency.

### Step 3: Import Weather Data
1. Import weather data from the specified source.
2. Perform any necessary preprocessing, such as cleaning and formatting.

### Step 4: Map Weather Data to Field Data
1. Use a mapping key (e.g., `Field_ID`) to merge weather data with the agricultural dataset.
2. Ensure the mapping is correct by checking for any mismatches or duplicates.

### Step 5: Calculate Mean Values
1. Calculate the mean values for relevant parameters in both the weather and agricultural datasets.
2. Store these values for later statistical analysis.

### Step 6: Perform t-Test
1. Calculate necessary parameters for the t-test, including variances and sample sizes.
2. Use these parameters to perform a **t-test** on the means of the weather and main datasets.

### Step 7: Interpret Results
1. Analyze the results of the **t-test**.
2. Draw conclusions regarding the null hypothesis, and document findings in the final report.

## File Structure

```plaintext
project/
├── data/
│   ├── MD_agric_df.csv            # Main agricultural dataset
│   ├── weather_data.csv           # Weather data for mapping
├── notebooks/
│   └── analysis.ipynb             # Jupyter Notebook with step-by-step analysis
├── src/
│   ├── data_cleaning.py           # Script for data cleaning
│   ├── data_mapping.py            # Script for mapping weather data to field data
│   └── t_test_analysis.py         # Script for performing t-test analysis
├── README.md                      # Project documentation
└── requirements.txt               # Python dependencies
```

## Requirements

Install dependencies using `pip`:

```bash
pip install -r requirements.txt
```

## Usage

1. **Data Cleaning**: Run `data_cleaning.py` to clean the imported data.
2. **Data Mapping**: Use `data_mapping.py` to map weather data to field data.
3. **Statistical Analysis**: Run `t_test_analysis.py` to calculate means, perform a t-test, and interpret results.

### Example Commands

```bash
# Run data cleaning
python src/data_cleaning.py

# Map weather data to field data
python src/data_mapping.py

# Conduct t-test analysis
python src/t_test_analysis.py
```

## Results

The results will be printed to the console and saved as an output file in the `results/` directory. Analysis of the t-test results will help in determining whether to reject the null hypothesis.

## License

This project is licensed under the MIT License. See `LICENSE` for more details.


