"""Things to bring: the starting point of your team project.

This is an example. Replace the topic with your own: change the fields,
the texts and the page. Grow it one pull request at a time.

What happens where:
- main.py      the web part: which address shows what (the "routes")
- storage.py   where the entries are kept
- templates/   the HTML page
- static/      the stylesheet
"""

from pathlib import Path

from fastapi import FastAPI, Form, Request
from fastapi.responses import RedirectResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

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
    if re.fullmatch(
        r"(?!www\.[a-zA-Z0-9-]+$)(www\.)?[a-zA-Z0-9]([a-zA-Z0-9-]*[a-zA-Z0-9])?\.[a-zA-Z]{2,}",
        url,
    ):
        storage.add_entry(
            url=url.strip(), short="".join(random.choices(string.ascii_letters, k=5))
        )
        return RedirectResponse(
            "/",
            status_code=303,  # Back to the start page. 303 tells the browser: load it with GET.
        )

    else:
        return "not a valid url"


@app.get("/short/{short_url}")
def short_2_long(short_url, request: Request):
    return templates.TemplateResponse(
        request,
        "redirect.html",
        context={"long_url": storage.search_for_url(short_url)},
    )
