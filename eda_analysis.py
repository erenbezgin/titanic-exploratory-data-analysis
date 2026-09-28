import pandas as pd
import seaborn as sns

def veri_yukle_ve_temizle():
    # Seaborn kütüphanesindeki Titanic veri setini çek 
    df = sns.load_dataset('titanic')
    print("Orijinal Veri Boyutu (Satır, Sütun):", df.shape)
    
    #  Aşırı boş olan 'deck' ve tekrar eden 'alive' sütunlarını kaldır
    df.drop(columns=['deck', 'alive'], inplace=True, errors='ignore')
    df['embark_town'] = df['embark_town'].fillna(df['embark_town'].mode()[0])
    
    # 2. Yaş sütunundaki eksikleri medyan değerine göre doldur
    medyan_yas = df['age'].median()
    df['age'] = df['age'].fillna(medyan_yas)
    
    # 3. Biniş limanı eksiklerini mod ile doldur doldur
    mod_liman = df['embarked'].mode()[0]
    df['embarked'] = df['embarked'].fillna(mod_liman)
    
    print("\nTemizleme Sonrası Eksik Değerler:")
    print(df.isnull().sum())
    return df

if __name__ == "__main__":
    df = veri_yukle_ve_temizle()