from fastapi import APIRouter
from starlette.responses import RedirectResponse

index_router = APIRouter()

@index_router.get("/")
def index():
    return RedirectResponse(url="/docs")