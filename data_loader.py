import pandas as pd

def get_crop_data(url):
    df = pd.read_csv(url)
    df = df.rename(columns={
        'State_Name': 'state',
        'District_Name': 'district',
        'Crop_Year': 'year',
        'Season': 'season',
        'Crop': 'crop',
        'Area': 'area',
        'Production': 'production'
    })
    df['state'] = df['state'].str.strip().str.lower()
    df['district'] = df['district'].str.strip().str.lower()
    df['crop'] = df['crop'].str.strip().str.lower()
    return df

def get_rainfall_data(path):
    df = pd.read_excel(path)
    df = df.rename(columns={
        'STATE/UT': 'state',
        'DISTRICT': 'district'
    })
    df['state'] = df['state'].str.strip().str.lower()
    df['district'] = df['district'].str.strip().str.lower()
    return df