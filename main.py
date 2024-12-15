# Import libraries
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.datasets import fetch_openml

# Step 1: Select a Dataset
data = fetch_openml(name='iris', version=1, as_frame=True)

# Step 2: Inspect the Data
print(data.DESCR)
df = data.frame
print(df.head())
print("Sample data:")
print(df.sample(5))
print("Summary statistics:")
print(df.describe())
print("Data types:")
print(df.dtypes)

# Step 3: Select Features
features = list(df.columns)
print("Available features:", features)
selected_features = [features[0], features[2]]
print("Selected features: ", selected_features)

# Step 4: Make Histogram Plots
fig, axs = plt.subplots(1, len(selected_features), figsize=(20, 3))
for ax, f in zip(axs, selected_features):
    ax.hist(df[f], bins=5, color='skyblue', edgecolor='black')
    ax.set_xlabel(f)
plt.show()

# Step 5: Test Correlation with Scatter Plots
reference_feature = selected_features[1]
y = df[reference_feature]

fig, axs = plt.subplots(1, len(features), figsize=(20, 3))
for ax, f in zip(axs, features):
    ax.scatter(df[f], y)
    ax.set_xlabel(f)
plt.show()

# Step 6: Save a Selected Correlation Plot
reference_feature = selected_features[0]
comparison_feature = selected_features[1]

plt.figure(figsize=(8, 6))
plt.scatter(df[reference_feature], df[comparison_feature], alpha=0.6)
plt.xlabel(reference_feature)
plt.ylabel(comparison_feature)
plt.title("Correlation Plot: {} vs {}".format(reference_feature, comparison_feature))

# Save the plot
plt.savefig('correlation_plot.png')
plt.show()
