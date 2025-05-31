from fastapi import APIRouter, Depends, HTTPException, status
from app.schemas.user import SchemaUserRegister
from app.services.user import ServiceUser, get_service
router: APIRouter = APIRouter(prefix="/auth", tags=["Users"])

@router.post(
    "/register", 
    name="Register new user", 
    summary="Endpoint for registration", 
    description=""" This endpoint registers a new user. In body, you have to send user data which 
                    contains first name, last name, email, username, password and flag for admin.
                    Username and email must be unique and password must pass the some checks. """,
    response_description="", 
    response_model=SchemaUserRegister, 
    status_code=status.HTTP_201_CREATED, 
    responses={
        status.HTTP_201_CREATED: {
            "description" : "User is successfully registered", 
            "content": {
                "application/json": {
                    "example": {
                        "first_name": "Jefimija",
                        "last_name": "Stamenovic",
                        "email": "jefimija.stamenovic@gmail.com",
                        "username": "jefimija.stamenovic",
                        "password": "jeff1234", 
                        "is_admin": False
                    }
                }
            }
        }, 
        status.HTTP_409_CONFLICT: {
            "description": "A user with the same email or username already exists.",
            "content": {
                "application/json": {
                    "example": {
                        "detail": "Username or email already in use."
                    }
                }
            }
        }, 
        status.HTTP_422_UNPROCESSABLE_ENTITY: {
            "description": "Validation error in the submitted data.",
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
            "description": "An unexpected error occurred on the server.",
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
def register_user(new_user: SchemaUserRegister, 
                  service: ServiceUser = Depends(get_service)) -> SchemaUserRegister: 
    try: 
        return service.register_user(new_user)
    except Exception as e: 
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Internal Server Error. Please try again later."
        )