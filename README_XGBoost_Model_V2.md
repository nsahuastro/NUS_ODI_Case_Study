# HDB Price Predictor (XGBoost Model V2)

## Overview
This notebook implements a machine learning pipeline to predict HDB resale prices in Singapore using XGBoost. The model is trained on historical data up to 2016 and validates predictions for 2017.

## Key Components

### 1. Data Preparation
- Input: HDB resale transactions data from CSV ('hdb_data_with_coords_mrt_dist_id.csv')
- Features used:
  - Numeric: resale_year, flat_age, floor_area_sqm, remaining_lease
  - Categorical: town, flat_type, flat_model, storey_range


### 2. Data Processing Pipeline
- `filter_data_for_modeling()`: Splits data into past (≤2016) and future (>2016) sets
- `preprocess_features_pipeline()`: 
  - Standardizes numeric features
  - One-hot encodes categorical features
  - Handles missing values and unknown categories

### 3. Model Architecture
```python
XGBRegressor(
    n_estimators=500,
    learning_rate=0.05,
    max_depth=8,
    subsample=0.8,
    colsample_bytree=0.8,
    random_state=42
)
```

### 4. Model Evaluation
- Metrics used:
  - RMSE (Root Mean Square Error)
  - MAPE (Mean Absolute Percentage Error)
  - R² (Coefficient of Determination)
- Visualization:
  - Predicted vs Actual scatter plots
  - Residual analysis
  - Price distribution analysis

### 5. Prediction Function
```python
predict_resale_price(
    model, actual_df, flat_type, town, flat_age, 
    flat_model, floor_area_sqm, storey_range, 
    remaining_lease, resale_year
)
```
- Predicts price for new inputs
- Finds similar transactions for comparison
- Provides price distribution analysis

## Usage Example
```python
predicted_price, similar_flats = predict_resale_price(
    model=xgb_model,
    flat_type='4 ROOM',
    town='YISHUN',
    flat_age=33,  # 2017-1984
    resale_year=2017,
    flat_model="New Generation",
    floor_area_sqm=91,
    storey_range="10 TO 12",
    remaining_lease=66  # 99-(2017-1984)
)
```

## Performance
- Test set (2016 data):
  - Shows strong predictive performance
  - R² > 0.9 indicates excellent fit
- Future predictions (2017):
  - Maintains good accuracy
  - Validated against actual transactions

## Validation Tools
- Similar transaction finder
- Price distribution analysis with Gaussian fit
- Visual comparison tools for predicted vs actual prices

## Dependencies
- pandas
- numpy
- matplotlib
- seaborn
- scikit-learn
- xgboost
- scipy

## Notes
- Model trained on pre-2017 data
- Predictions most reliable for typical HDB configurations
- Consider local market conditions when interpreting results

## Possible Future Improvements
- Add more features (e.g., amenities proximity) from external data
- Implement time-series components
- Add confidence intervals for predictions using Bayesian model
- Include market trend adjustments