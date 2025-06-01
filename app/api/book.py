from fastapi import APIRouter, Depends, Path, Query, status, HTTPException
from typing import List, Optional
from app.schemas.book import SchemaBook, SchemaBookBase
from app.services.book import ServiceBook, get_service

router: APIRouter = APIRouter(
    prefix="/books",
    tags=["Books"]
)

@router.post(
    "/",
    name="Create book",
    summary="Create a new book",
    description=(
        "This endpoint creates a new book. Required fields include title, isbn, availability, "
        "and author_id. Optionally, description and publication date can be added. "
        "The ISBN must be unique."
    ),
    response_model=SchemaBook,
    response_description="Created book data",
    status_code=status.HTTP_201_CREATED,
    responses={
        201: {
            "description": "Book created successfully",
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
        422: {
            "description": "Validation error in submitted data.",
        },
        500: {
            "description": "Server error.",
        }
    }
)
def create_book(book_data: SchemaBookBase, service: ServiceBook = Depends(get_service)) -> SchemaBook:
    try:
        return service.create(book_data)
    except Exception:
        raise HTTPException(500, "Internal Server Error. Please try again later.")

@router.get(
    "/{book_id}",
    name="Get book by ID",
    summary="Retrieve a book by ID",
    description="This endpoint returns book data for the given ID.",
    response_model=SchemaBook,
    status_code=200
)
def get_book_by_id(book_id: int, service: ServiceBook = Depends(get_service)) -> SchemaBook:
    try:
        book = service.get_by_id(book_id)
        if not book:
            raise HTTPException(404, f"Book with ID {book_id} not found.")
        return book
    except Exception:
        raise HTTPException(500, "Internal Server Error. Please try again later.")

@router.put(
    "/{book_id}",
    name="Update book",
    summary="Update a book by ID",
    description="This endpoint updates a book by its ID.",
    status_code=204
)
def update_book(book_id: int, book_data: SchemaBookBase, service: ServiceBook = Depends(get_service)) -> None:
    try:
        updated = service.update(book_id, book_data)
        if not updated:
            raise HTTPException(404, f"Book with ID {book_id} not found.")
    except Exception:
        raise HTTPException(500, "Internal Server Error. Please try again later.")

@router.delete(
    "/{book_id}",
    name="Delete book",
    summary="Delete a book by ID",
    description="This endpoint deletes the book identified by the given ID.",
    status_code=204
)
def delete_book(book_id: int, service: ServiceBook = Depends(get_service)) -> None:
    try:
        deleted = service.delete(book_id)
        if not deleted:
            raise HTTPException(404, f"Book with ID {book_id} not found.")
    except Exception:
        raise HTTPException(500, "Internal Server Error. Please try again later.")

@router.get(
    "/search",
    name="Search books",
    summary="Search books with optional filters",
    description=(
        "This endpoint returns books filtered by any combination of the following optional query parameters: "
        "combined `title` or `isbn`, `author_id`, and `available`. If no parameters are provided, all books will be returned."
    ),
    response_model=List[SchemaBook],
    status_code=200
)
def search_books(
    search: Optional[str] = Query(None, description="Filter by title (partial match) or ISBN"),
    available: Optional[bool] = Query(None, description="Filter by availability"),
    service: ServiceBook = Depends(get_service)
) -> List[SchemaBook]:
    try:
        return service.search(search, available)
    except Exception:
        raise HTTPException(500, "Internal Server Error. Please try again later.")