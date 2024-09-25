import sys
import os

# add root folder to sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from app import app
from fastapi.testclient import TestClient

from wonderwords import RandomWord

client = TestClient(app)

prefix = 'api/v1'

def test_create_blogs():
    r = RandomWord()
    random_word = r.random_words(4)
    blog_data = {
        "title": f"{random_word[0]} {random_word[1]} {random_word[2]} {random_word[3]}",
        "body": "This is a test blog content",
        "author_id": 2
    }

    response = client.post(f"{prefix}/blog/add", json=blog_data)
    assert response.status_code == 201

def test_read_blogs():
    response = client.get(prefix + '/blogs')
    assert response.status_code == 200

