from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from model import *

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

MESES = {
    1: "Janeiro",
    2: "Fevereiro",
    3: "Março",
    4: "Abril",
    5: "Maio",
    6: "Junho",
    7: "Julho",
    8: "Agosto",
    9: "Setembro",
    10: "Outubro",
    11: "Novembro",
    12: "Dezembro",
}

MESES_ABREV = {
    1: "JAN",
    2: "FEV",
    3: "MAR",
    4: "ABR",
    5: "MAI",
    6: "JUN",
    7: "JUL",
    8: "AGO",
    9: "SET",
    10: "OUT",
    11: "NOV",
    12: "DEZ",
}


# ──────────────────────────────────────────
# CONSULTAR CONVIVÊNCIAS
# ──────────────────────────────────────────
@app.get("/convivencias", response_class=HTMLResponse)
async def convivencias(request: Request):
    convivencias = consultar_convivencias()

    for convivencia in convivencias:
        convivencia["mes"] = MESES[convivencia["data"].month]
        convivencia["mes_abrev"] = MESES_ABREV[convivencia["data"].month]

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
        context={"avisos": avisos}
    )


# ──────────────────────────────────────────
# HOME
# ──────────────────────────────────────────
@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse(
        request=request,
        name="index.html"
    )