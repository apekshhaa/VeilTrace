from fastapi import FastAPI

from api.routes import router

app = FastAPI(
    title="VeilTrace Core Engine"
)

app.include_router(router)


@app.get("/")
def root():
    return {
        "message": "VeilTrace Core Engine Running"
    }