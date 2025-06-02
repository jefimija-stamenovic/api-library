from fastapi import APIRouter, Depends, status, HTTPException, Query, Body
from typing import Sequence, Optional
from schemas.author import SchemaAuthorBase, SchemaAuthor, SchemaAuthorUpdate
from services.author import ServiceAuthor, get_service
from core.classes import *
from api.examples.author import *
from core.security import JWTHelper

router: APIRouter = APIRouter(prefix="/authors", tags=["Authors"])

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
async def create_author(new_author: SchemaAuthorBase = Body(openapi_examples=example_create), 
                  service: ServiceAuthor = Depends(get_service), 
                  current_user=Depends(JWTHelper.get_current_user)) -> SchemaAuthor:
    try:
        return await service.create(new_author)
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
async def get_author_by_id(author_id:int, service: ServiceAuthor = Depends(get_service)) -> SchemaAuthor:
    try:
        return await service.find_by_id(author_id)
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
async def update_author(author_id: int,
                updated_data: SchemaAuthorUpdate = Body(openapi_examples=example_update), 
                service: ServiceAuthor = Depends(get_service), 
                current_user=Depends(JWTHelper.get_current_user)) -> SchemaAuthor:
    try:
        return await service.update(author_id, updated_data)
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
async def delete_author(author_id: int, service: ServiceAuthor = Depends(get_service), current_user=Depends(JWTHelper.get_current_user)) -> SchemaAuthor: 
    try:
        return await service.delete(author_id)
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
    response_model=Sequence[SchemaAuthor], response_description="List of authors matching the filters.", status_code=status.HTTP_200_OK,
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
async def search_authors(
    search: Optional[str] = Query(None, description="Filter by author's first name or last name or biography"),
    service: ServiceAuthor = Depends(get_service)) -> Sequence[SchemaAuthor]:
    try:
        return await service.search(search)
    except Exception:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Internal Server Error. Please try again later."
        )