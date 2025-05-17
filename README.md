# Biblioteka API

U ovom projektu je prikazana izrada web servera za upravljanje bibliotekom uz korišćenje Python framework-a **FastAPI**. Aplikacija je razvijena u skladu sa troslojnom arhitekturom UI-BL-DAL čime se postiže lakše održavanje i veća preglednost koda, kao i jasno razgraničavanje odgovornosti između slojeva. Za rad sa podacima je primenjen ORM model **SQLAlchemy** koji omogućava objektno-orijentisanu komunikaciju sa bazom podataka bez direktnog pisanja SQL upita, sami podaci se čuvaju u MySQL bazi podataka, dok su **Pydantic** modeli korišćeni za validaciju podataka pristiglih od korisnika i pretvaranje u formate koji su podržani od strane FastAPI-a. 

## 🛠️ Korišćene tehnologije u razvoju aplikacije

### 🚀 FastAPI 

> 💡 **Tip**  
> FastAPI je idealan framework ukoliko je potrebna mikroservisna arhitektura jer se lako integriše sa drugim alatima kao što su Docker i Celery

## Arhitektura aplikacije 
Sama aplikacija je organizovana u tri sloja: 
  1) UI (user interface) sloj - ovo je sloj koji predstavlja korisnički interfejs same aplikacije prema klijentima koji komuniciraju sa njom preko HTTP/HTTPS protokola. Glavni zadatak ovog sloja jeste implementiranje REST API ruta, prijem HTTP zahteva i slanje adekvatnih HTTP odgovora. Sem toga, UI obrađuje parametre (path, query, body i header) HTTP zahteva, validira ih i prosleđuje podatke sloju ispod sebe tj. sloju poslovne logije (BL). UI sloj, sam po sebi, ne treba da sadrži poslovnu logiku, već samo treba da bude posrednik koji je zadužen za komunikaciju između klijenta i unutrašnjih komponenti aplikacije.

  2) BL (business layer) sloj - ovo je sloj poslovne logike i predstavlja središnji nivo aplikacione arhitekture jer se nalazi između sloja korisničkog interfejsa i sloja za pristup podacima. Glavni zadatak ovog sloja je da obradi pristigle podatke i implementira pravila kojima se definiše ponašanje sistema - tzv. "poslovna logika".  Na primer, u ovom sloju će se obaviti provera ispunjenosti kriterijuma za iznajmljivanje knjiga, da li je knjiha dostupna itd. Sem toga, BL sloj transformiše podatke po potrebi i priprema odgovore koje potom delegira UI sloju. O
  
  3) DAL (data access layer) sloj - ovo je sloj za pristup podacima, pa samim tim je i zadužen za direktnu komunikaciju sa bazom podataka. U okviru njega se definišu CRUD (create, read, update, delete) operacije tj. operacije za kreiranje, čitanje, ažuriranje i brisanje. Ovaj sloj predstavlja apstrakciju nad samom bazom podataka što znači da sloj poslovne logike ne mora, a ni ne treba da zna tehničke detalje baze ili samih SQL upita. U ovoj aplikaciji, DAL koristi SQLAlchemy ORM koji omogućava efikasan, a pre svega tipski bezbedan rad sa MySQL bazom podataka. Sve operacije nad entitetima se nalaze u ovom sloju čime se izbegava replikacija koda i pojednostavljuje njegovo održavanje. 

Ovakva arhitektura aplikavicije omogućava jasnu podelu odgovornosti slojeva što značajno olakšava samo održavanje, testiranje, ali i skaliranje aplikacije jer se svaki sloj može nezavisno razvijati i menjati. Sem toga, ovakva struktura omogućava bolju preglednost koda i smanjuje rizik od grešaka. 



## Podešavanje okruženja
Za uspešno pokretanje projekta, potrebno je prethodno podesiti okruženje što podrazumeva podešavanje virtualnog okruženja, uvoz neophodnih zavisnosti tj. biblioteka i podešavanje radnog okruženja (produkciono/razvojno) 

### Instalacija zavisnosti
```{python}
python -m venv naziv-virtualnog-okruzenja
.\naziv-virtualnog-okruzenja\Scripts\Activate.ps1
pip install -r requirements.txt
```

> [!TIP]  
> Ukoliko ažurirate postojeće zavisnosti tj. biblioteke ili dodajete nove, možete ažurirati `requirements.txt` fajl sledećom komandom:  
>  
> ```bash  
> pip freeze > requirements.txt  
> ```

### Upravljanje okruženjem i konfiguracijom aplikacije
Česta praksa prilikom razvoja web aplikacija jeste razdvajanje razvojnog (development) i produkcionog (production) okruženja, a razlog za to je njihova različita namena. Razvojno okruženje se koristi kada je potrebno da se testiraju nove funkcionalnosti ili da se otklone uočene nepravilnosti u radu aplikacije, dok je produkciono okruženje namenjeno korisnicima i mora da bude stabilno i pouzdano. Ovakva praksa omogućava programerima da rade bez rizika od narušavanja rada aplikacije u realnom vremenu. Pored toga, oba okruženja uglavnom imaju različite konfiguracione parametre - pristup bazi, logovanje ili bezbedonosna podešavanja što doprinosi fleksibilnosti i sigurnosti u radu. 
