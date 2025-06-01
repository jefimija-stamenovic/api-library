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
    }
}