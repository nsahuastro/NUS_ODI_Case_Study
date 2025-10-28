# HDB Data Processing and Geocoding Pipeline

## Overview
This notebook processes Singapore HDB (Housing & Development Board) resale flat data, enriching it with geographical information including coordinates and nearest MRT stations using OneMap API.

## Features
- Data cleaning and preprocessing
- Address geocoding
- Nearest MRT station identification
- Distance calculations
- Transaction ID assignment

## Pipeline Steps

### 1. Data Loading and Initial Processing
```python
- Import required libraries
- Load HDB data from CSV
- Clean and preprocess initial dataset
```

### 2. Address Processing
```python
- Generate full addresses by combining block, street_name, and town
- Create unique address set to minimize API calls
- Store processed data in 'Processed_Data' folder
```

### 3. Geocoding (OneMap API)
```python
- Convert addresses to coordinates (latitude/longitude)
- Handle failed geocoding with fallback address modification
- Store coordinates in address_to_coords dictionary
- Add coordinates as new columns to main dataframe
```

### 4. MRT Station Processing
```python
- Find nearest MRT station for each address
- Search radius: 2km (fallback to 4km if needed)
- Store MRT information:
  - Station ID
  - Station name
  - MRT coordinates
  - Road name
```

### 5. Distance Calculation
```python
- Calculate distance between HDB flat and nearest MRT
- Use Haversine formula for geodesic distance
- Store distances in kilometers
```

## Functions

### `get_coordinates(address)`
Converts address to coordinates using OneMap API

### `get_nearest_mrt_coordinates(latitude, longitude, radius=2000)`
Finds nearest MRT station within specified radius

### `haversine(lat1, lon1, lat2, lon2)`
Calculates distance between two coordinate pairs

## Output Files
- processed_hdb_data_w_full_address.csv
- hdb_data_geocoded_test3.csv
- hdb_data_geocoded_mrt.csv
- hdb_data_with_dist_mrt.csv
- hdb_data_with_coords_mrt_dist_id.csv

## Requirements
```python
- pandas
- numpy
- requests
- datetime
- statsmodels
- matplotlib
```

## API Requirements
- OneMap API token
- Rate limiting: 0.2s delay between requests

## Usage
1. Set up environment:
```bash
pip install -r requirements.txt
```

2. Configure API token:
```python
TOKEN = "your_onemap_api_token"
```

3. Run notebook cells sequentially

## Notes
- Geocoding success rate is monitored
- Failed geocoding attempts use modified address format
- MRT search uses expanding radius (2km → 4km)
- Unique transaction IDs added for referencing

## Data Structure
Final dataset includes:
- Original HDB data
- Full addresses
- HDB coordinates
- Nearest MRT information
- Distance to MRT
- Unique transaction IDs

## Future Improvements
1. Implement batch processing for API calls
2. Add error recovery mechanisms
3. Include more POI distances
4. Add data validation steps
5. Implement progress tracking

## Known Limitations
- API rate limits
- Geocoding accuracy depends on address format
- MRT distance limited to 4km radius
- Some addresses may not be geocoded