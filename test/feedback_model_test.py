from model.feedback import Feedback
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

def test_import_feedback_model_from_dict(fix_feedback_data):
    '''Тест проверяет работоспособность класса Feedback:
    - создание экземпляра класса
    - выдачу данных экземпляра класса как словарь'''
    feedback_obj = Feedback()
    feedback_obj.from_dict(fix_feedback_data)
    assert feedback_obj.to_dict() == fix_feedback_data

def test_wrong_type_feedback_id(fix_feedback_data):
    '''Тест проверяет корректность отработки исключения 
    на строковый тип данных в поле feedback_id'''
    wrong_data = fix_feedback_data
    wrong_data["feedback_id"] = uuid.uuid4()
    with pytest.raises(TypeError):
        Feedback().from_dict(wrong_data)