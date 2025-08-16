import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Set Seaborn style and context for a professional look
sns.set_style("whitegrid")
sns.set_context("notebook", font_scale=1.2, rc={"lines.linewidth": 2.5})

# Generate realistic synthetic data for customer engagement metrics
np.random.seed(42)  # for reproducibility
metrics = [
    'Time on Site (min)', 'Pages Viewed', 'Session Frequency',
    'Add to Cart Rate', 'Purchase Conversion Rate', 'Customer Lifetime Value'
]

# Create a sample correlation matrix with realistic relationships
# We'll build a lower triangular matrix and fill it out
corr_matrix_data = np.array([
    [1.00,  0.75,  0.60,  0.40,  0.30,  0.20],
    [0.75,  1.00,  0.55,  0.45,  0.35,  0.25],
    [0.60,  0.55,  1.00,  0.50,  0.40,  0.30],
    [0.40,  0.45,  0.50,  1.00,  0.70,  0.60],
    [0.30,  0.35,  0.40,  0.70,  1.00,  0.85],
    [0.20,  0.25,  0.30,  0.60,  0.85,  1.00]
])

# Use pandas DataFrame to create the correlation matrix
corr_df = pd.DataFrame(corr_matrix_data, columns=metrics, index=metrics)

# Create the heatmap
plt.figure(figsize=(8, 8))  # Set figure size for 512x512 output

# Customize the heatmap for professional presentation
heatmap = sns.heatmap(
    corr_df,
    annot=True,          # Show correlation values on the heatmap
    cmap="YlGnBu",       # Use a professional color palette
    fmt=".2f",           # Format annotations to two decimal places
    linewidths=0.5,      # Add lines between cells for clarity
    cbar_kws={'label': 'Correlation Coefficient'}
)

# Add a title and labels
plt.title('Customer Engagement Metrics Correlation Matrix', fontsize=16, pad=20)
plt.xlabel('Customer Engagement Metrics', fontsize=12, labelpad=15)
plt.ylabel('Customer Engagement Metrics', fontsize=12, labelpad=15)

# Ensure the layout is tight and save the figure
# Setting dpi to 64 and figsize to (8,8) results in 512x512 pixels (8*64 = 512)
plt.savefig('chart.png', dpi=64, bbox_inches='tight')

plt.show()