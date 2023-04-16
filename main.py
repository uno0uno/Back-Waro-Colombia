# ============================================================
# WAROCOL.COM FAST API, HOLA :v
# ============================================================

#FastAPI
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware #different "origins"
from app.product.routers.product_router import product_router_app
from app.owners.routers.owner_router import owner_router_app
from app.sellers.router.seller_router import seller_router_app
from app.venues.router.venue_router import venue_router_app
from app.users.router.user_router import user_router_app
import uvicorn

# Initialize the app
app = FastAPI()
app.include_router(product_router_app)
app.include_router(owner_router_app)
app.include_router(seller_router_app)
app.include_router(venue_router_app)
app.include_router(user_router_app)

# ============================================================
# MIDDLEWARE TO CONECT
# ============================================================

origins = [
    "https://www.warocol.com",
    "https://warocol.com",
    "https://socio.warocol.com",
    "http://127.0.0.1:5173",
    "http://127.0.0.1:5174",
    "http://127.0.0.1:4173",
    "http://139.95.1.121"
    "http://0.0.0.0"
]

app.add_middleware(
        CORSMiddleware,
        allow_origins=origins,
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
        )


if __name__ == '__main__':
    uvicorn.run(app)