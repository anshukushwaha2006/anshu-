import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import pandas as pd

sns.set_style("whitegrid")
plt.rcParams['figure.figsize'] = (12, 5)

np.random.seed(42)
n = 500

ages = np.random.normal(loc=35, scale=12, size=n)
ages = np.clip(ages, 18, 80).astype(int)  # constrain to adult range

genders = np.random.choice(['Female', 'Male', 'Non-binary'], size=n, p=[0.48, 0.48, 0.04])
df = pd.DataFrame({'Age': ages, 'Gender': genders})

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 5))

#  Histogram: Age distribution
ax1.hist(df['Age'], bins=15, color='royalblue', edgecolor='black', alpha=0.7)
ax1.set_title('Age Distribution in Population', fontsize=14, fontweight='bold')
ax1.set_xlabel('Age (years)', fontsize=12)
ax1.set_ylabel('Frequency (number of people)', fontsize=12)
ax1.axvline(df['Age'].mean(), color='red', linestyle='dashed', linewidth=1.5, label=f'Mean: {df["Age"].mean():.1f}')
ax1.axvline(df['Age'].median(), color='green', linestyle='dashed', linewidth=1.5, label=f'Median: {df["Age"].median():.1f}')
ax1.legend()

#  Bar chart: Gender distribution
gender_counts = df['Gender'].value_counts()
bars = ax2.bar(gender_counts.index, gender_counts.values, color=['yellow','darkgreen','orange'], 
               edgecolor='black', alpha=0.7)
ax2.set_title('Gender Distribution in Population', fontsize=14, fontweight='bold')
ax2.set_xlabel('Gender', fontsize=12)
ax2.set_ylabel('Count (number of people)', fontsize=12)


for bar in bars:
    height = bar.get_height()
    ax2.text(bar.get_x() + bar.get_width()/2., height + 3,
             f'{int(height)}', ha='center', va='bottom', fontsize=11)


plt.tight_layout()
plt.suptitle('Population Demographics Visualization', fontsize=16, y=1.02, fontweight='bold')
plt.show()

print("\n--- Summary Statistics ---")
print(f"Age - Mean: {df['Age'].mean():.1f}, Median: {df['Age'].median():.1f}, Std: {df['Age'].std():.1f}")
print(f"Age range: {df['Age'].min()} to {df['Age'].max()} years")
print("\nGender distribution:")
print(df['Gender'].value_counts())
