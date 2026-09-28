import os
import matplotlib
matplotlib.use('Agg')  # Arayüz açmadan doğrudan dosyaya kaydetmeyi garanti eder
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

def veri_yukle_ve_temizle():
    # Seaborn kütüphanesindeki Titanic veri setini yükle[cite: 2]
    df = sns.load_dataset('titanic')
    print("Orijinal Veri Boyutu (Satır, Sütun):", df.shape)
    
    # Eksik veya tekrar eden sütunları temizle[cite: 2]
    df.drop(columns=['deck', 'alive'], inplace=True, errors='ignore')
    
    # Eksik değerleri doldur[cite: 2]
    df['embark_town'] = df['embark_town'].fillna(df['embark_town'].mode()[0])
    df['embarked'] = df['embarked'].fillna(df['embarked'].mode()[0])
    df['age'] = df['age'].fillna(df['age'].median())
    
    print("\nTemizleme Sonrası Eksik Değerler:")
    print(df.isnull().sum())
    return df

def analiz_et_ve_ciz(df):
    os.makedirs('grafikler', exist_ok=True)
    
    # Cinsiyet ve bilet sınıfına göre hayatta kalma oranları[cite: 2]
    print("\n=== Cinsiyete Göre Hayatta Kalma Oranı ===")
    print(df.groupby('sex')['survived'].mean())
    
    print("\n=== Bilet Sınıfına Göre Hayatta Kalma Oranı ===")
    print(df.groupby('pclass')['survived'].mean())
    
    # Grafik oluştur ve kaydet[cite: 2]
    plt.figure(figsize=(7, 5))
    sns.barplot(x='sex', y='survived', hue='pclass', data=df, palette='viridis')
    plt.title('Cinsiyet ve Bilet Sınıfına Göre Hayatta Kalma Oranı')
    plt.ylabel('Hayatta Kalma Oranı')
    plt.xlabel('Cinsiyet')
    plt.tight_layout()
    
    cikti_yolu = os.path.join('grafikler', 'hayatta_kalma_cinsiyet_sinif.png')
    plt.savefig(cikti_yolu, dpi=300)
    plt.close()
    print(f"\nGrafik başarıyla kaydedildi: {os.path.abspath(cikti_yolu)}")

if __name__ == "__main__":
    df = veri_yukle_ve_temizle()
    analiz_et_ve_ciz(df)