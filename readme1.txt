# Problema 1: Moștenirea claselor în Python - Employee și Manager

Acest fișier conține o soluție pentru problema 1, care implică crearea unei clase Manager care moștenește clasa Employee, și implementează anumite funcționalități specifice.

## Descrierea Problemei

- Se consideră un fișier `employee.py` care conține clasa `Employee`.
- Problema implică extinderea clasei `Employee` prin crearea clasei `Manager` care să aibă anumite funcționalități adiționale.
- Cerințele includ crearea de obiecte Manager, modificarea metodei de afișare a angajaților și gestionarea numărului de obiecte create pentru Manager.

## Soluție

1. **Moștenirea claselor:**
   - Clasa `Manager` moștenește clasa `Employee` pentru a beneficia de funcționalitățile și atributele acesteia.

2. **Variabila de clasă pentru numărul de obiecte Manager:**
   - Folosim o variabilă de clasă `mgr_count` pentru a urmări numărul de obiecte create din clasa Manager.

3. **Constructorul clasei Manager:**
   - Constructorul clasei `Manager` primește trei argumente: `name`, `salary` și `department`, unde numele departamentului este prefixat cu "D5".

4. **Metoda de afișare `display_employee` în clasa Manager:**
   - Metoda `display_employee` din clasa `Manager` afișează doar numele angajatului.

5. **Crearea obiectelor și apelarea metodelor:**
   - Sunt create două obiecte ale clasei `Manager`.
   - Se apelează metoda `display_employee` pentru toate obiectele din clasele `Manager` și `Employee`.

6. **Afișarea valorii atributului emp_count:**
   - Valorile atributului `emp_count` sunt afișate pentru o instanță a clasei `Employee` și pentru o instanță a clasei `Manager`.

## Cum să folosești codul

- Pentru a folosi acest cod, ai nevoie de fișierul `employee.py`.
- Creează o instanță a clasei `Manager` și apelează metodele corespunzătoare pentru a observa funcționarea soluției.

## Structura codului
- Fișierul `employee.py` conține definita clasei `Employee` și poate fi extins pentru a implementa soluția pentru problema 1.

