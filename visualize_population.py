import pandas as pd
import matplotlib.pyplot as plt

# Load the dataset
file_path = 'world_population.csv'
df = pd.read_csv(file_path)

# Create a bar chart to visualize the distribution of ages
plt.figure(figsize=(10, 6))
plt.bar(df['Age'], df['Population'], color='skyblue')
plt.xlabel('Age Group')
plt.ylabel('Population')
plt.title('Distribution of Ages in Population')
plt.xticks(rotation=45, ha='right')  # Rotate x-axis labels for better readability
plt.tight_layout()  # Adjust layout to prevent clipping of labels
plt.show()
