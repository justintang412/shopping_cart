from fastapi import FastAPI
from app.routes import auth, items

app = FastAPI()
app.include_router(auth.router, prefix="", tags=["token"])
app.include_router(items.router, prefix="", tags=["items"])
