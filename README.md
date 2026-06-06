# Data_Pipeline_Development_1

**COMPANY**: CODTECH IT SOLUTIONS

**NAME**: kORSIPATI MIDHILESH REDDY

**INTERN ID**: CTIS9177

**DOMAIN**: DATA SCIENCE

**BATCH DURATION**: MAY 9th, 2026 TO JUNE 6th, 2026

**ETL Pipeline Development Using Pandas and Scikit-Learn**

The objective of this project is to develop an ETL (Extract, Transform, Load) pipeline using Python, Pandas, and Scikit-Learn. ETL pipelines are widely used in data engineering and machine learning workflows to prepare raw data for analysis and model training. This pipeline automates the process of loading data, cleaning and transforming it, splitting it into training and testing sets, and finally saving the processed data for future use.

Extract Phase

The first stage of the ETL process is Extraction, where data is collected from a source. In this project, the dataset is stored in a CSV file named data.csv. The Pandas library is used to read the file into a DataFrame using the read_csv() function.

To ensure reliability, a try-except block is implemented. If the file is not found in the specified location, the program displays an error message and terminates gracefully. Once the dataset is successfully loaded, the first five rows are displayed using the head() function. This allows users to inspect the structure and content of the dataset before processing.

Transform Phase

The transformation phase is the most important step of the ETL pipeline. Raw data often contains missing values, inconsistent formats, and categorical variables that cannot be directly used by machine learning algorithms. Therefore, several preprocessing operations are performed.

Handling Missing Values

Missing values can negatively affect the performance of machine learning models. To address this issue, the pipeline identifies all numerical columns using the select_dtypes() method. The SimpleImputer class from Scikit-Learn is then used with the mean strategy, which replaces missing numerical values with the average value of the corresponding column.

This approach preserves the dataset size and reduces information loss compared to deleting rows containing missing values. After imputation, the updated dataset is displayed to verify that missing values have been handled successfully.

Encoding Categorical Data

Machine learning algorithms require numerical input. Therefore, categorical columns containing text values must be converted into numeric representations. The pipeline identifies all object-type columns and applies LabelEncoder.

Each unique category is assigned a numeric label. For example, values such as "Male" and "Female" may be converted into 0 and 1. This transformation enables machine learning models to process categorical information efficiently.

After encoding, the transformed dataset is displayed to show the converted values.

Feature and Target Separation

The dataset is then divided into two components:

Features (X): Independent variables used for prediction.
Target (y): Dependent variable that the model aims to predict.

The pipeline assumes that the last column of the dataset represents the target variable. All preceding columns are considered input features.

Feature Scaling

Feature scaling is performed using StandardScaler. Different features may have different units and value ranges, which can negatively impact many machine learning algorithms.

Standardization transforms each feature so that it has:

Mean = 0
Standard Deviation = 1

This ensures that all features contribute equally to the model training process and improves convergence for algorithms such as Logistic Regression, Support Vector Machines, and Neural Networks.

The first few rows of the scaled feature matrix are displayed for verification.

Train-Test Split

After preprocessing, the dataset is divided into training and testing subsets using the train_test_split() function.

The split ratio used is:

80% Training Data
20% Testing Data

A random_state value of 42 is specified to ensure reproducibility of results. The training dataset is used to train machine learning models, while the testing dataset is reserved for evaluating model performance on unseen data.

The shapes of the training and testing datasets are printed to confirm successful splitting.

Load Phase

The final stage of the ETL process is Loading. The processed datasets are saved as separate CSV files:

X_train.csv
X_test.csv
y_train.csv
y_test.csv

These files can be directly used for machine learning model development, testing, and deployment without repeating the preprocessing steps.

Conclusion

This ETL pipeline demonstrates a complete data preprocessing workflow using Pandas and Scikit-Learn. It efficiently extracts data from a CSV file, handles missing values, encodes categorical features, scales numerical data, performs train-test splitting, and stores the processed datasets. By automating these tasks, the pipeline ensures consistency, improves data quality, and provides a reliable foundation for machine learning and data analytics projects.
