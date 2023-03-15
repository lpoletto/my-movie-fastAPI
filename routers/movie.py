from fastapi import APIRouter
from fastapi import Path, Query, Depends
from fastapi.responses import JSONResponse
from typing import List
from config.database import Session
from models.movie import Movie as MovieModel
from fastapi.encoders import jsonable_encoder
from middlewares.jwt_bearer import JWTBearer
from services.movie import MovieService
from schemas.movie import Movie

movie_router = APIRouter()

@movie_router.get('/movies', tags=["movies"], response_model=Movie, status_code=200, dependencies=[Depends(JWTBearer())])
def get_movies() -> List[Movie]:
    db = Session()
    result = MovieService(db).get_movies()
    if not result:
        return JSONResponse(status_code=404, content={"message": "No encontrado"})
    
    return JSONResponse(status_code=200, content=jsonable_encoder(result))


# Parametros de ruta
@movie_router.get('/movies/{id}', tags=["movies"], response_model=Movie, status_code=200)
def get_movie(id: int = Path(ge=1, le=2000)) -> Movie:
    db = Session()
    result = MovieService(db).get_movie(id=id)
    if not result:
        return JSONResponse(status_code=404, content={"message": "No encontrado"})
    
    return JSONResponse(status_code=200, content=jsonable_encoder(result))


# Parametros Query
@movie_router.get('/movies/' ,tags=["movies"], response_model=List[Movie], status_code=200)
def get_movies_by_category(category: str = Query(min_length=5, max_length=15)) -> List[Movie]:
    db = Session()
    result = MovieService(db).get_movies_by_category(category=category)
    if not result:
        return JSONResponse(status_code=404, content={"message": "No encontrado"})
    
    return JSONResponse(status_code=200, content=jsonable_encoder(result))


# Metodo POST
@movie_router.post('/movies', tags=["movies"], response_model=dict, status_code=201)
def create_movie(movie: Movie) -> dict:
    db = Session()
    MovieService(db).create_movie(movie)
    return JSONResponse(status_code=201, content={"message":"Se ha registrado la película"})


# Metodo PUT
@movie_router.put('/movies/{id}', tags=["movies"], response_model=dict, status_code=200)
def update_movie(id: int, movie: Movie) -> dict:
    db = Session()
    result = MovieService(db).get_movie(id=id)
    if not result:
        return JSONResponse(status_code=404, content={"message": "No encontrado"})
    
    MovieService(db).update_movie(id=id, data=movie)
    return JSONResponse(status_code=200, content={"message":"Se ha modificado la película"})


# Metodo DELETE
@movie_router.delete('/movies/{id}', tags=["movies"], response_model=dict, status_code=200)
def delete_movie(id: int) -> dict:
    db = Session()
    result = MovieService(db).get_movie(id=id)
    if not result:
        return JSONResponse(status_code=404, content={"message": "No encontrado"})
    
    MovieService(db).delete_movie(id=id)
    return JSONResponse(status_code=200, content={"message":"Se ha eliminado la película"})