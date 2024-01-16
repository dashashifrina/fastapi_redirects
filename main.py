from fastapi import FastAPI, Request
from starlette.responses import RedirectResponse

app = FastAPI()

@app.post("/upload_image")
async def upload_image():
    return RedirectResponse(url='/get_image', status_code=307)

@app.post("/get_image")
async def get_image(request: Request):
    return await request.json()