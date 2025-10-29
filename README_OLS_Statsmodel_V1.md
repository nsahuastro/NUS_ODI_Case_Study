# HDB Price Predictor (OLS Statsmodel V1)

## Overview
A statistical modeling approach using Ordinary Least Squares (OLS) regression to predict HDB resale prices in Singapore. The model uses log-transformed prices and includes time-based analysis. The model is trained on historical data up to 2013 (threshold year ) and validates predictions for 2014. You can change the threshold year as per your requirement.

The model provides a statistical baseline with interpretable coefficients but consider more flexible approaches (Model 2=Random Forest, Model 3=XGBoost) for better accuracy.

## Key Components

### 1. Data Processing
Features:
- Numeric: resale_year, flat_age
- Categorical: town, flat_type
Target:
- log10(resale_price)

### Exploratory Data Analysis

#### **Data Quality Checks**
- **Size:** Dataset dimensions (rows × columns)  
- **Missing Values:** Detection and visualization using *missingno*  
- **Infinite Values:** Validation in numeric columns  
- **Zero Values:** Analysis of zero-value distributions  
- **Unique Values:** Cardinality checks for categorical features  
- **Memory Usage:** Resource utilization and optimization review  

#### **Price Distribution Analysis**
- **Temporal Trends:** 4-year binned resale prices (1990–2025)  
- **Density Plots:** KDE visualizations of price evolution  
- **Year Groups:** Comparison of chronological pricing patterns  

#### **Visualization Outputs**
1. **Missing Value Matrix** – Visual overview of data completeness and missing-data patterns  
2. **Correlation Heatmap** – Relationships among numeric features and price correlation insights  
3. **Price Distribution Plots** – Temporal evolution, price range analysis, and density visualization  

### 2. Core Functions

#### Data Preparation
```python
filter_data_for_modeling(clean_hdb_df, year_cutoff=2013)
```
- Splits data into past/future sets
- Transforms prices using log10
- Creates feature/target pairs with transaction IDs


#### Feature Processing
```python
prepare_features_sm(df, training_columns=None, drop_first=True)
```
- One-hot encoding for categorical variables
- Maintains column alignment for predictions
- Handles transaction IDs


#### Model Application
```python
apply_model_sm(X_train, Y_train)
```
- Fits OLS regression
- Adds constant term
- Returns statsmodels results object


### 3. Time Analysis
- Groups data into 4-year periods
- Visualizes price distribution evolution
- KDE plots for price trends

### 4. Model Performance
- R² value reported in model summary
- RMSE and Mean Absolute Error tracking
- Visual diagnostics:
  - Predicted vs Actual plots
  - Error distribution analysis
  - Price trend visualization

### 5. Prediction Interface
```python
predict_resale_price(
    model_results,
    training_columns,
    actual_df,
    flat_type,
    town,
    flat_age,
    resale_year=2014
)
```

## Usage Example
```python
predicted_price, similar_flats = predict_resale_price(
    model_results=results_model1_sm,
    training_columns=training_columns,
    flat_type='4 ROOM',
    town='BEDOK',
    flat_age=25,
    resale_year=2014,
    actual_df=comparison_data
)
```

## Key Features
- Log-transformed price modeling
- Time-based price evolution analysis
- Similar property comparison
- Detailed error analysis
- Visual performance metrics

## Dependencies
- pandas
- numpy
- statsmodels
- matplotlib
- seaborn

## Limitations
- Linear model assumptions
- Fixed 2013 cutoff
- Basic feature set
- Potential underprediction issues:
  1. Time trend bias
  2. Nonlinearity in relationships



