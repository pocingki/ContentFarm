import pandas as pd


def read_excel(path="data/upload.xlsx"):

    try:

        df = pd.read_excel(path)

        return df

    except Exception as e:

        print(e)

        return None