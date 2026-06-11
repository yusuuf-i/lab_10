import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

# Veri setini içe aktarma
dataset_path = os.path.join(os.path.dirname(__file__), 'Social_Network_Ads.csv')
dataset = pd.read_csv(dataset_path)

print("--- EDA (Exploratory Data Analysis) Raporu ---")

# 1. Veri setinin ilk 5 satırı
print("\nVeri Setinin İlk 5 Satırı:")
print(dataset.head())

# 2. Veri seti bilgileri (Değişken tipleri ve eksik veri durumu)
print("\nVeri Seti Bilgileri:")
print(dataset.info())

# 3. İstatistiksel özet
print("\nİstatistiksel Özet:")
print(dataset.describe())

# 4. Eksik veri kontrolü
print("\nEksik Veri Kontrolü:")
print(dataset.isnull().sum())

# Görselleştirme
sns.set_theme(style="whitegrid")

# a. Hedef Değişken (Purchased) Dağılımı
plt.figure(figsize=(6, 4))
sns.countplot(x='Purchased', data=dataset, palette='Set2')
plt.title('Satın Alma Durumu Dağılımı (0: Hayır, 1: Evet)')
plt.savefig('eda_purchased_distribution.png')
print("\n'eda_purchased_distribution.png' grafiği kaydedildi.")

# b. Yaş Dağılımı
plt.figure(figsize=(8, 5))
sns.histplot(dataset['Age'], kde=True, color='blue', bins=20)
plt.title('Kullanıcı Yaş Dağılımı')
plt.savefig('eda_age_distribution.png')
print("'eda_age_distribution.png' grafiği kaydedildi.")

# c. Maaş Dağılımı
plt.figure(figsize=(8, 5))
sns.histplot(dataset['EstimatedSalary'], kde=True, color='green', bins=20)
plt.title('Tahmini Maaş Dağılımı')
plt.savefig('eda_salary_distribution.png')
print("'eda_salary_distribution.png' grafiği kaydedildi.")

# d. Yaş ve Maaş İlişkisi (Satın Almaya Göre Renklendirilmiş)
plt.figure(figsize=(10, 6))
sns.scatterplot(x='Age', y='EstimatedSalary', hue='Purchased', data=dataset, palette='Set1', alpha=0.8)
plt.title('Yaş ve Maaş İlişkisinin Satın Alma Durumuna Göre Dağılımı')
plt.savefig('eda_age_salary_scatter.png')
print("'eda_age_salary_scatter.png' grafiği kaydedildi.")

print("\nEDA tamamlandı. Veri setinin genel özellikleri ve değişkenler arası ilişkiler analiz edildi.")
