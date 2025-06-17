import os
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from . import models
from .database import engine
from .routers import user, post, auth


# Only create tables if not in testing mode
if not os.getenv("TESTING"):
    models.Base.metadata.create_all(bind=engine)

# instance of fastapi
app = FastAPI()


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Configure this properly for production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(post.router)
app.include_router(user.router)
app.include_router(auth.router)

@app.get("/")
async def root():
    return "Server running at http://localhost:8000"



