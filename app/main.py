from pathlib import Path

from fastapi import FastAPI, Form, Request
from fastapi.responses import RedirectResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi import HTTPException  # noqa: F401
from . import storage

import random, string, re

HERE = Path(__file__).parent

app = FastAPI(title="Url shortener (shorty)")
app.mount("/static", StaticFiles(directory=HERE / "static"), name="static")
templates = Jinja2Templates(directory=HERE / "templates")


@app.get("/")
def show_list(request: Request):  # The start page: the form and all entries.
    return templates.TemplateResponse(
        request, "index.html", {"entries": storage.all_entries()}
    )


@app.post("/add")
def add(url: str = Form(...)):  # The form on the start page sends its fields here.
    valid_url = storage.validate_url(url)
    if not valid_url:
        return "not a valid url"

    storage.add_entry(
        url=valid_url,
        short=storage.create_short(),
    )

    return RedirectResponse(
        "/",
        status_code=303,  # Back to the start page. 303 tells the browser: load it with GET.
    )


@app.api_route("/short/{short_url}", methods=["GET", "HEAD"])
def short_2_long(short_url, request: Request):
    long_url = storage.search_for_url(short_url)
    if not long_url:
        return templates.TemplateResponse(
            request, "not_found.html", {"entries": storage.all_entries()}
        )

    return RedirectResponse(long_url, status_code=307)
