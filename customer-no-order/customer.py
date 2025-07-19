import pandas as pd

def find_customers(customers: pd.DataFrame, orders: pd.DataFrame) -> pd.DataFrame:
    df1 = pd.merge(customers, orders, how='left', left_on='id', right_on='customerId')
    return df1.loc[df1['customerId'].isnull(), ['name']].rename(columns={'name': 'Customers'})