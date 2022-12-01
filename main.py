# ============================================================
# WAROCOL.COM FAST API, HOLA :v
# ============================================================

#FastAPI
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware #different "origins"
from app.parthner.routers.parthner_router import parthner_router_app
from app.users.routers.user_router import user_router_app
from app.Product.routers.products import product_router_app
from app.Payments.routers.payments_router import payment_router_app
from app.Songs.routers.songs import songs_router_app

import uvicorn

# Initialize the app
app = FastAPI()
app.include_router(user_router_app)
app.include_router(parthner_router_app) 
app.include_router(product_router_app)
app.include_router(payment_router_app)
app.include_router(songs_router_app)

# ============================================================
# MIDDLEWARE TO CONECT
# ============================================================

origins = [
    "https://www.warocol.com",
    "https://warocol.com",
    "http://127.0.0.1:5173",
    "http://139.95.1.121"
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