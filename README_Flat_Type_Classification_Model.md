# Flat Type Classification Model

## Overview
This notebook implements two classification models to predict HDB flat types:
1. Simple Decision Tree using only floor area
2. Advanced Random Forest using multiple features with class balancing

## Models

### Model 1: Decision Tree Classifier
- Input: floor_area_sqm only
- Performance: 
  - Good F1 scores (>0.9) for most flat types
  - Poor performance on "MULTI-GENERATION" class
- Max depth: 3
- Simple but effective baseline

### Model 2: Random Forest Classifier
```python
RandomForestClassifier(
    n_estimators=100,
    max_depth=20,
    class_weight='balanced',
    n_jobs=-1
)
```
- Features used:
  - Numeric: floor_area_sqm, flat_age, resale_price
  - Categorical: town, flat_model, storey_range
- Performance:
  - Excellent F1 scores (≥0.99) for all classes
  - Successfully handles "MULTI-GENERATION" class
  - >99% true positive rate

## Data Processing
- Standard scaling for numeric features
- One-hot encoding for categorical features
- Stratified train-test split (80/20)
- Class balancing for minority classes

## Visualizations
1. Exploratory:
   - Average floor area by flat type
   - Floor area distribution strips
2. Model Performance:
   - F1 scores per flat type
   - Confusion matrix heatmaps
   - Feature importance rankings

## Key Findings
1. Floor area strongly correlates with flat type
2. Model 2 achieves near-perfect classification
3. Top predictive features:
   - Floor area
   - Resale price
   - Flat model features

## Dependencies
```python
- pandas
- numpy
- scikit-learn
- matplotlib
- seaborn
```

## Usage
```python
# Load and preprocess data
feature_df = pd.DataFrame({
    "town": df["town"],
    "flat_model": df["flat_model"],
    "storey_range": df["storey_range"],
    "floor_area_sqm": df["floor_area_sqm"],
    "flat_age": ((df["month"] - df["lease_commence_date"]).dt.days / 365.25),
    "resale_price": df["resale_price"]
})

# Fit model
model2 = RandomForestClassifier(
    n_estimators=100,
    max_depth=20,
    class_weight='balanced',
    random_state=42
)
model2.fit(X_train2_preprocessed, y_train2)
```

## Future Improvements
1. Feature engineering:
   - Add location-based features
   - Create price per sqm features
2. Model enhancements:
   - Grid search for hyperparameters
   - Try other algorithms (XGBoost, LightGBM)
3. Add:
   - Cross-validation
   - Model persistence
   - Prediction interface

## Note
The model achieves excellent classification accuracy but should be periodically retrained as housing patterns evolve.