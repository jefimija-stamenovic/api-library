# Library API
A modular and scalable REST API for managing a digital library, built with FastAPI.

Ovaj projekat predstavlja FastAPI aplikaciju za upravljanje bibliotekom. Funkcionalnosti aplikacije su: 
 - upravljanje korisnicima tj. čitaocimai i administratorima 
 - upravljanje publikacija
 - upravljanje iznajmljivanjima i vraćanjima publikacija

## Podešavanje okruženja
Za uspešno pokretanje projekta, potrebno je prethodno podesiti okruženje 
### Instalacija zavisnosti
```{python}
python -m venv naziv-virtualnog-okruzenja
.\naziv-virtualnog-okruzenja\Scripts\Activate.ps1
pip install -r requirements.txt
```

> [!NOTE]  
> Ukoliko ažurirate biblioteke ili dodajete nove, možete ažurirati `requirements.txt` fajl sledećom komandom:  
>  
> ```bash  
> pip freeze > requirements.txt  
> ```