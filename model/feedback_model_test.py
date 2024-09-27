from feedback import Feedback
import uuid, json
import pytest

@pytest.fixture(scope="module")
def fix_feedback_data():
    '''Пресет данных для фидбека'''
    return  {
        "feedback_id": str(uuid.uuid4()),
        "content": "content_test_string",
        "author_id": str(uuid.uuid4()),
        "receiver_id": str(uuid.uuid4())
    }

def test_create_feedback_model(fix_feedback_data):
    '''Тест проверяет работоспособность класса Feedback:
    - создание экземпляра класса
    - выдачу данных экземпляра класса как словарь'''
    assert Feedback(fix_feedback_data).to_dict() == fix_feedback_data
