# HDB Price Analysis and Prediction

## Overview
This repository contains a comprehensive analysis of Singapore's HDB resale prices, including data processing, visualization,  multiple prediction models, classification model, and policy/governance models implemented in Jupyter notebooks.

## Repository Structure

### Data Processing
- get_hdb_data.py: Functions to fetch HDB data from government APIs
- preprocessing_hdb_data.py: Data cleaning and preprocessing utilities
- hdb_analysis.ipynb: Notebook for geocoding and enriching HDB data with MRT information. See [README](README_HDB_Data_cleaning_aggregration_and_setup) for more details.

### Models
1. **XGBoost Models**
   - HDB_Price_Predictor_XGBoost_Model_V1.ipynb: Basic XGBoost implementation, check model [README](README_XGBoost_Model_V1.md)
   - HDB_Price_Predictor_XGBoost_Model_V2.ipynb: Enhanced XGBoost with additional features, check model  [README](README_XGBoost_Model_V2.md) 
   - See individual model READMEs for detailed performance metrics
        

2. **Random Forest Model**
   - HDB_Price_Predictor_RandomForrest_Model_V1.ipynb: Random Forest implementation
   - Refer to model [README](README_RandomForrest_Model_V1.md)for feature importance and accuracy metrics

3. **Statistical Model**
   - HDB_Price_Predictor_OLS_Statsmodel_V1.ipynb: OLS regression analysis
   - Check model [README](README_OLS_Statsmodel_V1.md) for statistical insights

4. **Classification Model**
   - Flat_Type_Classification_Model.ipynb: Predicts flat types using various features
   - See model [README](README_Flat_Type_Classification_Model.md) for classification performance details

5. **Difference in Differences Model**
   - DiD_Model.ipynb: Analyses causal effect of DT line 2 opening on resale prices of HDBs in towns served by this line
   - See model [README](README_DiD_Model.md) for details
6. **HDB Prices and CAR COE Relationship Analysis**
   - Car_COE_vs_HDB_price_relation.ipynb : analyzes the relationship between Singapore's HDB resale prices and Car COE (Certificate of Entitlement) prices, specifically examining if high COE prices influence housing location choices between central and distant towns.
   - Analysis methods: 
      - Price Trend Visualization
      - Correlation Analysis
      - Advanced Statistical Tests: Linear detrending analysis, Granger causality tests 
   - See model [README](README_Car_COE_vs_HDB_price_relation.md) for details

### Data Folders
- Processed_Data: Contains cleaned and enriched datasets
- ResaleFlatPrices: Raw HDB resale transaction data

## Setup

### Requirements
```bash
pip install -r requirements.txt
```

### Environment Variables
```bash
# OneMap API token for geocoding
export ONEMAP_TOKEN="your_token_here"
```

## Usage
1. Run data processing:
````python
python preprocessing_hdb_data.py
````

2. Open desired model notebook:
```bash
jupyter notebook HDB_Price_Predictor_XGBoost_Model_V2.ipynb
```

## Model Performance Summary
- XGBoost V2: Best overall performance r2=0.97
- Random Forest: Good balance of accuracy and interpretability
- OLS Model: Provides statistical insights
- Classification Model: >99% accuracy for flat type prediction

For detailed model analysis and performance metrics, refer to individual model READMEs.

## Contributing
1. Fork repository
2. Create feature branch
3. Submit pull request

## License
MIT License