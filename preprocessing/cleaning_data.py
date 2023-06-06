import pandas as pd

df_zip = pd.read_csv("zip_to_nis.csv")
list_zip = df_zip["zipCode"].to_list()
list_names = df_zip["name"].to_list()

dict_zip_names = {list_zip[i]: list_names[i] for _ in list_zip }

"""
{
  "data": {
    "area": int,
    "property-type": "APARTMENT" | "HOUSE" | "OTHERS",
    "rooms-number": int,
    "zip-code": int,
    "land-area": Optional[int],
    "garden": Optional[bool],
    "garden-area": Optional[int],
    "equipped-kitchen": Optional[bool],
    "full-address": Optional[str],
    "swimming-pool": Optional[bool],
    "furnished": Optional[bool],
    "open-fire": Optional[bool],
    "terrace": Optional[bool],
    "terrace-area": Optional[int],
    "facades-number": Optional[int],
    "building-state": Optional[
      "NEW" | "GOOD" | "TO RENOVATE" | "JUST RENOVATED" | "TO REBUILD"
    ]
  }
}"""

rename_dict {
    "area": "living_area",
    "property-type": 'building_type',
    "rooms-number": int,
    "zip-code": int,
    "land-area": Optional[int],
    "garden": Optional[bool],
    "garden-area": Optional[int],
    "equipped-kitchen": Optional[bool],
    "full-address": Optional[str],
    "swimming-pool": Optional[bool],
    "furnished": Optional[bool],
    "terrace-area": Optional[int],
  }

def preprocess(data: dict):
    df = pd.DataFrame(data)
    df.rename(columns=some_dict, inplace=True)

    df_preprocessed = pd.DataFrame(columns=[[
        "living_area",
        "terrace",
        "garden",
        "swimming_pool",
        "energy_class",
        "municipality"]])
    
    df_municipality = pd.get_dummies(df_selection[["municipality"]])

    df_preprocessed['living_area'] = df["area"]

    df_preprocessed['terrace'] = df["area"]
    df_preprocessed['garden'] = df["area"]
    df_preprocessed['swimming_pool'] = df["area"]
    df_preprocessed['energy_class'] = df["area"]
    df_preprocessed['municipality'] = df["zip-code"]
    df_preprocessed['municipality'] = df_preprocessed['municipality'].rename(dict_zip_names)
    df_municipality = pd.get_dummies(df_selection[["municipality"]])
