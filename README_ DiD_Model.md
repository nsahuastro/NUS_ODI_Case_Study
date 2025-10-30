# Difference-in-Differences (DiD) Analysis: Impact of Downtown Line Stage 2 on HDB Prices

## Overview
This notebook implements a Difference-in-Differences (DiD) analysis to evaluate the causal impact of Singapore's Downtown Line Stage 2 (DTL2) opening on HDB resale prices.

## Methodology

### Data Preparation
- Input: Processed HDB data with MRT coordinates and distances
- Treatment definition: Properties within 1km of DTL2 stations
- Time periods: 
  - Pre-DTL2: Before December 27, 2015
  - Post-DTL2: After December 27, 2015

### Models Implemented

1. **Baseline Model (Model 1)**
```python
log_price ~ treated + post + treated_post + remaining_lease + floor_area_sqm
```
- Basic DiD specification
- Controls for property characteristics
- Natural log transformation of prices

2. **Fixed Effects Model (Model 2)**
```python
log_price ~ treated + post + treated_post + C(town) + C(flat_type)
```
- Enhanced with town and flat-type fixed effects
- Controls for:
  - Persistent town-level price differences
  - Systematic flat-type variation
  - Location-specific characteristics

## Key Variables

- `treated`: Properties within 1km of DTL2 stations
- `post`: Time period after DTL2 opening
- `treated_post`: DiD interaction term
- `town`: Town fixed effects
- `flat_type`: Property type fixed effects

## Key Findings

### Model Performance
- Explains significant variation in resale prices
- Large sample size ensures robust estimates
- Fixed effects improve model specification

### Policy Impacts
1. **DTL2 Effect**
   - Measurable price premium for nearby properties
   - Statistically significant uplift post-opening

2. **Spatial Variation**
   - Identified high and low-value towns
   - Controls for pre-existing price differences

3. **Market Trends**
   - Captures overall market appreciation
   - Isolates DTL2-specific effects

## Policy Implications

1. **Infrastructure Value**
   - Quantifies transportation accessibility premium
   - Demonstrates wealth creation through infrastructure

2. **Policy Considerations**
   - Equity in transportation access
   - Affordability management
   - Development spillover effects

## Usage

### Requirements
```python
import pandas as pd
import numpy as np
import statsmodels.formula.api as smf
```

### Data Input
```python
clean_hdb_df1 = pd.read_csv('Processed_Data/hdb_data_with_coords_mrt_dist_id.csv',
    parse_dates=['month', 'lease_commence_date'])
```

## Limitations

1. **Assumptions**
   - Parallel trends pre-treatment
   - No other major interventions
   - Stable composition of treatment/control groups

2. **Scope**
   - Limited to 1km radius
   - Focus on immediate price effects
   - Residential properties only

## Future Extensions

1. **Analysis Enhancements**
   - Robustness checks with different radii
   - Additional control variables
   - Alternative treatment definitions

2. **Policy Analysis**
   - Long-term effects tracking
   - Neighborhood composition changes
   - Commercial property impacts

## File Structure
- DiD_Model.ipynb: Main analysis notebook
- Input: `hdb_data_with_coords_mrt_dist_id.csv`
- Dependencies: pandas, numpy, statsmodels