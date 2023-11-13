from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routes.route import router

app = FastAPI()

# Set up CORS
origins = [
    "https://ephemeral-bubblegum-4b0b0c.netlify.app",
]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["GET", "POST", "PUT", "DELETE"],
    allow_headers=["Content-Type", "Authorization"],
)
app.include_router(router)
