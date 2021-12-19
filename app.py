from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import FileResponse


from scraper import get_quotes_with_author_images
from scraper import get_data_from_api
from scraper import get_author_image
from scraper import create_author_quote_mapping

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"]
)


@app.get("/")
async def homepage():
    return FileResponse("./index.html")


@app.get("/api")
async def api():
    quotes_with_author_images = get_quotes_with_author_images()
    return {'data': quotes_with_author_images}


@app.get("/api/quotes")
async def api():
    api_response = get_data_from_api()
    return api_response


@app.get("/api/images")
async def api():
    api_data = get_data_from_api()
    author_quote_mapping = create_author_quote_mapping(api_data)
    author_quote_mapping = dict(
        sorted(author_quote_mapping.items(), key=lambda x: x[0].lower()))
    images = get_author_image(list(author_quote_mapping.keys()))
    return images
