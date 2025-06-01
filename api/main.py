from fastapi import FastAPI
from api.ratings.routes import router as ratings_router
from api.users.users_routes import router as users_router
from api.books.books_routes import router as books_router
from api.exchange.exchange_routes import router as exchange_router
from api.history.history_routes import router as history_router




app = FastAPI(title="BookSwap API")

# Registrar rutas
app.include_router(ratings_router)
app.include_router(users_router)
app.include_router(books_router)
app.include_router(exchange_router)
app.include_router(history_router)


@app.get("/")
def read_root():
    return {"message": "API BookSwap funcionando"}
