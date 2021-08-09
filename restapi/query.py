import pandas as pd
from pathlib import Path

data_path = Path("./data/cities_info.CSV")
countries_data = pd.read_csv(data_path)


def get_data(country_id: int = None, capital: bool = False, area: bool = False):
    if country_id is None:
        return {"countries": countries_data.to_dict(orient="records")}
    elif capital:
        return {"capital": countries_data.iloc[country_id]["capital"]}
    elif area:
        return {"total_area": float(countries_data.iloc[country_id]["total_area"])}
    else:
        return countries_data.iloc[country_id].to_dict()
