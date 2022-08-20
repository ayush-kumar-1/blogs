import requests
import pandas as pd 
import os

class FRED(): 
    """
    Class to easily query data from St. Louis Federal Reserve using 
    the FRED api. 
    """
    
    OBSERVATIONS_URL : str = "https://api.stlouisfed.org/fred/series/observations"

    def __init__(self, api_key: str) -> None:
        self.api_key = api_key

    def get_series(self, series_id) -> pd.DataFrame: 
        """
        Returns the specified series as a pandas dataframe. 
        """
        params = {
            "series_id": series_id, 
            "api_key": self.api_key,
            "file_type": "json" 
        }
        res = requests.get(url, params=params)

    def get_fred_series(api_key, series_id):
        url = "https://api.stlouisfed.org/fred/series/observations"
        params = {
            "series_id": series_id,
            "api_key": api_key, 
            "file_type": "json"}
        res = requests.get(url, params=params)
        return json.loads(res.text)

