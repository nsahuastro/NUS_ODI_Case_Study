import requests
import pandas as pd
import os
import glob

# Base API URL
#BASE_URL = "https://api-production.data.gov.sg/v2/public/api"

# Collection ID for Resale Flat Prices
#COLLECTION_ID = 189

#url= f"{BASE_URL}/collections/{COLLECTION_ID}/metadata"

# Get HDB data from data.gov.sg
def get_hdb_metadata_from_api(BASE_URL, COLLECTION_ID):
    """Get list of all HDB datasets"""
    url= f"{BASE_URL}/collections/{COLLECTION_ID}/metadata"
    collection_response = requests.get(url)
    collection = collection_response.json()
    
    # Extract the child dataset IDs
    child_dset_id = collection['data']['collectionMetadata']['childDatasets']
    child_datasets_info=[]
    for cid in child_dset_id:
        url_child_dset=f"{BASE_URL}/datasets/{cid}/metadata"
        child_data_response=requests.get(url_child_dset)
        child_datasets_info.append(child_data_response.json())

    print(f"Found {len(child_datasets_info)} datasets:")
    
    return [child_dset_id, child_datasets_info]



def load_hdb_data_from_csv(folder_path="."):
    """
    loads HDB data from csv file obtained from data.gov.sg
    """

    #find all csv files in the folder
    csv_files=glob.glob(os.path.join(folder_path,"*.csv"))
  
    # raise error if file not found
    if len(csv_files)>0:
        print(f"Found {len(csv_files)} csv files in {folder_path}")
    else:
        raise ValueError(f"No csv files found in {folder_path}")
    
    #reading all csv files
    data_frames=[]
    for file in csv_files:
        try:
            df=pd.read_csv(file)
            data_frames.append(df)
            print(f"Loaded {file} with shape {df.shape}")
            print(f"Columns: {list(df.columns)}")
            print(df.head(2))
        except Exception as e:
            print(f"Error loading file {file}: {e}")
    
    #finding reference column set that has all possible columns names
    reference_columns = set()
    for df1 in data_frames:
        try:
            #df=pd.read_csv(file)
            reference_columns |= set(df1.columns)
        except Exception as e:
            print(f"Error reading the file {file}: {e}")
            continue
    reference_columns_list=list(reference_columns)
    print(f"all unique columns across all files: {reference_columns_list}")

    #modifying dataframes by reindexing  to match reference columns
    modified_data_frames=[]
    total_rows=0
    for df1 in data_frames:
        try:
            print(f"checking dataframe with shape {df1.shape}")
            print(f"Missing columns to be filled with NaN: {[col for col in reference_columns_list if col not in df1.columns]}")
            df1=df1.reindex(columns=reference_columns_list)
            modified_data_frames.append(df1)
            total_rows += len(df1)
            print(f"Columns: {list(df1.columns)}")
            print(df1.head(2))
            print("\n")
        except Exception as e:
            print(f"Error modifying the columns of file {file}: {e}")

    combined_df= pd.concat(modified_data_frames, ignore_index=True)
    print(f"combined dataframe with rows {total_rows}")
    
    return combined_df


