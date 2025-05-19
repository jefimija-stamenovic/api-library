- [Biblioteka API](#biblioteka-api)
  - [O projektu](#o-projektu)
  - [🛠️ Ostale korišćene tehnologije u razvoju aplikacije](#️-ostale-korišćene-tehnologije-u-razvoju-aplikacije)
    - [🦄 Uvicorn](#-uvicorn)
    - [🧩 Pydantic](#-pydantic)
    - [🔗 SQLAlchemy](#-sqlalchemy)
    - [📦 Alembic](#-alembic)
  - [Arhitektura aplikacije](#arhitektura-aplikacije)
  - [Podešavanje okruženja](#podešavanje-okruženja)
    - [Instalacija zavisnosti](#instalacija-zavisnosti)
    - [Upravljanje okruženjem i konfiguracijom aplikacije](#upravljanje-okruženjem-i-konfiguracijom-aplikacije)
  - [Literatura](#literatura)


# Biblioteka API

## O projektu
U ovom projektu je prikazana izrada web servera za upravljanje bibliotekom uz korišćenje Python framework-a **FastAPI**. Aplikacija je razvijena u skladu sa troslojnom arhitekturom UI-BL-DAL čime se postiže lakše održavanje i veća preglednost koda, kao i jasno razgraničavanje odgovornosti između slojeva. Za rad sa podacima je primenjen ORM model **SQLAlchemy** koji omogućava objektno-orijentisanu komunikaciju sa bazom podataka bez direktnog pisanja SQL upita, sami podaci se čuvaju u MySQL bazi podataka, dok su **Pydantic** modeli korišćeni za validaciju podataka pristiglih od korisnika i pretvaranje u formate koji su podržani od strane FastAPI-a. 

## 🛠️ Ostale korišćene tehnologije u razvoju aplikacije

### 🦄 Uvicorn 
**Uvicorn** je ASGI (Asynchronous Server Gateway Interface) server koji se koristi za pokretanje FastAPI aplikacije. Osnovni zadatak Uvicorn-a je prijem HTTP zahteva koje šalje klijent i da ih prosledi samoj aplikaciji. Pošto radi po ASGI standardu, to značo da je moguć asinhroni rad tj. aplikacija može istovremeno da obrađuje više paralelnih zahteva, a da ne dođe do blokiranja. Ovo značajno doprinosi poboljšanju performansi i skalabilnosti aplikacije, naročito ako se radi o aplikacijama sa značajnim brojem korisnika. 

> [!IMPORTANT]
> Uvicorn je zvanično preporučen server za FastAPI aplikacije zbog svoje brzine i podrške za asinhroni rad. S obzirom da minimalno troši resurse, a brzo odgovara na klijentske zahteve, idealan je za upotrebu i u razvojnom i u produkcionom okruženju, posebno ako se radi o sistemima koji zahtevaju visok stepen paralelne obrade podataka. 

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


## Literatura

https://www.uvicorn.org/#quickstart
https://alembic.sqlalchemy.org/en/latest/