import requests
import pandas as pd
import matplotlib.pyplot as plt

# 1. Iegūsti datus no servera

url = "https://raw.githubusercontent.com/okskola/matinz/refs/heads/main/W4/gaisa_sildisana.json"

atbilde = requests.get(url, timeout=30)
atbilde.raise_for_status()
dati = atbilde.json()

# 2. Izveido mērījumu tabulu

masa_g = dati["mass_g"]
df = pd.DataFrame(dati["measurements"])

print(df.head())

# 3. Aprēķini blīvumu katrā mērījumā

df["density_g_cm3"] = masa_g / df["volume_cm3"]

print(df.head())

# 4. Uzzīmē grafiku

df.plot(
    x="temperature_C",
    y="density_g_cm3",
    marker="o",
    linestyle="None",
    xlabel="Temperatūra (°C)",
    ylabel="Blīvums (g/cm³)",
    title="Gaisa blīvums atkarībā no temperatūras"
)

plt.show()
