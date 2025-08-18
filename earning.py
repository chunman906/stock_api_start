import pandas as pd
from api_data import get_income_statement

def analyze_earnings():
    data = get_income_statement()
    df = pd.DataFrame(data)
    df['revenue_growth_yoy'] = df['revenue'].pct_change(periods=-1) * 100
    df['net_income_growth_yoy'] = df['netIncome'].pct_change(periods=-1) * 100
    df['profit_margin'] = (df['netIncome'] / df['revenue']) * 100
    return df[['date', 'revenue', 'netIncome', 'revenue_growth_yoy', 'net_income_growth_yoy', 'profit_margin']]

print(analyze_earnings())
