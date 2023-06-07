import pandas as pd


df_zip = pd.read_csv('zipcode-belgium.csv')
df_zip = df_zip.drop_duplicates(subset='postcode', keep="first")
list_zip = df_zip["postcode"].to_list()
list_names = df_zip["municipality"].to_list()

dict_zip_names = {k: v for k, v in zip(list_zip, list_names)}
dummies_list = pd.read_csv("df_municipality_dummies.csv").columns.to_list()
headers = [
"living_area",
"terrace",
"garden",
"swimming_pool"]
headers.extend(dummies_list)


def preprocess(data: dict):
    df = pd.Series(data).to_frame().T

    df_preprocessed = pd.DataFrame(columns= headers)


    # Dealing with living_area
    df_preprocessed["living_area"] = df['area']
    # Dealing with terraces
    df["terrace"] = df["terrace"].replace(True, 1).fillna(0)
    df_preprocessed["terrace"] = df[["terrace", "terrace-area"]].sum(axis=1, skipna=False).fillna(0)
    # Dealing with garden
    df["garden"] = df["garden"].replace(True, 1).fillna(0)
    df["garden-area"] = df["garden-area"].fillna(0)
    df_preprocessed["garden"] = df[["garden", "garden-area"]].sum(axis=1, skipna=False).fillna(0)
    # Dealing with swimming_pool
    df_preprocessed["swimming_pool"] = df["swimming-pool"].replace([True, False], [1, 0]).fillna(0)
    # Dealing with locality

    df_preprocessed[f"municipality_{dict_zip_names[df.at[0, 'zip-code']]}"] = 1

    df_preprocessed = df_preprocessed.fillna(0)

    return df_preprocessed

