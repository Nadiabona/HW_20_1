import pytest
from demostration_solution.service.genre import GenreService

class TestGenreService:
    @pytest.fixture(autouse=True) #фикстура, которая из дао будет кмидать в сервис то, что нужно
    #нам нужна фикстура несколько раз для всех тестов, и автоюз дает множественную загрузку фикстуры
    def genre_service(self, genre_dao): #тут genre_dao прогружается без импорта (находится среди фикстур, пропсанных в conftest
        self.genre_service = GenreService(dao = genre_dao) #фикстура дао падает в фикстуру сервиса

    def test_get_all(self):
        genres = self.genre_service.get_all()
        assert genres is not None
        assert len(genres) >0

    def test_get_one(self):
        genre = self.genre_service.get_one(1)
        assert genre is not None
        assert genre.id is not None
        assert genre.name == "Genre_1"

    def test_create(self):
        genre_d = {
            "name": "Genre_4"
        }

        genre = self.genre_service.create(genre_d)
        assert genre.id is not None

    def test_update(self):
        genre_d = {
            "id": 3,
            "name" : "New Name"
        }

        assert self.genre_service.update(genre_d)

    def test_delete(self):
        assert self.genre_service.delete(1) is None
