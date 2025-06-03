
# Django Projekt – Spuštění a práce s aplikací

Tento projekt je vytvořen pomocí frameworku **Django**. Využívá databázi **MySQL** a běží ve **virtuálním prostředí**.

---

## 📋 Předpoklady

- Python 3.8 nebo vyšší
- MySQL server (nainstalovaný a běžící)
- `pip` (Python balíčkový manažer)
- `virtualenv` (pro práci s virtuálním prostředím)

---

## 🚀 Postup pro spuštění projektu

### 1. Stažení nebo klonování projektu

Pokud máš projekt v repozitáři:

```bash
git clone <url_adresa_repozitáře>
cd <název_složky_projektu>
```

---

### 2. Vytvoření a aktivace virtuálního prostředí

Vytvoření prostředí:

```bash
python -m venv venv
```

Aktivace prostředí:
- **Windows**:
  ```bash
  venv\Scripts\activate
  ```
- **Linux/macOS**:
  ```bash
  source venv/bin/activate
  ```

---

### 3. Instalace potřebných balíčků

Pokud máš `requirements.txt`:

```bash
pip install -r requirements.txt
```

Pokud ne:

```bash
pip install django mysqlclient
```

---

### 4. Nastavení připojení k databázi

V souboru `settings.py` nastav databázi:

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'nazev_databaze',
        'USER': 'uzivatel',
        'PASSWORD': 'heslo',
        'HOST': 'localhost',
        'PORT': '3306',
    }
}
```

---

### 5. Migrace databáze

```bash
python manage.py makemigrations
python manage.py migrate
```

---

### 6. (Volitelné) Vytvoření administrátorského účtu

```bash
python manage.py createsuperuser
```

Zadej uživatelské jméno, e-mail a heslo.

---

### 7. Spuštění vývojového serveru

```bash
python manage.py runserver
```

Aplikace bude dostupná na: [http://127.0.0.1:8000](http://127.0.0.1:8000)

---

## 💡 Poznámky

- Po změnách v `models.py` nezapomeň na:
  ```bash
  python manage.py makemigrations
  python manage.py migrate
  ```
- Pokud instaluješ nové knihovny:
  ```bash
  pip freeze > requirements.txt
  ```
- Při problémech s připojením k databázi zkontroluj přihlašovací údaje a zda běží MySQL server.

---

## ✍️ Autor

- **Jméno:** Jakub Bittner, Matěj Kupka  
- **Datum:** 03.06.2025
