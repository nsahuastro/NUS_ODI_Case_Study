# HDB Prices and COE Relationship Analysis

## Overview
This notebook analyzes the relationship between Singapore's HDB resale prices and Car COE (Certificate of Entitlement) prices, specifically examining if high COE prices influence housing location choices between central and distant towns.

## Data Sources
1. HDB Resale Transactions
   - Source: Processed HDB data with coordinates and MRT distances
   - File: `hdb_data_with_coords_mrt_dist_id.csv`

2. Car COE Data
   - Source: COE Bidding Exercise Results
   - File: `COE_Car_data/Results of COE Bidding Exercise - Results.csv`

## Analysis Components

### 1. Data Preparation
- Cleaning COE data (removing '$', ',' and converting types)
- Filtering relevant COE categories (Cat A & B cars)
- Temporal alignment of HDB and COE data

### 2. Town Classification
- Central Towns: Toa Payoh, Queenstown
- Distant Towns: Sengkang, Punggol

### 3. Analysis Methods
1. **Price Trend Visualization**
   - Long-term price trends by town type
   - COE price overlay analysis
   
2. **Correlation Analysis**
   - Raw price correlations
   - Percentage change correlations
   - Price gap vs COE relationship

3. **Advanced Statistical Tests**
   - Linear detrending analysis
   - Granger causality tests (1-4 year lags)

## Key Findings

### 1. Price Correlations
- Moderate positive correlations (0.28-0.47 range)
- Distant towns show stronger correlation with COE prices
- Average correlation:
  - Distant towns: 0.46
  - Central towns: 0.30

### 2. Price Gap Analysis
- Early Period (2006-2010): Distant towns commanded premium
- Transition (2011-2013): Central towns gained premium as COE prices rose
- Recent Period (2020-2025): Volatile gap with recent narrowing

### 3. Causal Analysis
- Detrended correlation betweeb (central-distance) hdb price vs coe price: -0.65
- Granger causality suggests 2-4 year lagged effects
- Evidence of delayed rather than immediate causality

## Dependencies
```python
import pandas as pd
import numpy as np
import statsmodels.formula.api as smf
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats
from statsmodels.tsa.stattools import grangercausalitytests
```

## Conclusions
1. Trade-off theory has some merit but relationship is complex
2. COE prices show moderate influence on housing location choices
3. Effect is more pronounced in distant towns
4. Time-lagged effects suggest delayed market responses
5. Multiple factors beyond COE influence housing decisions

## Limitations
- Long-term trend effects may mask short-term relationships
- Limited town sampling (2 central, 2 distant)
- Other economic factors not controlled for
- Analysis period constrained by data availability