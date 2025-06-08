from fastapi import APIRouter, Depends, Path, Query, status, HTTPException, Body
from typing import List, Optional
from schemas.book import *
from services.book import ServiceBook, get_service
from core.classes import *
from api.examples.book import *
from core.security import JWTHelper

router: APIRouter = APIRouter(prefix="/books",tags=["Books"], 
                              dependencies= [Depends(JWTHelper.get_current_user)])

@router.post("/", name="Create book", summary="Create a new book",
    response_model=SchemaBook, response_description="Created book data", status_code=status.HTTP_201_CREATED,
    description="""This endpoint adds a new book in database. Required fields include title, isbn, availability, and author_id. 
                    Optionally, you can enter description and publication date. The ISBN must be unique.""",
    responses={
        status.HTTP_201_CREATED: {
            "description": "Successfully created author",
            "content": {
                "application/json": {
                    "example": {
                        "id": 1,
                        "title": "Na Drini ćuprija",
                        "description": "Roman o mostu i njegovoj simbolici",
                        "publication_date": "1945-01-01",
                        "isbn": "9788652101234",
                        "available": True,
                        "author_id": 1
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
def create_book(new_book: SchemaBookBase = Body(openapi_examples=example_create), 
                service: ServiceBook = Depends(get_service)) -> SchemaBook:
    try:
        return service.create(new_book)
    except ExceptionConflict as e:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, 
                            detail="Book with this name already exists.")
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, 
                            detail=str(e))

@router.get("/{book_id: int}", name="Get book by ID", summary="Retrieve book by ID",
    description="This endpoint retrieves the details of a specific book by their unique ID.",
    response_model=SchemaBook, response_description="Successfully retrieved book data.", status_code=status.HTTP_200_OK,
    responses={
        status.HTTP_200_OK: {
            "description": "Book successfully retrieved.",
            "content": {
                "application/json": {
                    "example": {
                        "id": 1,
                        "title": "Na Drini ćuprija",
                        "description": "Roman o mostu i njegovoj simbolici",
                        "publication_date": "1945-01-01",
                        "isbn": "9788652101234",
                        "available": True,
                        "author_id": 1
                    }
                }
            }
        },
        status.HTTP_404_NOT_FOUND: {
            "description": "Book not found.",
            "content": {
                "application/json": {
                    "example": {
                        "detail": "Book with provided ID does not exist."
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
                                "loc": ["path", "book_id"],
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
    })
def find_by_id(book_id: int, service: ServiceBook = Depends(get_service)) -> SchemaBook:
    try:
        return service.find_by_id(book_id)
    except ExceptionNotFound as e: 
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Book with provided ID = {book_id} not found"
        )
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=str(e)
        )

@router.put(
    "/{book_id: int}", name = "Update book by ID", summary = "Update book data providing ID", 
    description="This endpoint updates a book's data based on the provided ID ", 
    response_model=SchemaBook, status_code=status.HTTP_200_OK, 
    responses={
        status.HTTP_200_OK: {
            "description": "Book successfully updated.",
            "content": {
                "application/json": {
                    "example": {
                        "id": 1,
                        "title": "Na Drini ćuprija",
                        "description": "Roman o mostu i njegovoj simbolici",
                        "publication_date": "1945-01-01",
                        "isbn": "9788652101234",
                        "available": True,
                        "author_id": 1
                    }
                }
            }
        },
        status.HTTP_404_NOT_FOUND: {
            "description": "Book not found.",
            "content": {
                "application/json": {
                    "example": {
                        "detail": "Book with provided ID does not exist."
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
                                "loc": ["path", "book_id"],
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
def update_book(book_id: int, book_data: SchemaBookUpdate = Body(openapi_examples=example_update), service: ServiceBook = Depends(get_service)) -> SchemaBook:
    try:
        return service.update(book_id, book_data)
    except ExceptionNotFound as e: 
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Author with provided ID = {book_id} does not exist."
        )
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))

@router.delete("/{book_id: int}", name = "Delete author by ID", 
    summary = "Delete a book by provided ID", description="This endpoint deletes a book by ID from the database", 
    status_code=status.HTTP_200_OK, response_model=SchemaBook, 
    responses  = {
        status.HTTP_200_OK: {
            "description": "Book successfully deleted.",
            "content": {
                "application/json": {
                    "example": {
                        "id": 1,
                        "title": "Na Drini ćuprija",
                        "description": "Roman o mostu i njegovoj simbolici",
                        "publication_date": "1945-01-01",
                        "isbn": "9788652101234",
                        "available": True,
                        "author_id": 1
                    }
                }
            }
        },
        status.HTTP_404_NOT_FOUND: {
            "description": "Book not found.",
            "content": {
                "application/json": {
                    "example": {
                        "detail": "Book with provided ID does not exist."
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
                                "loc": ["path", "book_id"],
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
def delete_book(book_id: int, service: ServiceBook = Depends(get_service)) -> SchemaBook: 
    try:
        return service.delete(book_id)
    except ExceptionNotFound as e: 
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Book with provided ID = {book_id} does not exist."
        )
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=str(e)
        )

@router.get("/search", name="Search books", summary="Search books with optional filters",
    description="""Returns a list of books matching any combination of the following optional query parameters:
                `search` (title or ISBN), `available`, `author_id` and `publication_date`.
                If no filters are provided, all books are returned.""",
    response_model=List[SchemaBook], status_code=status.HTTP_200_OK,
    responses={
        status.HTTP_200_OK: {
            "description": "List of books retrieved successfully.",
            "content": {
                "application/json": {
                    "example": [
                        {
                            "id": 1,
                            "title": "Na Drini ćuprija",
                            "description": "Roman o mostu i njegovoj simbolici",
                            "publication_date": "1945-01-01",
                            "isbn": "9788652101234",
                            "available": True,
                            "author_id": 1
                        }
                    ]
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
def search_books(
    search: Optional[str] = Query(None, description="Filter by title (partial match) or ISBN"),
    available: Optional[bool] = Query(None, description="Filter by availability"),
    author_id: Optional[int] = Query(None, description="Filter by author ID"),
    publication_date: Optional[date] = Query(None, description="Filter by publication date"),
    service: ServiceBook = Depends(get_service)
) -> List[SchemaBook]:
    try:
        return service.search(search, available, author_id, publication_date)
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=str(e)
        )