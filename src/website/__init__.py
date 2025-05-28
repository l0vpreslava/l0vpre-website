from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from jinja2 import Environment, PackageLoader


env = Environment(loader=PackageLoader("website", "./templates"))
templates = Jinja2Templates(env=env)

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")


@app.get("/", response_class=HTMLResponse)
def handle_root(request: Request):
    return templates.TemplateResponse(request=request, name="index.html")
