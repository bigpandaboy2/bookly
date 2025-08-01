from fastapi import FastAPI
from src.books.routes import book_router
from src.auth.routes import auth_router
from src.reviews.routes import review_router
from src.tags.routes import tags_router
from contextlib import asynccontextmanager
from src.db.main import init_db
from .errors import register_all_errors
from .middleware import register_middleware

@asynccontextmanager
async def life_span(app: FastAPI):
    print(f"Server is starting...")
    await init_db()
    yield
    print(f"Server has been stopped.")

version = "v1"

app = FastAPI(
    title="Bookly",
    description="A simple book management API",
    version=version
)

register_all_errors(app)

register_middleware(app)

app.include_router(book_router, prefix=f"/api/{version}/books", tags=["books"])
app.include_router(auth_router, prefix=f"/api/{version}/auth", tags=["auth"])
app.include_router(review_router, prefix=f"/api/{version}/reviews", tags=["review"])
app.include_router(tags_router, prefix=f"/api/{version}/tags", tags=["tags"])