import pytest
import redis
import app

@pytest.fixture()
def test_correct_count():
    count = app.get_hit_count()
    newCount = app.get_hit_count()
    assert count == (newCount + 1)

@pytest.fixture()
def test_incorrect_count():
    count = app.get_hit_count()
    get_hit_count()
    newCount = app.get_hit_count()
    assert count == (newCount + 1)
