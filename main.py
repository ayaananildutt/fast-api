from fastapi import FastAPI

api = FastAPI()

@api.get('/')
def root():
    return {"message" : "Welcome to the Book Club API"}

@api.get('/status')
def status():
    return {
        "status" : "running",
        "api" : "Book Club"
    }
