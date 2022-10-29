import json

def load_candidates():
    """
    Функция, которая загружает список кандидатов из файла
    """
    with open("candidates.json", 'r', encoding='utf-8') as file:
        candidates = json.load(file)

    # Создаём пустой список
    all_candidates = []

    # Запускаем цикл, который добавляет кандидатов в новый список
    for item in candidates:
        all_candidates.append(item)

    # Возвращаем список кандидатов
    return all_candidates

def get_all():
    """
    Функция выводит имена всех кандидатов
    """
    all_candidates = load_candidates()
    candidates = []

    for candidate in all_candidates:
        candidates.append(candidate["name"])

    return ", ".join(candidates)

def get_by_pk(pk):
    """
    Функция выводит кандидата по заданному id
    """
    all_candidates = load_candidates()

    for candidate in all_candidates:

        if candidate["pk"] == pk:
            right_candidate = candidate

    return right_candidate

def get_by_skill(skill):
    """
    Функция выводит всех кандидатов, у кого есть заданный навык
    """
    all_candidates = load_candidates()
    right_skills = []

    for candidate in all_candidates:

        if skill.lower() in candidate["skills"].lower().split(", "):
            right_skills.append(candidate)

    return right_skills



