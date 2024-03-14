## Get this done by 17.march

- Find out relevant features to include, visualize it to understand better. (done)
  - Include:
    - Hovedart
    - Redskap
    - Rundvekt
    - Lengdegruppe
    - Hovedområde
  
  - Exclude:
    - Trekkavstand
    - Varighet
    - Tidspunkt

- Look at outliers for each of the features we have chosen to include. (1/5)
- Pick 3 models that fits the features we have chosen to include.
- Find out WHAT we have to do with the features we have chosen so that it can be used in our machine learning model.

# Outlier Analysis Guidelines for Feature Exploration

## Objective

- The primary objective of this analysis is to explore and document findings related to outliers within a specific feature of our dataset. By examining outliers, we aim to understand their impact on the dataset and determine appropriate strategies for handling them. This exploration involves identifying outliers, assessing their significance, and deciding on actions such as keeping, modifying, or removing these outliers.

## Dataset Overview

- Feature of Interest: [Insert Feature Name Here]

## Steps for Outlier Analysis

### 1. Identifying Outliers

- Visual Inspection:
  - Generate a Scatter Plot to visualize the distribution of data points. Scatter plots help in spotting outliers as points that fall far from the majority of data.
  - Create a Box Plot for the feature. Box plots visually show the median, quartiles, and outliers as points outside the whiskers.

### 2. Evaluating the Significance of Outliers

- Analyze the outliers identified from the plots to determine their impact. Consider the following:
  - Are these outliers errors in data collection, or do they represent valid extreme values?
  - Is there any instance (such as the blue whale example) that is significantly different from others, making prediction or comparison difficult due to the scarcity of similar data points?

### 3. Deciding on Actions for Outliers (If there are any)

- Based on the evaluation, decide on how to handle the outliers:
  - Retention: If the outlier provides valuable information and is a valid observation, consider keeping it.
  - Modification: In some cases, outliers may be adjusted if they are deemed to be errors but still contain useful information.
  - Removal: If an outlier is considered to not contribute valuable information or is an error that cannot be corrected, consider removing it.

### 4. Analyzing Sparse Entries

- Investigate if there are values within the feature that have significantly fewer entries than others. Consider the context, such as whether these entries represent rare occurrences that are difficult to analyze due to their scarcity.

### 5. Handling Missing Values (NaNs)

- Assess the presence of NaN values within the feature and decide on an approach:
  - Imputation: Is it possible to "Guess" the NaN values, such as filling in missing roundweight with an average weight for that species.
  - Categorization: For certain types of data, such as time, categorizing into groups like morning, afternoon, evening, and night might be more appropriate than numeric imputation.
  - Removal: Though not recommended, in cases where NaN values cannot be logically imputed or categorized, and their presence significantly biases the analysis, removal might be considered.

### Documentation and Reporting

- Document each step of the analysis with detailed observations, including the reasoning behind the decisions made regarding outliers.
- Visual aids (plots) should be included to support findings and decisions.
  Conclusions should summarize the impact of outliers on the dataset and the chosen strategies for handling them.

## Tasks for Hejung Yu

Please explore this feature of the dataset: Rundvekt

## Tasks for Tsz Ching

Please explore this feature of the dataset: Redskap

## Tasks for Sverre-Emil

Please explore this feature of the dataset: Hovedområde start

## Tasks for me

Please explore this feature of the dataset: Hovedart FAO, Lengdegruppe
