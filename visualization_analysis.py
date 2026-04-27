"""
Visualization Analysis for Test Dataset
Author: [Chaika Maksim]
"""

import pandas as pd
import matplotlib.pyplot as plt
import os

DATA_PATH = "data/test_dataset.csv"
OUTPUT_DIR = "output/figures"

os.makedirs(OUTPUT_DIR, exist_ok=True)

df = pd.read_csv(DATA_PATH)
df = df.sort_values(['company_id', 'year'])

df['net_margin'] = df['net_profit'] / df['revenue']
df['tax_rate'] = df['taxes_paid'] / df['operating_profit']
df['revenue_growth'] = df.groupby('company_id')['revenue'].pct_change()
df['headcount_growth'] = df.groupby('company_id')['headcount'].pct_change()

plt.figure()
df.boxplot(column='net_margin', by='industry')
plt.title('Margin Distribution by Industry')
plt.suptitle('')
plt.savefig(f"{OUTPUT_DIR}/margin_by_industry.png")
plt.close()

plt.figure()
plt.scatter(df['revenue_growth'], df['headcount_growth'])
plt.axvline(x=1, linestyle='--')
plt.axhline(y=0.1, linestyle='--')
plt.savefig(f"{OUTPUT_DIR}/growth_vs_headcount.png")
plt.close()

plt.figure()
plt.scatter(df['net_margin'], df['tax_rate'])
plt.axvline(x=0.5, linestyle='--')
plt.axhline(y=0.1, linestyle='--')
plt.savefig(f"{OUTPUT_DIR}/margin_vs_tax.png")
plt.close()

founder_counts = df.groupby('founder_id')['company_id'].nunique()
plt.figure()
founder_counts.sort_values(ascending=False).head(20).plot(kind='bar')
plt.savefig(f"{OUTPUT_DIR}/founder_distribution.png")
plt.close()

address_counts = df.groupby('address_hash')['company_id'].nunique()
plt.figure()
address_counts.sort_values(ascending=False).head(20).plot(kind='bar')
plt.savefig(f"{OUTPUT_DIR}/address_distribution.png")
plt.close()

print("All visualizations saved.")
