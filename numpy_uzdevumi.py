import numpy as np

# 1. uzdevums - Paraugu blivums

# 1. Izveido masivus
masa_g = np.array([26.8, 27.4, 26.4, 27.1])
tilpums_cm3 = np.array([10.0, 10.0, 9.6, 10.0])

# 2. Aprēķini blivumu
blivums = masa_g / tilpums_cm3
print("Paraugu blīvums:", blivums)

# 3. Raksturo paraugus
print("Vidējais blīvums:", np.mean(blivums))
print("Mazākais blīvums:", np.min(blivums))
print("Lielākais blīvums:", np.max(blivums))

# 4. Atlasi paraugus
maska = blivums > 2.72
print("Maska:", maska)
print("Atlasītie blīvumi:", blivums[maska])
print("Paraugi B un C")




# 2. uzdevums - Temperatura krasni

# 1. Izveido 2D masivu
temperatura = np.array([
    [790, 810],
    [798, 806],
    [794, 808]
])

print("Temperatūras masīvs:")
print(temperatura)

print("Masīva izmērs:", temperatura.shape)
print("Cikls B pie durvīm:", temperatura[1, 0])

# 2. Aprēķini katra cikla videjo temperaturu
ciklu_videja = np.mean(temperatura, axis=1)
print("Ciklu vidējās temperatūras:", ciklu_videja)

# 3. Salidzini abas krasns vietas
videja_pie_durvim = np.mean(temperatura[:, 0])
videja_dziluma = np.mean(temperatura[:, 1])

starpiba = videja_dziluma - videja_pie_durvim

print("Vidējā temperatūra pie durvīm:", videja_pie_durvim)
print("Vidējā temperatūra dziļumā:", videja_dziluma)
print("Temperatūras starpība:", starpiba)
