import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Set Seaborn style for professional appearance
sns.set_style("whitegrid")
sns.set_context("notebook", font_scale=1.2, rc={"lines.linewidth": 2.5})

# Generate realistic synthetic data for customer engagement metrics
np.random.seed(42)  # for reproducibility
metrics = [
    'Time on Site (min)', 'Pages Viewed', 'Session Frequency',
    'Add to Cart Rate', 'Purchase Conversion Rate', 'Customer Lifetime Value'
]

corr_matrix_data = np.array([
    [1.00,  0.75,  0.60,  0.40,  0.30,  0.20],
    [0.75,  1.00,  0.55,  0.45,  0.35,  0.25],
    [0.60,  0.55,  1.00,  0.50,  0.40,  0.30],
    [0.40,  0.45,  0.50,  1.00,  0.70,  0.60],
    [0.30,  0.35,  0.40,  0.70,  1.00,  0.85],
    [0.20,  0.25,  0.30,  0.60,  0.85,  1.00]
])

corr_df = pd.DataFrame(corr_matrix_data, columns=metrics, index=metrics)

# Set the figure size to 8x8 inches.
# When combined with dpi=64, this will produce a 512x512 pixel image.
plt.figure(figsize=(8, 8))

heatmap = sns.heatmap(
    corr_df,
    annot=True,
    cmap="YlGnBu",
    fmt=".2f",
    linewidths=0.5,
    cbar_kws={'label': 'Correlation Coefficient'}
)

plt.title('Customer Engagement Metrics Correlation Matrix', fontsize=16, pad=20)
plt.xlabel('Customer Engagement Metrics', fontsize=12, labelpad=15)
plt.ylabel('Customer Engagement Metrics', fontsize=12, labelpad=15)

# Save the figure. The `bbox_inches='tight'` parameter is essential
# for ensuring the final image dimensions are consistent.
plt.savefig('chart.png', dpi=64)

# plt.show() is optional and will display the plot in a window.
# You can comment it out if you only need the file.
plt.show()