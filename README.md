# 1. Wymagania
- Python 3.9.7
- virutalenv
- pip

# 2. Instalacja
Aby zainstalować aplikację musisz wykonać poniższe polecenia.

## Tworzenia enva
```
python3 -m venv env
```

## Uruchomienie enva w zależności od systemu

### Widnows
```
.\env\Scripts\activate
```

### Linux 
```
source env/bin/activate
```

Instalacja zależności:
```
pip install -r requirements.txt
```

## Uruchomienie migracji:

### Windows
```
python .\manage.py migrate
```

### Linux
```
python manage.py migrate
```

## Utworzenie admina
```
python manage.py createsuperuser
```

# 3. Uruchomienie

### Windows
```
python .\manage.py runserver
```

### Linux
```
python manage.py runserver
```
