import pandas as pd

# Population Data
population_data = {
    'Country': ['Germany', 'Bosnia', 'United States'],
    'Population': [83019200, 3516816, 331002651]
}

# Climate Data
climate_data = {
    'Country': ['Germany', 'Bosnia', 'United States'],
    'Average Temperature (°C)': [10.9, 13.5, 12.6]
}

# Create DataFrames
population_df = pd.DataFrame(population_data)
climate_df = pd.DataFrame(climate_data)

# Save DataFrames to CSV
population_df.to_csv('population_data.csv', index=False)
climate_df.to_csv('climate_data.csv', index=False)

print(population_df, climate_df)
