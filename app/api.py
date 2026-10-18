from fastapi import FastAPI

from app.main import add, subtract

api = FastAPI(title="CI/CD Demo API")


@api.get("/")
def root():
    return {"message": "CI/CD demo API. See /docs"}


@api.get("/add")
def add_route(a: float, b: float):
    return {"result": add(a, b)}


@api.get("/subtract")
def subtract_route(a: float, b: float):
    return {"result": subtract(a, b)}


@api.get("/health")
def health():
    return {"status": "ok"}
