import pandas as pd


# 1. Nolasi datus

df = pd.read_csv("p6sieti1.csv")

print(df)


# 2. Aprēķini kopējo masu

kopeja_masa = df["masa_g"].sum()

print(f"Kopējā masa: {kopeja_masa:.1f} g")


# 3. Aprēķini frakciju masas procentus

df["masas_procents"] = df["masa_g"] / kopeja_masa * 100

print(df)

parbaude = df["masas_procents"].sum()

print("Procentu summa:", parbaude)


# 4. Saglabā rezultātu

df.to_csv(
    "p6rezultati.csv",
    index=False,
    float_format="%.1f"
)

print("Rezultāti saglabāti datnē p6rezultati.csv")

