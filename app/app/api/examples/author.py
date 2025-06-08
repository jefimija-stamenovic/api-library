from typing import Dict 
from fastapi.openapi.models import Example
example_create: Dict[str, Example] = {
    "Example 1 - Basic Author": {
        "summary": "Author with all fields",
        "description": "The valid author with all specified fields",
        "value":{
            "first_name": "Ivo",
            "last_name": "Andrić",
            "biography": "Dobitnik Nobelove nagrade"
        }
    },
    "Example 2 - Without Biography": {
        "summary": "Author without biography",
        "description": "Valid author that don't include optional field `biography`",
        "value":{
            "first_name": "Desanka",
            "last_name": "Maksimović"
        }
    }, 
    "Example 3 - Invalid First Name": {
        "summary" : "Invalid value for author's first name", 
        "description" : "The value of first name is not matched with requested regular expression", 
        "value" : {
            "first_name": "Ivo111",
            "last_name": "Andrić",
            "biography": "Dobitnik Nobelove nagrade"
        }
    }
}

example_update: Dict[str, Example] = {
    "Example 1 - Basic": {
        "summary": "Author without books",
        "description": "A valid author update without associated books.",
        "value": {
            "first_name": "Danilo",
            "last_name": "Kiš",
            "biography": "Autor Grobnice za Borisa Davidoviča"
        }
    }
}