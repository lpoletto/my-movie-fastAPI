from models.movie import Movie as MovieModel
from schemas.movie import Movie

class MovieService():
    
    def __init__(self, db):
        self.db = db
    

    def get_movies(self):
        try:
            result = self.db.query(MovieModel).all()
        finally:
            self.db.close()
        return result


    def get_movie(self, id: int):
        try:
            result = self.db.query(MovieModel).filter(MovieModel.id == id).first()
        finally:
            self.db.close()
        return result


    def get_movies_by_category(self, category: str):
        try:
            result = self.db.query(MovieModel).filter(MovieModel.category== category).all()
        finally:
            self.db.close()
        return result
    

    def create_movie(self, movie: Movie):
        new_movie = MovieModel(**movie.dict()) # Envío los datos al modelo
        try:
            self.db.add(new_movie)
            self.db.commit() # actualizo en la db
        finally:
            self.db.close()
        return
    

    def update_movie(self, id: int, data: Movie):
        try:
            movie = self.db.query(MovieModel).filter(MovieModel.id == id).first()
            movie.title = data.title
            movie.overview = data.overview
            movie.year = data.year
            movie.rating = data.rating
            movie.category = data.category

            self.db.commit() # actualizo en la db
        finally:
            self.db.close()
        return
    

    def delete_movie(self, id: int):
        try:
            movie = self.db.query(MovieModel).filter(MovieModel.id == id).first()
            
            self.db.delete(movie)
            self.db.commit() # actualizo en la db
        finally:
            self.db.close()
        return