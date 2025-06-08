from fastapi import APIRouter, Depends, HTTPException, status
from schemas.user import *
from services.user import ServiceUser, get_service
from core.classes import *
from fastapi.security import OAuth2PasswordRequestForm

router: APIRouter = APIRouter(prefix="/auth", tags=["Users"])
@router.post(path = "/register", name="Registration", summary="Register a new user", 
    description="""This endpoint registers a new user. In body, you have to send user data which 
                contains first name, last name, email, username, password and flag for admin.
                Username and email must be unique and password must pass the some checks. """,
    response_description="This endpoint returns the created user", response_model=SchemaUser, status_code=status.HTTP_201_CREATED, 
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
                        "detail": "User with username or email already exists"
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
def register_user(new_user: SchemaUserRegister, service: ServiceUser = Depends(get_service)) -> SchemaUser: 
    try: 
        return service.register(new_user)
    except ExceptionConflict as e: 
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail = str(e))
    except Exception as e: 
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))

@router.post(path="/login", name="Login", summary="Login with credentials (username and password)",
    description="""This endpoint authenticates an existing user. You need to provide valid credentials of user - username and password.
            If authentication succeeds, it returns access and refresh tokens.""",
    response_description="Access and refresh tokens", response_model=SchemaToken, status_code=status.HTTP_200_OK,
    responses={
        status.HTTP_200_OK: {
            "description": "Login successful.",
            "content": {
                "application/json": {
                    "example": {
                        "access_token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...",
                        "refresh_token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9..."
                    }
                }
            }
        },
        status.HTTP_401_UNAUTHORIZED: {
            "description": "Invalid username or password.",
            "content": {
                "application/json": {
                    "example": {
                        "detail": "Invalid credentials"
                    }
                }
            }
        },
        status.HTTP_422_UNPROCESSABLE_ENTITY: {
            "description": "Validation error in the submitted credentials.",
            "content": {
                "application/json": {
                    "example": {
                        "detail": [
                            {
                                "loc": ["body", "username"],
                                "msg": "field required",
                                "type": "value_error.missing"
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
def login_user(form_data: OAuth2PasswordRequestForm = Depends(), service: ServiceUser = Depends(get_service)) -> SchemaToken:
    credentials = SchemaCredentials(username=form_data.username, password=form_data.password)
    try:
        return service.login(credentials)
    except ExceptionNotAuthorized:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid username or password.")
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))