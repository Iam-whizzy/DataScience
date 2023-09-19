import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Read the CSV file
data = pd.read_csv("https://modcom.co.ke/datasets/bank.csv")

sns.countplot(data['Gender'], palette = 'Reds')
plt.title("Distribution of Gender Status")
plt.xlabel('Gender')
plt.ylabel('Number of Members')

