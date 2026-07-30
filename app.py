from fastapi import FastAPI, Form, Request
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from model import *
import locale
import uvicorn

app = FastAPI()

locale.setlocale(locale.LC_TIME, "pt_BR.UTF-8")  # Linux/macOS
locale.setlocale(locale.LC_TIME, "Portuguese_Brazil.1252") # Windows
app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

# ──────────────────────────────────────────
# CONSULTAR CONVIVÊNCIAS
# ──────────────────────────────────────────
@app.get("/convivencias", response_class=HTMLResponse)
async def convivencias(request: Request):
    convivencias = consultar_convivencias()

    return templates.TemplateResponse(
        request=request,
        name="convivencia.html",
        context={"convivencias": convivencias}
    )

# ──────────────────────────────────────────
# CONSULTAR AVISOS
# ──────────────────────────────────────────
@app.get("/avisos", response_class=HTMLResponse)
async def avisos(request: Request):
    avisos = consultar_avisos()

    return templates.TemplateResponse(
        request=request,
        name="avisos.html",
        context={"avisos":avisos}
    )

@app.get("/", response_class=HTMLResponse)
async def home(request:Request):
    return templates.TemplateResponse(
        request=request,
        name="index.html"
    )

#if __name__ == "__main__":
    # Importante: ajuste o "app:app" caso o nome deste arquivo não seja app.py
#    uvicorn.run("app:app", host="0.0.0.0", port=8000, reload=True)