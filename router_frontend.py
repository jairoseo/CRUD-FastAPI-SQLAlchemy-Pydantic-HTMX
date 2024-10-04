from pathlib import Path
from fastapi import APIRouter, Request, HTTPException
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi_htmx import htmx, htmx_init
import httpx

htmx_init(templates=Jinja2Templates(directory=Path(".") / "templates"))

API_BASE_URL = "http://127.0.0.1:8000"

router = APIRouter()

@router.get("/", response_class=HTMLResponse)
@htmx("index","index")
async def index(request: Request):
    return {"title": "Productos"}

@router.get("/b/add_product", response_class=HTMLResponse)
@htmx("product_add")
async def add_product(request: Request):
    return {"ok":"ok"}

@router.get("/b/products", response_class=HTMLResponse)
@htmx("product_list")
async def products(request: Request):
    async with httpx.AsyncClient() as client:
        response = await client.get(f"{API_BASE_URL}/products/")    
        if response.status_code != 200:
            raise HTTPException(status_code=response.status_code, detail="Error al obtener el listado de productos")
    return {"products": response.json()}

@router.get("/b/product/{product_id}", response_class=HTMLResponse)
@htmx("product_view")
async def product_view(request: Request, product_id: int):
    async with httpx.AsyncClient() as client:
        response = await client.get(f"{API_BASE_URL}/product/{product_id}")    
        if response.status_code != 200:
            raise HTTPException(status_code=response.status_code, detail="Error al obtener el producto")
    return {"product": response.json()}

@router.get("/b/edit_product/{product_id}", response_class=HTMLResponse)
@htmx("product_edit")
async def product_view(request: Request, product_id: int):
    async with httpx.AsyncClient() as client:
        response = await client.get(f"{API_BASE_URL}/product/{product_id}")    
        if response.status_code != 200:
            raise HTTPException(status_code=response.status_code, detail="Error al obtener el producto")
    return {"product": response.json()}