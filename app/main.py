from fastapi import FastAPI, File, UploadFile
from pydantic import BaseModel
import pandas as pd

app = FastAPI()


class Item(BaseModel):
    name: str
    description: str | None = None
    price: float
    tax: float | None = None


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.post("/uploadfile/")
async def create_upload_file(file: UploadFile = File(...)):
    df = pd.read_csv(file.file)
    # Process the DataFrame (df) as needed
    # return {"filename": file.filename, "columns": df.columns.tolist()}
    return {"filename": file.filename, "data": df.to_json(orient="records")}


@app.post("/items/")
async def create_item(item: Item):
    return item