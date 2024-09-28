import sys 
import os.path 
sys.path.append(os.path.dirname(os.path.abspath(__file__)) + "/..") 

from data.database_interface import FeedbackDTO
import pytest
import uuid, json

@pytest.fixture
def temp_catalog_user(tmp_path):
    '''Создаёт временный каталог user для тестов.'''
    catalog = tmp_path / 'data' / 'user'
    catalog.mkdir(parents=True, exist_ok=True)
    return catalog

@pytest.fixture()
def temp_catalog_feedback(tmp_path):
    '''Создаёт временный каталог feedback для тестов.'''
    catalog = tmp_path / 'data' / 'feedback'
    catalog.mkdir(parents=True, exist_ok=True)
    return catalog

@pytest.fixture
def fix_feedback_data():
    '''Пресет данных для фидбека'''
    return  {
        "feedback_id": str(uuid.uuid4()),
        "content": "content_test_string",
        "author_id": str(uuid.uuid4()),
        "receiver_id": str(uuid.uuid4())
    }

def test_add_feedback(temp_catalog_feedback, fix_feedback_data):
    feedback_id = fix_feedback_data['feedback_id']
    FeedbackDTO(temp_catalog_feedback).add_feedback_by_id(feedback_id, fix_feedback_data)

    file_path = temp_catalog_feedback / f"{feedback_id}.json"
    assert file_path.exists()

    with open(file_path, 'r', encoding='utf-8') as f:
        saved_data = json.load(f)
        assert saved_data == fix_feedback_data

def test_get_feedback(temp_catalog_feedback, fix_feedback_data):
    feedback_id = fix_feedback_data['feedback_id']
    FeedbackDTO(temp_catalog_feedback).add_feedback_by_id(feedback_id, fix_feedback_data)
    exist_feedback_data = FeedbackDTO(temp_catalog_feedback).get_feedback_by_id(feedback_id)
    assert exist_feedback_data == fix_feedback_data