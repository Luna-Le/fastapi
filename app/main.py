
from fastapi import FastAPI
from . import models
from .database import engine
from .routers import post, user, auth, vote
from .config import settings
from fastapi.middleware.cors import CORSMiddleware



# models.Base.metadata.create_all(bind=engine)

app = FastAPI() 

origins = ["*"]


app.add_middleware(
    CORSMiddleware,
    allow_origins=origins, #which domains are allowed to talk to our api
    allow_credentials=True,
    allow_methods=["*"], #which methods are allowed
    allow_headers=["*"], ##which headers are allowed
)


app.include_router(post.router)
app.include_router(user.router)
app.include_router(auth.router)
app.include_router(vote.router)

@app.get("/")
def root():
    return {"message": "Hello World"}



