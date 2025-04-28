from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# Allow frontend to call the backend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # In production, change "*" to your frontend's URL
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def read_root():
    return {"message": "Hello from FastAPI!"}

@app.get("/hello")
def say_hello(name: str = "World"):
    return {"greeting": f"Hello, {name}!"}
