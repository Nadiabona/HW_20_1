import pytest
from demostration_solution.service.director import DirectorService

class TestDirectorService:
    @pytest.fixture(autouse=True) #фикстура, которая из дао будет кмидать в сервис то, что нужно
    #нам нужна фикстура несколько раз для всех тестов, и автоюз дает множественную загрузку фикстуры
    def director_service(self, director_dao): #тут director_dao прогружается без импорта (находится среди фикстур, пропсанных в conftest
        self.director_service = DirectorService(dao = director_dao) #фикстура дао падает в фикстуру сервиса

    def test_get_all(self):
        directors = self.director_service.get_all()
        assert directors is not None
        assert len(directors) >0

    def test_get_one(self):
        director = self.director_service.get_one(1)
        assert director is not None
        assert director.id is not None
        assert director.name == "Director_1"

    def test_create(self):
        director_d = {
            "name": "Director_4"
        }

        director = self.director_service.create(director_d)
        assert director.id is not None

    def test_update(self):
        director_d = {
            "id": 3,
            "name" : "New Name"
        }

        assert self.director_service.update(director_d)

    def test_delete(self):
        assert self.director_service.delete(1) is None


