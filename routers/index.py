from fastapi import APIRouter
from starlette.responses import RedirectResponse

index_router = APIRouter()

@index_router.get("/", include_in_schema=False)
def index():
    return RedirectResponse(url="/docs")