import pandas as pd

def compare_states(df, crop, s1, s2, years):
    d1 = df[(df['state'] == s1) & (df['crop'] == crop) & (df['year'].isin(years))]
    d2 = df[(df['state'] == s2) & (df['crop'] == crop) & (df['year'].isin(years))]

    p1 = d1['production'].mean() if not d1.empty else None
    p2 = d2['production'].mean() if not d2.empty else None

    r1 = df[(df['state'] == s1)][['annual']].mean().iloc[0] if 'annual' in df.columns else None
    r2 = df[(df['state'] == s2)][['annual']].mean().iloc[0] if 'annual' in df.columns else None

    return p1, p2, r1, r2

def best_worst_district(df, crop, s1, s2, year):
    a = df[(df['state'] == s1) & (df['crop'] == crop) & (df['year'] == year)]
    b = df[(df['state'] == s2) & (df['crop'] == crop) & (df['year'] == year)]

    best = a.sort_values(by='production', ascending=False).head(1)
    worst = b.sort_values(by='production', ascending=True).head(1)

    return best, worst

def crop_trend(df, crop, state, yrs):
    d = df[(df['state'] == state) & (df['crop'] == crop) & (df['year'].isin(yrs))]
    d = d.groupby('year')['production'].sum().reset_index()
    return d

def policy_compare(df, crop_a, crop_b, state, yrs):
    a = df[(df['state'] == state) & (df['crop'] == crop_a) & (df['year'].isin(yrs))]
    b = df[(df['state'] == state) & (df['crop'] == crop_b) & (df['year'].isin(yrs))]

    pa = a.groupby('year')['production'].sum().mean() if not a.empty else 0
    pb = b.groupby('year')['production'].sum().mean() if not b.empty else 0

    ra = df[df['state'] == state]['annual'].mean() if 'annual' in df.columns else None

    return pa, pb, ra
