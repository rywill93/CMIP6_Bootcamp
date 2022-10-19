import baspy as bp
import numpy as np
import os
import netCDF4
from netCDF4 import Dataset
import xarray as xr

# Search catalogue of data on CEDA and store results in a dataframe - Arguments can give: 
df = bp.catalogue(dataset='cmip6', Model='EC-Earth3', Experiment=['historical','ssp370','ssp585'], CMOR = 'Amon', Var = 'tas')

# Save dataframe search results to CSV file
df.to_csv(path_or_buf='/home/users/rywill93/baspy_output.csv', index=False) # Output all model run metadata to CSV

i = -1 # Keep track of model runs included

### Iterate over rows in catalogue - We may only be interested in the first available ensemble member for historical, ssp370 and ssp585
for index, row in df.iterrows():  

    i = i + 1
    print (i)

    # Refer to model column storing the Experiment ID
    if df.iloc[i,3] == df.iloc[i-1,3]:
    
        continue # Ignore row if model is same as in row before (we only want want the first available ensemble member for each experiment)
    
    elif df.iloc[i,3] != df.iloc[i-1,3]:

        # Only one realisation per model is read in!

        myfile = bp.open_dataset(row, use_cftime = 'True') # xarray
        #myfile = bp.get_cube(row) # iris

        #print(myfile)

        # Read in Variables
        tas = myfile.tas 
        lat = myfile.lat
        lon = myfile.lon
        time = myfile.time

        tas = tas.sel(time=slice("1940-01", "1969-12")) # Index time dimension

    


    
