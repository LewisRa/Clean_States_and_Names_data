#Creating a new column with the sales increase from previous year


df['WeeklySalesPreviousYear'] = np.nan

for store in df.Store.unique():
    idx = df.Store==store
    a = df['WeeklySales'][idx].values
    a = np.roll(a,52) # shift by one year
    a[0:52] = np.nan
    df.loc[idx, 'WeeklySalesPreviousYear'] = a
    
df['WeeklySalesIncreaseRatio'] = df['WeeklySales'] / df['WeeklySalesPreviousYear']