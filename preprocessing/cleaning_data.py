import pandas as pd


df_zip = pd.read_csv('preprocessing/zipcode-belgium.csv')
df_zip = df_zip.drop_duplicates(subset='postcode', keep="first")
list_zip = df_zip["postcode"].to_list()
list_names = df_zip["municipality"].to_list()

dict_zip_names = {k: v for k, v in zip(list_zip, list_names)}
dummies_list = pd.read_csv("preprocessing/df_municipality_dummies.csv").columns.to_list()
data_headers = [
    "area",
    "property_type",
    "rooms_number",
    "zip_code",
    "land_area",
    "garden",
    "garden_area",
    "equipped_kitchen", 
    "full_address",
    "swimming_pool",
    "furnished",
    "open_fire",
    "terrace",
    "terrace_area",
    "facades_number",
    "building_state"
]
headers = [
"living_area",
"terrace",
"garden",
"swimming_pool"]
headers.extend(dummies_list)


def preprocess(data: dict):
    df = pd.DataFrame(columns= data_headers, index = [0])
    df_preprocessed = pd.DataFrame(columns= headers)
    print(df)
    for key in data:
        df[key] = data[key]
    df = df.fillna(0)

    # Dealing with living_area
    df_preprocessed["living_area"] = df['area']
    # Dealing with terraces
    df["terrace"] = df["terrace"].replace(True, 1).fillna(0)
    df_preprocessed["terrace"] = df[["terrace", "terrace_area"]].sum(axis=1, skipna=False).fillna(0)
    # Dealing with garden
    df["garden"] = df["garden"].replace(True, 1).fillna(0)
    df["garden_area"] = df["garden_area"].fillna(0)
    df_preprocessed["garden"] = df[["garden", "garden_area"]].sum(axis=1, skipna=False).fillna(0)
    # Dealing with swimming_pool
    df_preprocessed["swimming_pool"] = df["swimming_pool"].replace([True, False], [1, 0]).fillna(0)
    # Dealing with locality
    print(df)
    print(df['zip_code'])
    df_preprocessed[f"municipality_{dict_zip_names[df.at[0, 'zip_code']]}"] = 1

    df_preprocessed = df_preprocessed.fillna(0)
    df_preprocessed = df_preprocessed.drop(columns = ["Unnamed: 0"])
    return df_preprocessed

