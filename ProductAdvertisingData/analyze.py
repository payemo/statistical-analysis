import pandas as pd
from tabulate import tabulate
import scipy.stats as stats

df = pd.read_excel("./ProductAdvertisingData/Advertising_Data.csv.xlsx")

data = df.apply(pd.to_numeric, errors='coerce')

results = {}

for col in data.columns:
    if col != "Product_Sold":
        col_data = data[col]

        mean = col_data.mean()
        variance = col_data.var()
        std_dev = col_data.std()

        correlation_with_product_sold = col_data.corr(data["Product_Sold"])

        shapiro_stat, p_value = stats.shapiro(col_data)
        normality = 'Normal Distribution' if p_value > 0.05 else 'Not Normal Distribution'

        results[col] = {
            "Mean": mean,
            "Variance": variance,
            "Std Deviation": std_dev,
            "Normality Test": normality
        }

# Jinja2 dependency
#styled_df = pd.DataFrame(results).T.style.set_caption("Statistical Analysis Results").background_gradient(cmap='coolwarm')

print(tabulate(pd.DataFrame(results).T, headers='keys', tablefmt='fancy_grid'))