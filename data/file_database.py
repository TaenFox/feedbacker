import json

def getById(id:str)-> dict:
    '''Извлекает информацию из json-файла в текущей директории, 
    название которого соответствует маске `{id}.json`. 
    Возвращает словарь'''
    try:
        with open(f"{id}.json", "r", encoding="utf-8") as json_file:
            data = json.load(json_file)
            return data
    except Exception as e:
        print(f"Can't read file {id}.json: {e}")

def addById(id:str, data:dict)-> dict:
    '''Сохраняет информацию в json-файл в текущей директории, 
    название которого соответствует маске `{id}.json`.
    В случае успеха возвращает сохранённый словарь значений'''
    try:
        json_file = open(f"{id}.json", "x", encoding="utf-8")
        json_file.write(json.dumps(data))
        json_file.close()
    except Exception as e:
        print(f"Can't create file {id}.json: {e}")
        return None
    
    try:
        savedData = getById(id=id)
        if data != savedData: raise Exception("Input data doesn't match to saved data")
        return savedData
    except Exception as e:
        print(f"Error creating file {id}.json: {e}")
        return None