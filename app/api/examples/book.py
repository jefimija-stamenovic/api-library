from fastapi.openapi.models import Example
from typing import Dict 

example_create : Dict[str, Example] = {
    "na_drini_cuprija": Example(
        summary="Na Drini ćuprija",
        description="Roman Ive Andrića o mostu u Višegradu i istorijskim dešavanjima na Balkanu.",
        value={
            "title": "Na Drini ćuprija",
            "isbn": "978-86-519-0193-1",
            "description": "Istorijski roman koji prati život ljudi oko mosta u Višegradu tokom više vekova.",
            "author_id": 1, 
            "available" : True
        }
    ),
    "hazarski_recnik": Example(
        summary="Hazarski rečnik",
        description="Postmoderni roman Milorada Pavića u formi rečnika.",
        value={
            "title": "Hazarski rečnik",
            "isbn": "978-86-331-4363-3",
            "description": "Roman-leksikon koji se čita kao mozaik različitih mitova, religija i vremena.",
            "author_id": 2, 
            "avaliable" : True
        }
    ),
    "grobnica_borisa_davidovica": Example(
        summary="Grobnica za Borisa Davidoviča",
        description="Skup pripovedaka Danila Kiša o političkim represijama u 20. veku.",
        value={
            "title": "Grobnica za Borisa Davidoviča",
            "isbn": "978-86-03-00018-7",
            "description": "Sedam pripovedaka o pojedincima u totalitarnim sistemima.",
            "author_id": 3
        }
    )
}

example_update: Dict[str, Example] = {
    "Example 1 - Changed title": {
        "summary": "Ažuriranje više podataka",
        "description": "Promena naslova postojeće knjige.",
        "value": {
            "title": "Travnička hronika",
            "isbn": "978-86-519-2222-0",
            "available": False
        }
    },
    "Example 2 - Changed availability": {
        "summary": "Ažuriranje dostupnosti",
        "description": "Ažuriranje dostupnosti knjige i ISBN broja.",
        "value": {
            "isbn": "978-86-7346-456-1",
            "available": True
        }
    },
    "Example 3 - Changed author": {
        "summary": "Ažuriranje autora",
        "description": "Ažurira se autor knjige, kao naslov i dostupnost",
        "value": {
            "title": "Vreme smrti",
            "available": True,
            "author_id": 3
        }
    }
}