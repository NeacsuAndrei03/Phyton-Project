# Problema 2: Importul și vizualizarea datelor din fișierul CSV

Acest proiect implică importul datelor dintr-un fișier CSV și realizarea unei afișări grafice a acestora folosind Python.

## Descrierea Problemei

- Se consideră un fișier `data.csv` care conține date.
- Scopul problemei este să importăm aceste date într-un mediu Python și să le vizualizăm sub diferite forme.

## Soluție

1. **Importul datelor:**
   - Se folosește biblioteca Pandas pentru a citi datele din fișierul CSV (`data.csv`) și a le încărca într-un cadru de date.

2. **Afișarea tuturor valorilor:**
   - Se afișează toate valorile din fișierul CSV.

3. **Afișarea primelor 6 valori:**
   - Se afișează primele 6 valori din fișierul CSV pentru a oferi o privire rapidă asupra datelor.

4. **Procesarea datelor:**
   - Se elimină rândurile care conțin valori lipsă (NaN) în coloanele 'Durata' și 'Puls'.

5. **Afișarea ultimelor 6 valori pentru coloanele Durata și Puls:**
   - Se afișează ultimele 6 valori valabile din coloanele 'Durata' și 'Puls' din fișierul CSV.

6. **Trasarea graficului:**
   - Se trasează un grafic de bare pentru ultimele 6 valori valide ale coloanelor 'Durata' și 'Puls'.

## Cum să folosești codul

- Ai nevoie de fișierul `data.csv` pentru a rula codul.
- Asigură-te că ai bibliotecile Pandas și Matplotlib instalate în mediul tău Python.

## Structura codului

- Codul Python importă datele din fișierul CSV și utilizează Pandas pentru a le manipula și afișa grafic folosind Matplotlib.

