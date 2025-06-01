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
    return templates.TemplateResponse(request=request, name="pages/app/index.html")


@app.get("/commissions", response_class=HTMLResponse)
def handle_commissions(request: Request):
    return templates.TemplateResponse(
        request=request, name="pages/app/commissions.html"
    )


@app.get("/gallery", response_class=HTMLResponse)
def handle_gallery(request: Request):
    return templates.TemplateResponse(request=request, name="pages/app/gallery.html")


@app.get("/oc", response_class=HTMLResponse)
def handle_oc(request: Request):
    return templates.TemplateResponse(request=request, name="pages/app/oc.html")


@app.get("/login", response_class=HTMLResponse)
def handle_login(request: Request):
    return templates.TemplateResponse(request=request, name="pages/admin/login.html")


@app.get("/admin", response_class=HTMLResponse)
def handle_admin(request: Request):
    return templates.TemplateResponse(request=request, name="pages/admin/index.html")
