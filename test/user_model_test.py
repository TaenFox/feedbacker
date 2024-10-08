from model.user import User
import uuid, json
import pytest

@pytest.fixture(scope="module")
def fix_user_data():
    '''Пресет пользовательских данных'''
    return  {
        "user_id": str(uuid.uuid4()),
        "sent_feedback_ids": [],
        "recieved_feedback_ids":[]
    }

def test_import_user_model_from_dict(fix_user_data):
    '''Тест проверяет импорт класса User из словаря'''
    user_obj = User()
    user_obj.from_dict(fix_user_data)
    assert user_obj.to_dict() == fix_user_data

def test_wrong_type_user_id(fix_user_data):
    '''Тест проверяет корректность отработки исключения 
    на строковый тип данных в поле user_id'''
    wrong_data = fix_user_data
    wrong_data["user_id"] = uuid.uuid4()
    with pytest.raises(Exception):
        User(wrong_data)

def test_wrong_type_sent_feedback_ids(fix_user_data):
    '''Тест проверяет корректность отработки исключения 
    на тип данных список в поле sent_feedback_ids'''
    wrong_data = fix_user_data
    wrong_data["sent_feedback_ids"] = "test_string"
    with pytest.raises(TypeError):
        User(wrong_data)

def test_wrong_type_recieved_feedback_ids(fix_user_data):
    '''Тест проверяет корректность отработки исключения 
    на тип данных список в поле recieved_feedback_ids'''
    wrong_data = fix_user_data
    wrong_data["recieved_feedback_ids"] = "test_string"
    with pytest.raises(TypeError):
        User(wrong_data)