import pytest
from demostration_solution.service.movie import MovieService

class TestMovieService:
    @pytest.fixture(autouse=True) #фикстура, которая из дао будет кмидать в сервис то, что нужно
    #нам нужна фикстура несколько раз для всех тестов, и автоюз дает множественную загрузку фикстуры
    def movie_service(self, movie_dao): #тут movie_dao прогружается без импорта (находится среди фикстур, пропсанных в conftest
        self.movie_service = MovieService(dao = movie_dao) #фикстура дао падает в фикстуру сервиса

    def test_get_all(self):
        movies = self.movie_service.get_all()
        assert movies is not None
        assert len(movies) >0

    def test_get_one(self):
        movie = self.movie_service.get_one(1)
        assert movie is not None
        assert movie.id is not None
        assert movie.title == "Movie_1"

    def test_create(self):
        movie_d = {
            "title": "Movie_4",
            "description" : "Description",
            "trailer" : "link",
             "year" : 2000,
             "rating" : 10.0,
             "genre_id" : 1,
             "director_id" : 1
        }

        movie = self.movie_service.create(movie_d)
        assert movie.id is not None

    def test_update(self):
        movie_d =  {   "id" : 1,
            "title": "New Movie",
            "description" : "Description",
            "trailer" : "link",
             "year" : 2000,
             "rating" : 10.0,
             "genre_id" : 1,
             "director_id" : 1
        }
        assert self.movie_service.update(movie_d)

    def test_delete(self):
        assert self.movie_service.delete(1) is None
