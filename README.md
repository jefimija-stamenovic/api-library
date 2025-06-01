
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
  - [SQLALchemy modeli](#sqlalchemy-modeli)
  - [Pydantic šeme](#pydantic-šeme)
  - [Data Access Layer ➡️ `app\repositories`](#data-access-layer-️-apprepositories)
  - [Business Layer ➡️ `app\services`](#business-layer-️-appservices)
  - [User Interface Layer ➡️ `app\api`](#user-interface-layer-️-appapi)
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

```bash
  git clone https://github.com/jefimija-stamenovic/api-library.git
  cd api-library
```
#### Struktura projekta 
Nakon kloniranja projekta, klonirani projekat bi trebalo da ima sledeću strukturu: 

```
api-library/
├── app/
│   ├── api/                        # UI sloj 
│   │   ├── book.py
│   │   ├── author.py
│   │   └── user.py
│   │
│   ├── services/                   # BL sloj
│   │   ├── book.py
│   │   ├── author.py
│   │   └── user.py
│   │
│   ├── repositories/              # DAL sloj
│   │   ├── book.py
│   │   ├── author.py
│   │   └── user.py
│   │
│   ├── models/                    # SQLAlchemy modeli
│   │   ├── book.py
│   │   ├── author.py
│   │   └── user.py
│   │
│   ├── schemas/                   # Pydantic šeme
│   │   ├── book.py
│   │   ├── author.py
│   │   └── user.py
│   │
│   ├── core/                      # Konfiguracija, povezivanje na bazu, konstante itd.
│   │   ├── config.py
│   │   ├── constants.py
│   │   ├── db.py
│   │   └── security.py
│   │
│   └── main.py                    # Glavni program
│
├── alembic/                    # Alembic 
│   ├── versions/
│   ├── env.py
│   └── script.py.mako
│
├── alembic.ini                    # Alembic конфигурација
├── requirements.txt              # Зависности
├── README.md
└── .env                          # ENV променљиве (DB info, тајне, итд.)

```

### 📦 2. Podešavanje virtuelnog okruženja 

```bash
python -m venv naziv-virtualnog-okruzenja
.\naziv-virtualnog-okruzenja\Scripts\Activate.ps1
```

### 📄 3. Instalacija zavisnosti 
```bash
  pip install -r requirements.txt
```
> [!TIP]  
> Ukoliko ažurirate postojeće zavisnosti tj. biblioteke ili dodajete nove, možete ažurirati `requirements.txt` fajl sledećom komandom:  
>  
> ```bash
> pip freeze > requirements.txt  
> ```

### 📄 4. Pokretanje aplikacije

### Upravljanje okruženjem i konfiguracijom aplikacije
Česta praksa prilikom razvoja web aplikacija jeste razdvajanje razvojnog (development) i produkcionog (production) okruženja, a razlog za to je njihova različita namena. Razvojno okruženje se koristi kada je potrebno da se testiraju nove funkcionalnosti ili da se otklone uočene nepravilnosti u radu aplikacije, dok je produkciono okruženje namenjeno korisnicima i mora da bude stabilno i pouzdano. Ovakva praksa omogućava programerima da rade bez rizika od narušavanja rada aplikacije u realnom vremenu. Pored toga, oba okruženja uglavnom imaju različite konfiguracione parametre - pristup bazi, logovanje ili bezbedonosna podešavanja što doprinosi fleksibilnosti i sigurnosti u radu. 

U folderu env se nalaze dva fajla prod.env i test.env sa promenljivama koje su potrebne za podešavanje okruženja aplikacije i one mogu da se podešavaju i menjaju u skladu sa potrebama. 

### Pokretanje aplikacije
U zavisnosti od toga koje okruženje je potrebno, prilikom pokretanja programa se dodaje određeni parametar. Ako je potrebno testno okruženje, onda se pokreće sledećom komandom: 

```bash
  python -m app.main --test
```
Ako je, pak, potrebno produkciono okruženje, onda se dodaje argument --prod

```bash
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

```python

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
## SQLALchemy modeli
U okviru foldera **app/models** se nalaze svi SQLAlchemy modeli potrebni za rad aplikacije. 
Primer SQLAlchemy modela **Book**: 
```python
  class Book(Base):
    __tablename__ = "books"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(100), nullable=False, index=True)
    description = Column(Text, nullable=True)
    publication_date = Column(Date, nullable=True)
    isbn = Column(String(20), unique=True, nullable=False)
    available = Column(Boolean, default=True)

    author_id = Column(Integer, ForeignKey("authors.id"), nullable=False)
    author = relationship("Author", back_populates="books")
```
Objašnjenje ➡️ Klasa **Book** predstavlja entitet **Knjiga** koji je u bazi mapiran na tabelu **books** što i prikazuje naredna sekcija koda: 
```python
class Book(Base):
    __tablename__ = "books"
```
Svaka knjiga je opisana sa atributima (u SQLAlchemy su to objekti **Column**) čija objašnjenja data u tablici ispod: 
| Naziv kolone      | Tip podatka     | Opis                                                                 |
|-------------------|-----------------|----------------------------------------------------------------------|
| `id`              | Integer         | Primarni ključ čija je vrednost *autoincrement* tj. automatski se uvećava i podignut je indeks po ovoj koloni |
| `title`           | String(100)     | Naslov knjige sa maksimalnom dužinom od 100 karaktera |
| `description`     | Text            | Opis ili kratak sadržaj knjige koji nije obavezno uneti |
| `publication_date`| Date            | Datum objavljivanja knjige koji nije obavezno uneti |
| `isbn`            | String(20)      | Jedinstveni ISBN broj koji mora da se unese |
| `available`       | Boolean         | Identifikator da li je knjiga dostupna, a podrazumevana vrednost je da jeste |

Za svaku knjigu treba znati i njenog autora, pa je potrebno postaviti referencu na autora. 
Referenciranje podrazumeva postavljanje stranog ključa **author_id** i navigacije **relationship()**: 
```python
author_id = Column(Integer, ForeignKey("authors.id"), nullable=False)
author = relationship("Author", back_populates="books")
```

> [!IMPORTANT]
> Zbog automatskog praćenja svih SQLAlchemy modela koji se koriste u projektu, primenjena je sledeća logika – u fajlu **alembic.ini** je dodat sledeći kod:
>
> ```python
> from app.core.db import Base
> from app.models.base import *
> target_metadata = Base.metadata
> ```
>
> dok se u **app/models/base.py** navode svi modeli koji se koriste u aplikaciji:
>
> ```python
> from app.models.user import User
> from app.models.author import Author
> from app.models.book import Book
> ```
>
> Ovakvim pristupom je obezbeđeno da svi modeli budu registrovani na jednom mestu bez potrebe da se dodatno menja fajl **alembic.ini**.

## Pydantic šeme
U FastAPI-u se često koriste Pydantic šeme koje se koriste za validiranje i strukturisanje ulaznih i izlaznih podataka. Tehnički, one se ponašaju kao DTO-vi (Data Transfer Objects) tj. kao objekti za prenos podataka na relaciji klijent-aplikacija ili različitih slojeva aplikacije. 

> [!CAUTION]
> SQLAlchemy modeli služe za opisivanje strukture podataka u bazi i koriste se za rad na DAL nivou, dok se Pydantic šeme koriste isključivo za definisanje struktura podataka koje se primaju ili šalju preko API-ja. 

U nastavku je dat primer Pydantic šeme `SchemaBookBase`: 
```python
class SchemaBookBase(BaseModel): 
    title : str  = Field(min_length=1)
    description: Optional[str] = Field(None, max_length=2000)
    publication_date: Optional[date] = Field(None)
    isbn : str = Field(min_length=10, max_length=20)
    available: bool = Field()
    author_id: int = Field(gt=0)

    @field_validator("title")
    def validate_title(cls, value: str) -> str:
        pattern = r"^[A-Za-z0-9ČĆŽŠĐčćžšđ\s\-\.,!?\"'()]+$"
        if not re.match(pattern, value):
            raise ValueError("Title may contain letters, numbers, spaces, punctuation, and hyphens only.")
        return value

    @field_validator("isbn")
    def validate_isbn(cls, value: str) -> str:
        pattern = r"^[0-9\-]+$"
        if not re.match(pattern, value):
            raise ValueError("ISBN must contain only digits and hyphens.")
        return value

    model_config = ConfigDict(from_attributes=True)

```
**SchemaBookCreate** je DTO za kreiranje knjige i ima određena polja. Svako polje u klasi ima neke uslove - naslov ne sme biti prazan, isbn mora biti dužine između 10 i 20 karaktera, dok ID autor mora biti pozitivan ceo broj. U tabeli je dato detaljno objašnjenje svih korišćenih elemenata: 

| Element                           | Objašnjenje                                                                                                        |
|-----------------------------------|--------------------------------------------------------------------------------------------------------------------|
| `BaseModel`                       | Roditeljska klasa iz koje se izvode sve Pydantic šeme. Omogućava validaciju, parsiranje i automatsku dokumentaciju |
| `Field()`                         | Definiše dodatna pravila iinformacije za polja (npr. `min_length`, `gt`, `description`, itd.).                     |
| `Optional[type]`                  | Polje nije obavezno                                                                                                |
| `min_length`, `max_length`        | Minimum/maksimum dozvoljenih karaktera u stringu                                                                   |
| `gt=0`                            | Vrednost mora biti veća od nule (great than).                                                                      |
| `@field_validator("ime")`         | Dekorator za ručnu validaciju određenog polja koji se poziva automatski pri parsiranju podataka                    |
| `raise ValueError("poruka")`      | Ako vrednost nije validna, aktivira se greška tj.FastAPI će podići HTTPException sa status kodom 422 i porukom.    |
| `model_config = ConfigDict(...)`  | Konfiguracija ponašanja modela, npr. `from_attributes=True` omogućava ORM konverziju.                |

> [!NOTE]
> Moguće je direktno konvertovanje ORM modela u Pydantic šeme:  
> ```python
>   model_config = ConfigDict(from_attributes=True)
> ```
> Ovo je izuzetno korisno jer omogućava da se ORM objekti dobijeni od DAL sloja automatski pretvore u Pydantic šeme (DTO) bez ručnog mapiranja 

## Data Access Layer ➡️ `app\repositories`
Kao što je već rečeno, ovaj sloj je posrednik između baze podataka i poslovne logike aplikacije. U okviru njega se nalaze sve funkcije koje se tiču uzimanja, kreiranja, ažuriranja i brisanja podataka.

U nastavku je dat primer klase **RepositoryBook** koja sadrži metode za rad sa entitom **Book**. 
```python 
from datetime import date
from typing import Optional, List
from sqlalchemy import or_, func
from sqlalchemy.sql import expression
from sqlalchemy.orm import Session, Query
from app.models.book import Book
from app.models.author import Author
from app.core.db import Database

class RepositoryBook:
    _session : Session 
    def __init__(self) -> None:
        self._session = Database.get_session()

    def create(self, new_book: Book) -> Book:
            self._session.add(new_book)
            self._session.commit()
            self._session.refresh(new_book)
            return new_book

    def find_by_id(self, book_id: int) -> Optional[Book]:
        return self._session.query(Book).filter(Book.id == book_id).first()
    
    def find_by_title(self, title: str) -> Optional[Book]:
        return self._session.query(Book).filter(Book.title == title).first()

    def update(self, author_id, updated_data: dict) -> Book:
        updated_book: Book = self.find_by_id(author_id)
        print(updated_book)
        for attr, value in updated_data.items(): 
            if attr == 'id': 
                continue
            setattr(updated_book, attr, value)

        self._session.commit()
        self._session.refresh(updated_book)
        return updated_book

    def delete(self, book_id: int) -> bool:
        book: Book = self.find_by_id(book_id)
        self._session.delete(book)
        self._session.commit()
        return book

    def search(self, search: Optional[str] = None, available: Optional[bool] = None, author_id: Optional[int] = None,  
               publication_date: Optional[date] = None) -> List[Book]:
        query: Query[Book] = self._session.query(Book).join(Book.author)
        if search:
            param_search: str = f"%{search.lower()}%"
            query = query.filter(
                or_(
                    func.lower(Book.title).like(param_search),
                    func.lower(Book.isbn).like(param_search),
                    func.lower(Book.author).like(param_search), 
                    func.lower(Author.first_name).like(param_search),
                    func.lower(Author.last_name).like(param_search),
                )
            )
        query = query.filter(
                Book.author_id == author_id if author_id is not None else expression.true(), 
                Book.available == available if available is not None  else expression.true(), 
                Book.publication_date == publication_date if publication_date is not None else expression.true()
            )
        return query.all()
```
| Metoda                                 | Opis                                                                                   |
|----------------------------------------|----------------------------------------------------------------------------------------|
| `create(self, new_book: Book) -> Book` | Dodaje novu knjigu u bazu i odmah vraća novokreirani objekat sa generisanim `id`-jem.  |
| `find_by_id(self, book_id: int) -> Optional[Book]`  | Traži knjigu sa prosleđenim ID-em. Ako ne postoji, vraća `None`.          |
| `find_by_title(self, title: str) -> Optional[Book]` | Pomoćna metoda za filtriranje knjiga po naslovu.                          |
| `update(self, book_id: int, updated_data: dict) -> Book` | Ažuriranje knjige na osnovu prosleđenog rečnika `updated_data`       |
| `delete(self, book_id: int) -> bool` | Briše knjigu koja ima prosleđeni ID |

## Business Layer ➡️ `app\services` 
Servisi služe za implementiranje poslovne logike, a ujedno su posrednici između kontrolera i repozitorijuma. U okviru servisa se obavlja sva poslovna logika poput provere i pripreme podataka pre nego što se proslede DAL sloju. 
Servisi obezbeđuju da kontroleri ne brinu o detaljima baze, dok se repozitorijumi koriste isključivo za CRUD operacije bez pisanja dodatne logike.  

Dat je primer servisa **ServiceBook** u kom je implementirana logika upravljanja knjigama: 

```python 
from app.core.classes import *
from app.repositories.book import RepositoryBook
from app.schemas.book import *
from app.models.book import Book
from typing import Any, List, Optional, Dict

class ServiceBook: 
    _repository : RepositoryBook
    def __init__(self) -> None:
        self._repository = RepositoryBook() 

    def find_by_id(self, book_id: int) -> SchemaBook: 
        founded_book: Book = self._repository.find_by_id(book_id)
        if not founded_book:
            raise ExceptionNotFound
        return SchemaBook.model_validate(founded_book)
    
    def create(self, new_author: SchemaBookBase) -> SchemaBook:
        founded_book: Book = self._repository.find_by_title(new_author.title)
        if founded_book:
            raise ExceptionConflict()
        model_book : Book = Book(**new_author.model_dump())
        return SchemaBook.model_validate(self._repository.create(model_book))
    
    def delete(self, book_id: int) -> SchemaBook: 
        founded_book: Optional[SchemaBook] = self.find_by_id(book_id)
        return SchemaBook.model_validate(self._repository.delete(book_id))
    
    def update(self, book_id: int, updated_book: SchemaBookUpdate) -> SchemaBook: 
        founded_book: Optional[SchemaBook] = self.find_by_id(book_id)
        dict_book: Dict[str, Any] = updated_book.model_dump(exclude_unset=True)
        return SchemaBook.model_validate(self._repository.update(book_id, dict_book))

    def search(self, search: Optional[str] = None, available: Optional[bool] = None, 
               author_id: Optional[int] = None, publication_date: Optional[date] = None) -> List[SchemaBook]:
        books: List[Book] = self._repository.search(search, available, author_id, publication_date)
        return [SchemaBook.model_validate(book) for book in books]
```
## User Interface Layer ➡️ `app\api` 
UI sloj predstavlja ulaznu tačku za sve zahteve koji dolaze preko HTTP protokola. Router koristi dekoratore `@router.get()`, `@router.post()` i dr. za definisanje ruta tj. putanja i mapira ih na funkcije koje obrađuju te zahteve. 

Zadaci rutera su:
 - Validiranje ulaza - ruter koristi Pydantic šeme da proveri da li je zahtev ispravno formatiran (Body, Query, Path)
 - Pozivanje servisnog sloja - unutar rutera se poziva metode servisa sa određenim parametrima i logika je prepuštena njemu 
 - Slanje odgovora - ruter šalje odgovarajući HTTP status i telo odgovora (**response_model**)
 - Obrada grešaka - sve greške koje dođu od strane servisa se hvataju i u zavisnosti od greške se kreira određeni **HTTPException** sa status kodom i opisom greške 

Naredna sekcija koda prikazuje implementaciju kontrolera za upravljanje knjigama: 

```python
from fastapi import APIRouter, Depends, Path, status, HTTPException, Query, Body
from typing import List, Optional
from app.schemas.author import SchemaAuthorBase, SchemaAuthor, SchemaAuthorUpdate
from app.services.author import ServiceAuthor, get_service
from app.core.classes import *
from app.api.examples.author import *

router: APIRouter = APIRouter(
    prefix = "/authors", 
    tags = ["Authors"]
)

@router.post(path = "/", name = "Create new author", summary="Create a new author", 
        description="""This endpoint creates a new author. In body, you have to send data object which  
                        contains first name, last name and optionally a biography of author. 
                        First name and last name contain only letters, spaces or hyphens and length must
                        be between 2 and 50 characters
                    """, 
    response_model=SchemaAuthor, response_description="This endpoint returns the created author", status_code=status.HTTP_201_CREATED, 
    responses={
        status.HTTP_201_CREATED: {
            "description": "Successfully created author",
            "content": {
                "application/json": {
                    "example": {
                        "id": 1,                            
                        "first_name": "Ivo",
                        "last_name": "Andrić",
                        "biography": "Dobitnik Nobelove nagrade", 
                        "books" : []
                    }
                }
            }
        },
        status.HTTP_409_CONFLICT: {
            "description": "Author already exists",
            "content": {
                "application/json": {
                    "example": {
                        "detail": "Author with this name already exists."
                    }
                }
            }
        },
        status.HTTP_422_UNPROCESSABLE_ENTITY: {
            "description": "Validation error in the submitted data",
            "content": {
                "application/json": {
                    "example": {
                        "detail": [
                            {
                                "loc": ["body", "email"],
                                "msg": "value is not a valid email address",
                                "type": "value_error.email"
                            }
                        ]
                    }
                }
            }
        },
        status.HTTP_500_INTERNAL_SERVER_ERROR: {
            "description": "An unexpected error occurred on the server",
            "content": {
                "application/json": {
                    "example": {
                        "detail": "Internal Server Error. Please try again later."
                    }
                }
            }
        }
    }
)
def create_author(new_author: SchemaAuthorBase = Body(openapi_examples=example_create), service: ServiceAuthor = Depends(get_service)) -> SchemaAuthor:
    try:
        return service.create(new_author)
    except ExceptionConflict as e:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail="Author with this name already exists.")
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, 
                            detail=str(e))

@router.get("/{author_id: int}", name="Get author by ID", summary="Retrieve author by ID",
    description="This endpoint retrieves the details of a specific author by their unique ID.",
    response_model=SchemaAuthor, response_description="Successfully retrieved author data.", status_code=status.HTTP_200_OK,
    responses={
        status.HTTP_200_OK: {
            "description": "Author successfully retrieved.",
            "content": {
                "application/json": {
                    "example": {
                        "id": 1,
                        "first_name": "Ivo",
                        "last_name": "Andrić",
                        "biography": "Dobitnik Nobelove nagrade", 
                        "books" : []
                    }
                }
            }
        },
        status.HTTP_404_NOT_FOUND: {
            "description": "Author not found.",
            "content": {
                "application/json": {
                    "example": {
                        "detail": "Author with provided ID does not exist."
                    }
                }
            }
        },
        status.HTTP_422_UNPROCESSABLE_ENTITY: {
            "description": "Invalid ID format.",
            "content": {
                "application/json": {
                    "example": {
                        "detail": [
                            {
                                "loc": ["path", "author_id"],
                                "msg": "value is not a valid integer",
                                "type": "type_error.integer"
                            }
                        ]
                    }
                }
            }
        },
        status.HTTP_500_INTERNAL_SERVER_ERROR: {
            "description": "Unexpected server error.",
            "content": {
                "application/json": {
                    "example": {
                        "detail": "Internal Server Error. Please try again later."
                    }
                }
            }
        }
    }
)
def get_author_by_id(author_id:int, service: ServiceAuthor = Depends(get_service)) -> SchemaAuthor:
    try:
        return service.find_by_id(author_id)
    except ExceptionNotFound as e: 
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Author with provided ID = {author_id} does not exist."
        )
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=str(e)
        )

@router.put("/{author_id}", name = "Update author by ID", summary = "Update author data providing ID", 
    description="This endpoint updates an author's data based on the provided ID ", 
    response_model=SchemaAuthor, status_code=status.HTTP_200_OK, 
    responses={
        status.HTTP_200_OK: {
            "description": "Successfully created author",
            "content": {
                "application/json": {
                    "example": {
                        "id": 1,                            
                        "first_name": "Ivo",
                        "last_name": "Andrić",
                        "biography": "Dobitnik Nobelove nagrade", 
                        "books" : []
                    }
                }
            }
        },
        status.HTTP_404_NOT_FOUND: {
            "description": "Author based on the provided ID was not found.",
            "content": {
                "application/json": {
                    "example": {"detail": "Author with provided ID does not exist."}
                }
            }
        },
        status.HTTP_422_UNPROCESSABLE_ENTITY: {
            "description": "Invalid input data.",
            "content": {
                "application/json": {
                    "example": {
                        "detail": [
                            {
                                "loc": ["body", "first_name"],
                                "msg": "field required",
                                "type": "value_error.missing"
                            }
                        ]
                    }
                }
            }
        },
        status.HTTP_500_INTERNAL_SERVER_ERROR: {
            "description": "Unexpected server error.",
            "content": {
                "application/json": {
                    "example": {
                        "detail": "Internal Server Error. Please try again later."
                    }
                }
            }
        }
    }
)
def update_author(author_id: int, updated_data: SchemaAuthorUpdate = Body(openapi_examples=example_update), service: ServiceAuthor = Depends(get_service)) -> SchemaAuthor:
    try:
        return service.update(author_id, updated_data)
    except ExceptionNotFound as e: 
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Author with provided ID = {author_id} does not exist."
        )
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))
 
@router.delete(
    "/{author_id: int}", name = "Delete author by ID", 
    summary = "Delete an author by provided ID", description="This endpoint deletes an author by ID from the database", 
    status_code=status.HTTP_200_OK, response_model=SchemaAuthor, 
    responses = {
        status.HTTP_200_OK: {
            "description": "Successfully deleted author",
            "content": {
                "application/json": {
                    "example": {
                        "id": 1,                            
                        "first_name": "Ivo",
                        "last_name": "Andrić",
                        "biography": "Dobitnik Nobelove nagrade", 
                        "books" : []
                    }
                }
            }
        },
        status.HTTP_404_NOT_FOUND: {
            "description": "Author not found.",
            "content": {
                "application/json": {
                    "example": {
                        "detail": "Author with provided ID does not exist."
                    }
                }
            }
        },
        status.HTTP_500_INTERNAL_SERVER_ERROR: {
            "description": "Unexpected server error.",
            "content": {
                "application/json": {
                    "example": {
                        "detail": "Internal Server Error. Please try again later."
                    }
                }
            }
        }
    }
)
def delete_author(
    author_id: int, 
    service: ServiceAuthor = Depends(get_service)) -> SchemaAuthor: 
    try:
        return service.delete(author_id)
    except ExceptionNotFound as e: 
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Author with provided ID = {author_id} does not exist."
        )
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=str(e)
        )
    

@router.get("/search", name="Search authors", summary="Search authors with optional filter critera",
    description=(
        "This endpoints returns a list of authors that match the given filter criteria. "
        "Query param search is optional which means if is not provided, all authors will be returned. "
        "Search filter include: first name, last name, and partial match on biography."
    ),
    response_model=List[SchemaAuthor], response_description="List of authors matching the filters.", status_code=status.HTTP_200_OK,
    responses={
        status.HTTP_200_OK: {
            "description": "Authors retrieved successfully.",
            "content": {
                "application/json": {
                    "example": [
                        {
                            "id": 1,
                            "first_name": "Ivo",
                            "last_name": "Andrić",
                            "biography": "Dobitnik Nobelove nagrade"
                        }
                    ]
                }
            }
        },
        status.HTTP_500_INTERNAL_SERVER_ERROR: {
            "description": "Unexpected server error.",
            "content": {
                "application/json": {
                    "example": {"detail": "Internal Server Error. Please try again later."}
                }
            }
        }
    }
)
def search_authors(
    search: Optional[str] = Query(None, description="Filter by author's first name or last name or biography"),
    service: ServiceAuthor = Depends(get_service)) -> List[SchemaAuthor]:
    try:
        return service.search(search)
    except Exception:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Internal Server Error. Please try again later."
        )
```

| Dekorator          | Namena                                                                              |
|--------------------|-------------------------------------------------------------------------------------|
| `@router.post()`   | Prima `POST` zahtev i koristi se za **kreiranje** novog entiteta                    |
| `@router.get()`    | Prima `GET` zahtev i koristi se za **čitanje** ili **pretragu** postojećih podataka |
| `@router.put()`    | Prima `PUT` zahtev i koristi se za **ažuriranje** postojećeg entiteta               |
| `@router.delete()` | Prima `DELETE` zahtev i koristi se za **brisanje** entiteta                         |

Primer ➡️ `@router.post('/')`
Namena: Zadatak ove rute je kreiranje tj. dodavanje novog autora. U nastavku je dato detaljno objašnjenje svakog argumenta u okviru dekoratora `@router.post('/')`
| Parametar                       | Objašnjenje                                                                              |
|---------------------------------|------------------------------------------------------------------------------------------|
| `name="Create new author"`      | Naziv rute koji se prikazuje u OpenAPI (Swagger)                                         |
| `summary="Create a new author"` | Kratak opis rute - pojavljuje se kao naslov u Swagger web interfejsu                     |
| `description="""..."""`         | Detaljan opis zahteva - objašnjava koji podaci se očekuju i kako se validiraju           |
| `response_model=SchemaAuthor`   | Vraća podatke u obliku šeme `SchemaAuthor` – automatski validiran i dokumentovan odgovor |
| `status_code=201`               | HTTP status kod za uspešno kreiranje resursa                                             |
| `Depends(get_service)`          | Ubacuje instancu `ServiceAuthor` pomoću **dependency injection** sistema.                |
| `Body(openapi_examples=...)`    | Definiše telo zahteva i uključuje primere za Swagger                                     |
| `responses={...}`               | Dokumentuje sve moguće odgovore sa opisima i primerima.                                  |

## 🔒 Zaključak
FastAPI u kombinaciji sa troslojnom arhitekturom UI-BL-DAL predstavlja brzo, razumljivo i lako održivo rešenje za razvoj REST API-ja. U ovom jednostavnom projektu, kroz praktične primere, je napravljen *backend* za biblioteku koji je lak za nadogradnju, bezbedan za upotrebu i spreman za primenu u stvarnim projektima. 

## 📚 Literatura

https://www.uvicorn.org/#quickstart
https://alembic.sqlalchemy.org/en/latest/