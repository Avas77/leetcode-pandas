import pandas as pd

def find_products(products: pd.DataFrame) -> pd.DataFrame:
    df1 = products[(products['low_fats'] == 'Y') & (products['recyclable'] == 'Y')]
    return df1[['product_id']]