import re
import numpy as np
import pandas as pd
from field_data_processor import FieldDataProcessor
from weather_data_processor import WeatherDataProcessor
import logging 

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')

config_params = config_params = {
    "db_path": "sqlite:///Maji_Ndogo_farm_survey_small.db",
    "sql_query": """SELECT *
                    FROM geographic_features
                    LEFT JOIN weather_features USING (Field_ID)
                    LEFT JOIN soil_and_crop_features USING (Field_ID)
                    LEFT JOIN farm_management_features USING (Field_ID)
                    """,
    "columns_to_rename": {"Annual_yield": "Crop_type", "Crop_type": "Annual_yield"},
    "values_to_rename": {"cassaval": "cassava", "wheatn": "wheat", "teaa": "tea"},
    "weather_mapping_csv": "https://raw.githubusercontent.com/Explore-AI/Public-Data/master/Maji_Ndogo/Weather_data_field_mapping.csv",
    "weather_csv_path": "https://raw.githubusercontent.com/Explore-AI/Public-Data/master/Maji_Ndogo/Weather_station_data.csv",
    "regex_patterns": {
        'Rainfall': r'(\d+(\.\d+)?)\s?mm',
        'Temperature': r'(\d+(\.\d+)?)\s?C',
        'Pollution_level': r'=\s*(-?\d+(\.\d+)?)|Pollution at \s*(-?\d+(\.\d+)?)'
    }
}


field_processor = FieldDataProcessor(config_params)
field_processor.process()
field_df = field_processor.df

weather_processor = WeatherDataProcessor(config_params)
weather_processor.process()
weather_df = weather_processor.weather_df

def test_read_weather_DataFrame_shape():
    assert weather_df.shape == (1843, 4)

def test_read_field_DataFrame_shape():
    assert field_df.shape == (564, 19)

def test_weather_DataFrame_columns():
    assert (weather_df.columns == np.array(['weather_station_ID', 'Message', 'Measurement', 'Value'])).all()

def test_field_DataFrame_columns():
    assert (field_df.columns == np.array(['Field_ID', 'Elevation', 'Latitude', 'Longitude', 'Location', 'Slope',
                                          'Rainfall', 'Min_temperature_C', 'Max_temperature_C', 'Ave_temps',
                                          'Soil_fertility', 'Soil_type', 'pH', 'Pollution_level', 'Plot_size',
                                          'Annual_yield', 'Crop_type', 'Standard_yield', 'Weather_station'])).all()

def test_field_DataFrame_non_negative_elevation():
    assert len(field_df[field_df['Elevation'] < 0]) == 0

def test_crop_types_are_valid():
    assert (field_df['Crop_type'].unique() == np.array(['cassava', 'tea', 'wheat', 'potato', 'banana', 'coffee', 'rice', 'maize'])).all()

def test_positive_rainfall_values():
    assert len(field_df[field_df['Rainfall'] < 0]) == 0
