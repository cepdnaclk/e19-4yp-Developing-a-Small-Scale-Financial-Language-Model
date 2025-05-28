import pdfplumber
import pandas as pd
import matplotlib.pyplot as plt

all_tables = []

with pdfplumber.open("Financial Statement 2023-2024.pdf") as pdf:
    for page in pdf.pages:
        tables = page.extract_tables()
        for table in tables:
            df = pd.DataFrame(table[1:], columns=table[0])
            all_tables.append(df)

for i, df in enumerate(all_tables):
    df.to_csv(f"table_{i+1}.csv", index=False)

if len(all_tables) > 0:
    df = all_tables[0]
    print(df.head())  # Check column names
    df = df.dropna()
    df['Revenue'] = df['Revenue'].replace('[\$,]', '', regex=True).astype(float)
    df.plot(kind='bar', x='Year', y='Revenue', title="Yearly Revenue")
    plt.tight_layout()
    plt.show()
