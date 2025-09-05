from fastapi import FastAPI
from routes.drugs import router as drugs_router


app = FastAPI()
app.include_router(drugs_router)


@app.get("/")
async def root():
    return {"message": "Hello World"}
