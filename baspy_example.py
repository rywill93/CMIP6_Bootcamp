import baspy as bp
import numpy as np
import os
import netCDF4
from netCDF4 import Dataset
import xarray as xr

# Search catalogue of data on CEDA and store results in a dataframe 

# Suppose we want monthly 2m air temperature for all available models for historical, ssp370 and ssp585
df = bp.catalogue(dataset='cmip6', Experiment=['historical','ssp370','ssp585'], CMOR = 'Amon', Var = 'tas') # E.g. Could add if we just wanted for one model: EC-Earth3 (Model='EC-Earth3')

# Save dataframe search results to CSV file
df.to_csv(path_or_buf='/home/users/rywill93/baspy_output.csv', index=False) # Output all model run metadata to CSV (Remember to change filepath)

### Iterate over rows in catalogue - We may only be interested in the first available ensemble member for historical, ssp370 and ssp585 ###
for index, row in df.iterrows():  

    # Refer to model column storing the Experiment ID (as shown in CSV output file)
    if df.iloc[i,3] == df.iloc[i-1,3]:
    
        continue # Ignore row if model is same as in row before (we only want want the first available ensemble member for each experiment)
    
    elif df.iloc[i,3] != df.iloc[i-1,3]:

        # Only one realisation per model is read in!

        myfile = bp.open_dataset(row, use_cftime = 'True') # xarray
        #myfile = bp.get_cube(row) # iris

        print(myfile) # Show metadata

        # Read in Variables
        tas = myfile.tas 
        lat = myfile.lat
        lon = myfile.lon
        time = myfile.time

        tas = tas.sel(time=slice("1940-01", "1969-12")) # Index time dimension

    


    
