import pandas as pd
import matplotlib.pyplot as plt

# Citirea datelor din fișierul CSV
data = pd.read_csv('data.csv')
# Afișarea tuturor valorilor
print("Toate valorile:")
print(data)

# Afișarea primelor 6 valori
print("\nPrimele 6 valori:")
print(data.head(6))

# Eliminarea rândurilor cu valori lipsă în coloanele 'Durata' și 'Puls'
data_clean = data.dropna(subset=['Durata', 'Puls'])

# Afișarea ultimelor 6 valori pentru coloanele Durata și Puls
ultimele_6_valori = data_clean[['Durata', 'Puls']].tail(6)
print("\nUltimele 6 valori pentru Durata și Puls:")
print(ultimele_6_valori)

# Trasarea graficului pentru ultimele 6 valori valide pentru coloanele Durata și Puls
ultimele_6_valori.plot(x='Durata', y='Puls', kind='bar')
plt.xlabel('Durata')
plt.ylabel('Puls')
plt.title('Ultimele 6 valori valide pentru Durata și Puls')
plt.show()
