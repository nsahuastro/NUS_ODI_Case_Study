# HDB Price Predictor (Random Forest Model V1)

## Overview
A machine learning pipeline using Random Forest Regression to predict HDB resale prices in Singapore. The model is trained on data up to 2013 and validates against 2014 transactions.

## Key Components

### 1. Data Processing
```python
Input: hdb_data_with_coords_mrt_dist_id.csv
Features:
- Numeric: resale_year, flat_age
- Categorical: town, flat_type
```

### 2. Core Functions

#### Data Preparation
```python
filter_data_for_modeling(clean_hdb_df, year_cutoff=2013)
- Splits data into past/future sets
- Handles datetime conversions
- Calculates flat age
- Creates feature/target pairs
```

#### Feature Processing
```python
preprocess_features_pipeline(feature_df, numeric_features, categorical_features, preprocessor, fit)
- Standardizes numeric features
- One-hot encodes categorical features
- Handles unknown categories
```

### 3. Model Architecture
```python
RandomForestRegressor(
    n_estimators=500,
    max_depth=10,
    min_samples_split=2,
    min_samples_leaf=1,
    n_jobs=-1,
    random_state=42
)
```

### 4. Prediction Interface
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

## Usage Example
```python
predicted_price, similar_flats = predict_resale_price(
    model=rf_model,
    flat_type='4 ROOM',
    town='BEDOK',
    flat_age=25,
    resale_year=2014,
    actual_df=comparison_data
)
```

## Model Performance
- Metrics tracked:
  - RMSE (Root Mean Square Error)
  - MAPE (Mean Absolute Percentage Error)
  - R² (Coefficient of Determination)
- Visualization:
  - Predicted vs Actual scatter plots
  - Residual analysis plots

## Dependencies
- pandas
- numpy
- scikit-learn
- matplotlib
- seaborn

## Key Features
- Automated feature preprocessing
- Similar property finder
- Price range analysis
- Visual performance metrics

## Advantages vs XGBoost Version
- More interpretable
- Less prone to overfitting
- Better handles outliers
- Native feature importance

## Limitations
- Basic feature set
- Fixed 2013 cutoff
- No location-based features
- Limited price factors

## Future Improvements
- Add more features:
  - Floor area
  - Storey range
  - Remaining lease
  - Distance to amenities
- Implement:
  - Cross-validation
  - Feature importance analysis
  - Confidence intervals
  - Time-based validation
