# Assignment 2

## Justification

### Task 2: Data Preparation
- **What is UTF?**
-- UTF stands for Unicode Transformation Format. It is a character encoding standard that assigns unique numerical values, 
-- called code points, to every character in the Unicode standard. 
- **Why setting the format of a file is important when reading or writing it?**
-- UTF encoding standards are essential for ensuring that text can be accurately represented, 
-- exchanged, and displayed in a globalized and digital world, regardless of the language or script used. 
-- This universality and consistency make Unicode a fundamental component of modern computing and communication.

### Task 3: Data Exploration
- **What can cause the mean to not be reliable measure?**
-- The mean may not be reliable if there are extreme values (outliers) that significantly skew the average, 
-- giving a false representation of the data
- **What other statistic can you use to avoid this pitfall?**
-- You can use the median instead of the mean to avoid the impact of outliers. 
-- The median is the middle value when data is arranged in order, and it's not affected by extreme values.

### Task 4: Further Analyzes
Document your functions here. In particular:

#### -- Function 1: beer_styles_per_country
- Problem to solve.
-- The problem this function aims to solve is to determine the number of unique beer styles for each country based on the provided beer data.

- Motivation behind the analysis.
-- The motivation behind this analysis is to gain insights into the diversity of beer styles in different countries. It's useful for understanding the variety of beer styles available in each country, which can be valuable for market analysis, beer enthusiasts, or brewers.

- Where in the project your code has been implemented.
-- task4.py

- The design choices you made.
-- The function first initializes an empty dictionary (count1_styles) to store beer styles for each country.
It uses a loop to iterate through the provided beer data.
For each beer entry, it checks if the country is already in the count1_styles dictionary. If not, it initializes a list to store beer styles for that country.
It then appends the beer style to the list for the respective country.
A second dictionary (count2_styles) is created to store the unique beer styles for each country. It uses a set (special_items_set) to keep track of unique styles.
Finally, a third dictionary (count3_styles) is created to count the number of unique beer styles for each country. The result is sorted in descending order by the number of styles.

- Expected input and output of each function you have defined.
Input: A list of dictionaries where each dictionary represents a beer entry with information about the beer, including the country and style.
Output: A dictionary with country names as keys and the number of unique beer styles as values.

#### -- Function 2: total_beer_production
- Problem to solve.
-- The problem this function aims to solve is to calculate the total beer production for each country based on the provided beer data.

- Motivation behind the analysis.
-- The motivation for this analysis is to determine the total beer production for each country, which is essential for tracking and understanding the beer industry's production volumes. This information can be valuable for various stakeholders, including industry analysts and policymakers.

- Where in the project your code has been implemented.
-- task4.py

- The design choices you made.
-- The function initializes an empty dictionary (production) to store the total beer production for each country.
It uses a loop to iterate through the provided beer data.
For each beer entry, it extracts the last 12 values from the dictionary (presumably representing monthly production data).
It checks if the country is already in the production dictionary. If not, it initializes a production count for that country.
It then adds the sum of monthly production values to the country's production count.

- Expected input and output of each function you have defined.
Input: A list of dictionaries where each dictionary represents a beer entry with information about the beer, including the country and production data.
Output: A dictionary with country names as keys and the total beer production (sum of the last 12 values) as values.


#### -- Function 3: compute_mean_abv
- Problem to solve.
--The problem this function aims to solve is to calculate the average alcohol percentage (ABV) for each beer style based on the provided beer data.

- Motivation behind the analysis.
--The motivation for this analysis is to understand the average ABV for different beer styles. This information can be valuable for consumers, brewers, and anyone interested in beer preferences and characteristics.

- Where in the project your code has been implemented.
-- task4.py

- The design choices you made.
--The function initializes two dictionaries: one to store the total ABV for each beer style (abv_mean_dict) and another to store the count of beers for each style (beer_count_dict).
It uses a loop to iterate through the provided beer data.
For each beer entry, it extracts the beer style and ABV.
It updates the total ABV and beer count for each style in their respective dictionaries.
After processing all data, the function calculates the average ABV for each style.

- Expected input and output of each function you have defined.
-- input: A list of dictionaries where each dictionary represents a beer entry with information about the beer, including the style and ABV.
Output: A dictionary with beer style names as keys and the average ABV for that style as values.


