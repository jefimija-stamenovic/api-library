
# 📕 Biblioteka API
![68747470733a2f2f666173746170692e7469616e676f6c6f2e636f6d2f696d672f6c6f676f2d6d617267696e2f6c6f676f2d7465616c2e706e67](https://github.com/user-attachments/assets/36d292dc-f290-473e-b2d7-03d9a1f22591)
## 📝 Opis projekta

> [!NOTE]
> Projekat je kreiran u okviru seminarskog rada na predmetu **Napredno softversko inženjerstvo** na master akademskim studijama Elektronskog fakulteta Univerziteta u Nišu, smer Računarstvo i informatika, modul Softversko inženjerstvo. 

Repozitorijum sadrži implementaciju REST API servisa razvijenog uz pomoć **FastAPI** *framework*-a. Cilj projekta je da se prikaže praktična primena savremenih *backend* tehnologija baziranih na asinhronom radu, tipskoj bezbednosti i automatskoj validaciji podataka. 

U ovom projektu je prikazana izrada REST API servisa za upravljanje bibliotekom. Servis je razvijen u skladu sa troslojnom arhitekturom UI-BL-DAL, za rad sa podacima je primenjen ORM model **SQLAlchemy**, podaci se čuvaju u MySQL bazi podataka, dok su **Pydantic** modeli korišćeni za validaciju podataka pristiglih od korisnika i pretvaranje u formate koji su podržani od strane **FastAPI**-a. 

## 📙Sadržaj
- [📕 Biblioteka API](#-biblioteka-api)
  - [📝 Opis projekta](#-opis-projekta)
  - [📙Sadržaj](#sadržaj)
  - [💡Šta je FastAPI?](#šta-je-fastapi)
  - [❓ Koji problemi se rešavaju?](#-koji-problemi-se-rešavaju)
  - [🚀 Zašto baš FastAPI?](#-zašto-baš-fastapi)
  - [✅❌ Prednosti i mane](#-prednosti-i-mane)
  - [🔁 Konkurentna rešenja](#-konkurentna-rešenja)
  - [🛠️ Ostale korišćene tehnologije u razvoju aplikacije](#️-ostale-korišćene-tehnologije-u-razvoju-aplikacije)
    - [🦄 Uvicorn](#-uvicorn)
    - [🧩 Pydantic](#-pydantic)
    - [🔗 SQLAlchemy](#-sqlalchemy)
    - [📦 Alembic](#-alembic)
  - [✳️ Arhitektura aplikacije](#️-arhitektura-aplikacije)
  - [⚙️ Pokretanje projekta](#️-pokretanje-projekta)
    - [✅ 1. Kloniranje repoziturijuma](#-1-kloniranje-repoziturijuma)
      - [Struktura projekta](#struktura-projekta)
    - [📦 2. Podešavanje virtuelnog okruženja](#-2-podešavanje-virtuelnog-okruženja)
    - [📄 3. Instalacija zavisnosti](#-3-instalacija-zavisnosti)
    - [📄 4. Pokretanje aplikacije](#-4-pokretanje-aplikacije)
    - [Upravljanje okruženjem i konfiguracijom aplikacije](#upravljanje-okruženjem-i-konfiguracijom-aplikacije)
    - [Pokretanje aplikacije](#pokretanje-aplikacije)
  - [📄 Dokumentacija API-ja: Swagger i ReDoc](#-dokumentacija-api-ja-swagger-i-redoc)
    - [SwaggerUI](#swaggerui)
    - [ReDoc](#redoc)
    - [Konfiguracija Swagger i ReDoc dokumentacije](#konfiguracija-swagger-i-redoc-dokumentacije)
  - [Data Access Layer =\> repositories](#data-access-layer--repositories)
  - [Business Layer =\> services](#business-layer--services)
  - [User Interface Layer =\> api](#user-interface-layer--api)
  - [🔒 Zaključak](#-zaključak)
  - [📚 Literatura](#-literatura)

## 💡Šta je FastAPI? 
**FastAPI** je moderan i brz Python web *framework* namenjen brzom i jednostavnom pravljenju REST API servisa. Pruža sve što je potrebno za razvoj savremenih API-ja - od definisanja ruta i obrade podataka, pa do vraćanja odgovora klijentu i rukovanja greškama. 
Razvijen je na osnovu standardnih specifikacija poput OpenAPI-ja i JSON Schema-e. Takođe je baziran i na ASGI standardu, što znači da je moguć asinhroni način rada, odnosno, može da obrađuje više zahteva istovremeno što je značajno za performanse. 

## ❓ Koji problemi se rešavaju? 
**FastAPI** je razvijen kao odgovor na konkretne izazove u razvoju savremenih web servisa, gde je poseban akcenat stavljen na brzinu, pouzdanost i jednostavan razvoj. Ključni problemi koje rešava su: 
 - **Manuelna validacija podataka** - uz podršku biblioteke *Pydantic*, omogućena je automatska validacija ulaznih i izlaznih podataka. Time se eliminiše potreba za ručnim pisanjem logike gde se proverava ispravnost podataka, pa samim tim dolazi i do smanjenja koda i smanjenja mogućnosti za nastanak grešaka. 
 - **Nedostatak dokumentacije** - **FastAPI** automatski generiše potpunu i interaktivnu dokumentaciju u grafičkom okruženju koristeći Swagger i ReDoc na osnovu definisanih ruta i tipova. 
 - **Paralelna obrada zahteva** - **FastAPI** pruža podršku za asinhroni rad (*async/await*) što omogućava efikasno korišćenje resursa čak i u aplikacijama koje imaju potrebu za obradu velikog broja istovremenih zahteva
 - **Nedostatak kontrole nad strukturom podataka** - za razliku od nekih drugih tradicionalnih *framework*-ova, **FastAPI** nudi mogućnost eksplicitnog definisanja strukture podataka kroz tipove čime se omogućava automatska validacija i rano otkrivnje grešaka koje bi inače bile uočene tek u produkciji. 

## 🚀 Zašto baš FastAPI? 
1. **Izuzetne performanse** - **FastAPI** omogućava razvoj aplikacija sa asinhronim modelom izvršavanja što obezbeđuje efikasnu obradu velikog broja istovremenih zahteva bez ugrožavanja performansi 
2. **Smanjenje obima koda** - zahvaljujući ugrađenim mehanizmima za automatsku validaciju podataka i generisanje interaktivne dokumentacije, smanjuje se potreba za pisanjem koda što ujedno znači i ubrzavanje razvoja 
3. **Precizna i transparentna struktura podataka** - pošto **FastAPI** koristi jasno definisane tipove i Pydantic modele, to znači da je struktura podataka precizna i transparentna, pa je samim tim održavanje koda lakše
4. **Fleksibilnost** - zahvaljujući svom dizajnu, **FastAPI** se lako prilagođava i manjim i većim projektima što omogućava da bude korišćen u različitim poslovnim kontekstima
5. **Aktivna zajednica i održavanje** - **FastAPI** ima aktivnu zajednicu sačinjenu od korisnika i programera, kao i redovna ažuriranja što garantuje stabilnost **FastAPI**-ja i njegovo kontinuirano unapređivanje u vidu uvođenja novih funkcija 

## ✅❌ Prednosti i mane

| Kriterijum        | Prednosti                                                              | Mane                                                                 |
|-------------------|------------------------------------------------------------------------|----------------------------------------------------------------------|
| 🎯 Performanse     | Veoma brz zbog ASGI protokola i asinhronog načina rada                | Asinhrono programiranje može biti izazov za početnike                |
| 📄 Dokumentacija   | Generiše se automatski i uvek ažurna sa kodom                         | Za specifične i kompleksne domene može da bude neoptimalna           |
| 💡 Razvoj          | Visok stepen produktivnosti zbog automatske validacije i tipizacije   | Manje dostupnih tutorijala i primera u poređenju sa starijim alatima |
| 📈 Skalabilnost    | Fleksibilan za male i velike projekte, lako se prilagođava potrebama  | Za veoma velike sisteme može zahtevati dodatne optimizacije          |


## 🔁 Konkurentna rešenja 

| Tehnologija   | Podrška za asinhroni rad  | Automatska validacija | Ugrađena dokumentacija | Tipska bezbednost |
|---------------|---------------------------|-----------------------|------------------------|-------------------|
| FastAPI       | ✅                       | ✅                    | ✅                    | ✅                |
| Flask         | ❌ (moguće uz dodatke)   | ❌                    | ❌                    | ❌                |
| Django REST   | ⚠️ ograničeno            | ✅                    | ✅                    | ✅                |
| Tornado       | ✅                       | ❌                    | ❌                    | ⚠️ ograničeno     |
| Sanic         | ✅                       | ❌                    | ❌                    | ❌                |
| Falcon        | ✅                       | ❌                    | ❌                    | ⚠️ ograničeno     |

- **FastAPI** se izdvaja kao jedini *framework* koji ispunjava sve potrebne ključne kriterijume za razvoj savremenih i pouzdanih API-ja. Nudi mogućnost asinhronog načina rada, validacija podataka i kreiranje dokumentacije je automatizovano i tipizacija podataka je precizna što sve doprinosi brzini razvoja i smanjenju grešaka
- Iako je Flask izuzetno fleksibilan i jednostavan za korišćenje, on nema ugrađenu podršku za asinhroni način rada i automatsku obradu validacije i kreiranje dokumentacije, pa bi za te funkcionalnosti morale da se koriste dodatne biblioteke
- Django REST ima pouzdanu i sveobuhvatnu podršku za validaciju i dokumentaciju, ali je asinhroni način rada ograničen i zahteva dodatne korake koji mogu dovesti do usporavanja razvoja, naročito kod aplikacija sa velikim brojem istovremenih zahteva. 
- Tornado, Sanic i Falcon se fokusiranju na obezbeđivanje brzine i asinhrono procesiranje zahteva, ali nemaju ugrađene mehanizme za automatsku validaciju podataka i dokumentaciju, niti pružaju isti nivo tipske bezbednosti 

## 🛠️ Ostale korišćene tehnologije u razvoju aplikacije

### 🦄 Uvicorn 
**Uvicorn** je ASGI (Asynchronous Server Gateway Interface) server koji se koristi za pokretanje **FastAPI** aplikacije. Osnovni zadatak Uvicorn-a je prijem HTTP zahteva poslatih od strane klijenta i njihovo prosleđivanje aplikaciji. Pošto radi po ASGI standardu, to znači da je moguć asinhroni rad tj. aplikacija može istovremeno da obrađuje više paralelnih zahteva, a da ne dođe do blokiranja. 

> [!IMPORTANT]
> Uvicorn je zvanično preporučen server za **FastAPI** aplikacije zbog svoje brzine i podrške za asinhroni rad. S obzirom da minimalno troši resurse, a brzo odgovara na klijentske zahteve, idealan je za upotrebu i u razvojnom i u produkcionom okruženju, posebno ako se radi o sistemima koji zahtevaju visok stepen paralelne obrade podataka. 

### 🧩 Pydantic
**Pydantic** je Python biblioteka koja se koristi za definisanje modela podataka i njihovu automatsku proveru. Ova biblioteka omogućava da se na jednom mestu jasno opiše kako neki podatak treba da izgleda - kog je tipa, da li je obavezan i koja mu je podrazumevana vrednost. Kada aplikacija primi HTTP zahtev od strane klijenta, ona koristi Pydantic modele da bi proverila da li su pristigli podaci ispravni. Ukoliko nisu, klijent dobija HTTP odgovor sa statusom 422 i detaljnim objašnjenjem gde je došlo do greške. 

> [!IMPORTANT]
> Jedna od glavnih prednosti Pydantic-a je ta što se isti model može upotrebiti i za validiranje ulaznih podataka i za formatiranje odgovora koji se šalje klijentu. Time se obezbeđuje doslednost u strukturi podataka, ne dolazi do dupliranja logike, a ujedno se pojednostavljuje održavanje i testiranje celokupne aplikacije. 

### 🔗 SQLAlchemy
**SQLAlchemy** je Python biblioteka koja služi za rad sa bazama podataka kroz objektno-orijentisani pristup. Ova biblioteka je najčešće korišćeni ORM (Object-Relational Mapping) alat u Python-u i omogućava da se klase definisane u Python-u mapiraju na tabele u bazi podataka. Umesto ručnog pisanja SQL upita, nad podacima se mogu sprovesti CRUD (create-read-update-delete) operacije tj. dodavanje, čitanje, ažuriranje i brisanje preko Python objekata. Ovim se značajno olakšava rad nad podacima, smanjuje se mogućnost za nastanak grešaka i pojednostavljuje se logika unutar aplikacije. 

> [!NOTE]
> Iako je ORM glavni način rada sa podacima, SQLAlchemy podržava i manuelno pisanje SQL upita. Ovakva fleksibilnost je značajna kod aplikacija koje imaju specifične ili složene upite. 
> SQLAlchemy je fleksibilan pa tako omogućava da se složeni upiti pišu manuelno kada je to potrebno, ali i da se većina operacija obavlja kroz objektni model. Ovim se pojednostavljuje razvoj i unapređuje čitljivost koda. 

### 📦 Alembic 
**Alembic** je alat za migraciju baza podataka u Python okruženju i najčešće se koristi u kombinaciji sa SQLAlchemy biblotekom. Obezbeđuje praćenje i kontrolisano uvođenje izmena u strukturu baze podataka tokom razvoja aplikacije bez rizika od grešaka koje mogu da nastanu kao posledica manuelnog ažuriranja. 
Izmene se opisuju u vidu migracija tj. Python datoteka čiji sadržaj čine instrukcije za dodavanja, modifikovanje ili brisanje tabela ili kolona. Alembic funkcioniše tako što upoređuje trenutno stanje baze podataka sa stanjem koje je definisano SQLAlchemy modelima. Nakon utvrđivanja razlika, Alembic generiše migraciju kojom usklađuje bazu sa novim modelom čime se obezbeđuje da struktura baze podataka ostane usklađena sa logikom aplikacije tokom njenog razvoja. 

> [!IMPORTANT]
> Alembic značajno pojednostavljuje održavanje baze tokom razvoja, a razlog za to je što se umesto ručnog ažuriranja šeme primenjuju sve izmene preko verzionisanih migracija, uz mogućnost vraćanja na prethodno stanje ukoliko je potrebno. 

## ✳️ Arhitektura aplikacije 
Sama aplikacija je organizovana u tri sloja: 
  1) **UI (user interface) sloj** - ovaj sloj predstavlja korisnički interfejs same aplikacije prema klijentima koji komuniciraju sa njom preko HTTP/HTTPS protokola. Glavni zadatak ovog sloja jeste implementiranje REST API ruta, prijem HTTP zahteva i slanje adekvatnih HTTP odgovora. Sem toga, UI obrađuje parametre (path, query, body i header) HTTP zahteva, validira ih i prosleđuje podatke sloju ispod sebe tj. sloju poslovne logike (BL). UI sloj, sam po sebi, ne treba da sadrži poslovnu logiku, već samo treba da bude posrednik koji je zadužen za komunikaciju između klijenta i unutrašnjih komponenti aplikacije.

  2) **BL (business layer) sloj** - sloj poslovne logike predstavlja središnji nivo aplikacione arhitekture jer se nalazi između sloja korisničkog interfejsa i sloja za pristup podacima. Glavni zadatak ovog sloja je da obradi pristigle podatke i implementira pravila kojima se definiše ponašanje sistema. Na primer, u ovom sloju će se obaviti provera ispunjenosti kriterijuma za iznajmljivanje knjiga, da li je knjiga dostupna itd. Sem toga, BL sloj po potrebi transformiše podatke i priprema odgovore koje potom delegira UI sloju.
  
  3) **DAL (data access layer) sloj** - ovo je sloj za pristup podacima, pa samim tim je zadužen za direktnu komunikaciju sa bazom podataka. U okviru njega se definišu CRUD (create, read, update, delete) operacije tj. operacije za kreiranje, čitanje, ažuriranje i brisanje. DAL sloj predstavlja apstrakciju nad samom bazom podataka što znači da sloj poslovne logike ne mora, a ni ne treba da zna tehničke detalje baze ili samih SQL upita. U ovoj aplikaciji, DAL koristi SQLAlchemy ORM koji omogućava efikasan, a pre svega tipski bezbedan rad sa MySQL bazom podataka. Sve operacije nad entitetima se nalaze u ovom sloju čime se izbegava replikacija koda i pojednostavljuje njegovo održavanje. 

👉 Kratak pregleda funkcija slojeva:  
| Sloj  | Funkcija                           | Primer u FastAPI-ju                                            |
|-------|------------------------------------|----------------------------------------------------------------|
| UI    | Interfejs ka korisniku (API rute)  | rute, request handler-i                                        |
| BL    | Obrada podataka, poslovna logika   | servisni sloj, Pydantic klase i funkcije koje obrađuju podatke |
| DAL   | Komunikacija sa bazom podataka     | SQLAlchemy modeli i upiti, CRUD функције                       |

Ovakva arhitektura aplikacije omogućava jasnu podelu odgovornosti slojeva što značajno olakšava samo održavanje, testiranje, ali i skaliranje aplikacije jer se svaki sloj može nezavisno razvijati i menjati. Sem toga, ovakva struktura omogućava bolju preglednost koda i smanjuje rizik od nastanka grešaka. 

## ⚙️ Pokretanje projekta
Za uspešno pokretanje projekta, potrebno je prethodno podesiti okruženje što podrazumeva podešavanje virtualnog okruženja, uvoz neophodnih zavisnosti tj. biblioteka i podešavanje radnog okruženja (produkciono/razvojno). 

### ✅ 1. Kloniranje repoziturijuma 
Ovaj projekat se nalazi na *Github*-u, pa je prvi korak ka pokretanju projekta njegovo preuzimanje na lokalni računar putem komande: 

> [!WARNING]
> Pre nego što pokušate da preuzmete projekat koristeći komandu ispod, proverite da li na računaru imate instaliran Git CLI. Bez njega, komanda **git clone** neće biti prepoznata i preuzimanje repozitorijuma neće biti moguće 

```{bash}
  git clone https://github.com/jefimija-stamenovic/api-library.git
  cd api-library
```
#### Struktura projekta 
Nakon kloniranja projekta, klonirani projekat bi trebalo da ima sledeću strukturu: 

```{bash} 
  api-library/
  ├── app/
  │   ├── api/           # UI => rute
  │   ├── services/      # BL => servisi sa poslovnom logikom
  │   ├── repositories/  # DAL => rad sa bazom podataka
  │   ├── models/        # SQLAlchemy modeli
  │   ├── schemas/       # Pydantic šeme
  │   ├── core/          # Učitavanje konfiguracija, pomoćne funkcije i sl.  
  │   └── main.py        # Glavni fajl
  ├── requirements.txt   # Potrebne biblioteke 
  ├── .env               # Podešavanje okruženja
  │   ├── prod.env       # Podešavanja za produkciono okruženje 
  │   └── dev.env        # Podešavanja za razvojno okruženje 
  ├── alembic.ini
  └── README.md
```

### 📦 2. Podešavanje virtuelnog okruženja 

```{bash}
python -m venv naziv-virtualnog-okruzenja
.\naziv-virtualnog-okruzenja\Scripts\Activate.ps1
```

### 📄 3. Instalacija zavisnosti 
```{bash}
  pip install -r requirements.txt
```
> [!TIP]  
> Ukoliko ažurirate postojeće zavisnosti tj. biblioteke ili dodajete nove, možete ažurirati `requirements.txt` fajl sledećom komandom:  
>  
> ```{bash}  
> pip freeze > requirements.txt  
> ```

### 📄 4. Pokretanje aplikacije

### Upravljanje okruženjem i konfiguracijom aplikacije
Česta praksa prilikom razvoja web aplikacija jeste razdvajanje razvojnog (development) i produkcionog (production) okruženja, a razlog za to je njihova različita namena. Razvojno okruženje se koristi kada je potrebno da se testiraju nove funkcionalnosti ili da se otklone uočene nepravilnosti u radu aplikacije, dok je produkciono okruženje namenjeno korisnicima i mora da bude stabilno i pouzdano. Ovakva praksa omogućava programerima da rade bez rizika od narušavanja rada aplikacije u realnom vremenu. Pored toga, oba okruženja uglavnom imaju različite konfiguracione parametre - pristup bazi, logovanje ili bezbedonosna podešavanja što doprinosi fleksibilnosti i sigurnosti u radu. 

U folderu env se nalaze dva fajla prod.env i test.env sa promenljivama koje su potrebne za podešavanje okruženja aplikacije i one mogu da se podešavaju i menjaju u skladu sa potrebama. 

### Pokretanje aplikacije
U zavisnosti od toga koje okruženje je potrebno, prilikom pokretanja programa se dodaje određeni parametar. Ako je potrebno testno okruženje, onda se pokreće sledećom komandom: 

```{bash}
  python -m app.main --test
```
Ako je, pak, potrebno produkciono okruženje, onda se dodaje argument --prod

```{bash}
  python -m app.main --prod
```

## 📄 Dokumentacija API-ja: Swagger i ReDoc 
U prethodnim poglavljima je rečeno da je jedna od glavnih prednosti FastAPI framework-a ta što ima ugrađenu podršku za automatsko generisanje dokumentacije API-ja koja se oslanja na OpenAPI specifikaciju (ranije poznata i kao Swagger dokumentacija). Ova funkcionalnost FastAPI-ja u mnogome olakšava kako rad programerima, tako i krajnjim korisnicima API-ja jer imaju mogućnost brzog uvida u dostupne rute, parametre i očekivane odgovore. 

### SwaggerUI 
SwaggerUI interfejsu se pristupa preko rute */docs/swagger*. Ovaj interfejs predstavlja interaktivni web interfejs za pregled i testiranje API-ja bez potrebe za korišćenjem nekih drugih eksternih alata poput Postman-a ili curl-a. 

### ReDoc
ReDoc je drugi interaktivni web interfejs za pregled i testiranje API-ja koji je dostupan na ruti */docs/redoc*. Sam koncept ReDoc dokumentacije je drugačiji od Swagger-a jer je kod njega akcenat na strukturalno uređenoj i vizuelno čitljivijoj prezentaciji API-ja. Posebno je stavljen akcenat na hijerarhijsku navigaciju i detaljne opise polja i parametrima. ReDoc je često korišćen u produkciji gde je čitanje dokumentacije mnogo bitnije od interaktivnog testiranja. 

### Konfiguracija Swagger i ReDoc dokumentacije
Konfiguracija oba web interfejsa dokumentacije, tačnije definisanje njihovih ruta na osnovu kojih im se pristupa, se vrši prilikom inicijalizacije FastAPI aplikacije u **main.py** fajlu i to podešavanjem parametara *docs_url* i *redoc_url*: 

```{python}

app = FastAPI(
    title="Biblioteka API",
    description="REST API za upravljanje bibliotekom",
    version="1.0.0",
    contact={
        "name" : "Jefimija Stamenovic", 
        "url" : "https://github.com/jefimija-stamenovic", 
        "email" : "jefimija.stamenovic@gmail.com"
    },
    license_info={
        "name" : "Apache 2.0", 
        "url" : "https://www.apache.org/licenses/LICENSE-2.0.html"
    }, 
    docs_url="/docs/swagger", 
    redoc_url="/docs/redoc", 
    openapi_url="/openapi.json"
)
```
## Data Access Layer => repositories
Zbog automatskog praćenja svih SQLAlchemy modela koji se koriste u projektu, primenjena je sledeća logika - u fajlu **alembic.ini** je dodat sledeći kod:
```{python}
from app.core.db import Base
from app.models.base import *
target_metadata = Base.metadata
```
dok se u **app\models\base.py** navode svi modeli koji se koriste u aplikaciji: 
```{python}
from app.models.user import User
from app.models.author import Author
from app.models.book import Book
```
Ovakvim pristupom je obezbeđeno da svi modeli budu registrovani na jednom mestu bez potrebe da se dodatno menja fajl **alembic.ini**
## Business Layer => services 

## User Interface Layer => api 

## 🔒 Zaključak
FastAPI u kombinaciji sa troslojnom arhitekturom UI-BL-DAL predstavlja brzo, razumljivo i lako održivo rešenje za razvoj REST API-ja. U ovom jednostavnom projektu, kroz praktične primere, je napravljen *backend* za biblioteku koji je lak za nadogradnju, bezbedan za upotrebu i spreman za primenu u stvarnim projektima. 

## 📚 Literatura

https://www.uvicorn.org/#quickstart
https://alembic.sqlalchemy.org/en/latest/
