from msilib.schema import Directory
from tracemalloc import StatisticDiff
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from routes import item_routes, order_routes, sold_item_routes
import db_conn

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get('/')
def homeView():
    return 'This is initial page'

db_conn.base.metadata.create_all(db_conn.engine)

app.include_router(item_routes.approute)
app.include_router(order_routes.approute)
app.include_router(sold_item_routes.approute)

app.mount("/images", StaticFiles(directory = "images"), name="images")