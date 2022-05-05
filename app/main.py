from constants import TORTOISE_ORM_APP
from models import Notes
from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from tortoise import Tortoise

app = FastAPI()


@app.on_event("startup")
async def startup():
    await Tortoise.init(
        TORTOISE_ORM_APP
    )


@app.on_event("shutdown")
async def shutdown():
    await Tortoise.close_connections()


templates = Jinja2Templates(directory="templates")


@app.get("/", response_class=HTMLResponse)
async def create_note(request: Request):
    qs = await Notes.all()
    print(qs)
    await Notes(text="amaizing").save()
    qs = await Notes.all().count()
    print(qs)
    # query = notes.select()
    # notes_qs = await database.fetch_all(query)
    # # query = notes.insert().values(text=note.text, completed=note.completed)
    # tournament = Notes(text='New Tournament', )
    # await tournament.save()
    return templates.TemplateResponse("index.html", {"request": request})


