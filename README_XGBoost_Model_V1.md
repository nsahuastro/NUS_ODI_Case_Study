# HDB Price Predictor (XGBoost Model V1)

## Overview
This notebook implements an XGBoost-based machine learning model to predict HDB resale prices in Singapore, trained on pre-2014 data and validated against 2014 transactions.

## Components

### 1. Data Loading & Preprocessing
- Input: hdb_data_with_coords_mrt_dist_id.csv
- Key Features:
  - Numeric: resale_year, flat_age
  - Categorical: town, flat_type


### 2. Data Processing Functions
#### `filter_data_for_modeling()`
- Splits data into past (≤2013) and future (>2013) sets
- Handles datetime conversions
- Calculates flat age from lease commence date
- Creates feature and target DataFrames

#### `preprocess_features_pipeline()`
- Standardizes numeric features
- One-hot encodes categorical features
- Handles unknown categories at prediction time

### 3. Model Configuration
```python
XGBRegressor(
    n_estimators=500,
    learning_rate=0.05,
    max_depth=6,
    subsample=0.8,
    colsample_bytree=0.8,
    random_state=42
)
```

### 4. Evaluation Metrics
- RMSE (Root Mean Square Error)
- MAPE (Mean Absolute Percentage Error)
- R² (Coefficient of Determination)

### 5. Prediction Function
```python
predict_resale_price(
    model, 
    actual_df, 
    flat_type, 
    town, 
    flat_age, 
    resale_year=2014
)
```
Features:
- Makes single prediction
- Finds similar transactions
- Provides price statistics for comparable units

## Usage Example
```python
predicted_price, similar_flats = predict_resale_price(
    model=xgb_model,
    flat_type='4 ROOM',
    town='BEDOK',
    flat_age=25,
    resale_year=2014,
    actual_df=comparison_data
)
```

## Visualization
The notebook includes:
- Predicted vs Actual price scatter plots
- Residual analysis plots
- Year-specific performance analysis (2014)

## Dependencies
- pandas
- numpy
- matplotlib
- seaborn
- scikit-learn
- xgboost
- statsmodels

## Model Performance
- Test set (pre-2014):
  - High R² value (>0.9)
  - Low RMSE relative to price range
- Future predictions (2014):
  - Maintains prediction accuracy
  - Validates well against actual transactions

## Limitations
- Limited feature set compared to V2
- Fixed train/test split at 2013
- No storey range or floor area features
- Basic validation approach

## Key Differences from V2
- Fewer input features
- Simpler model architecture
- Earlier cutoff year (2013 vs 2016)
- More basic prediction validation

## Future Improvements, some already implemented in V2
- Add more features (floor area, remaining lease)
- Implement rolling validation
- Add confidence intervals
- Include market trends analysis