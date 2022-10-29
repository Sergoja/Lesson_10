# Импортируем Flask и написанные функции
from flask import Flask
from functions import load_candidates, get_by_pk, get_by_skill

# Задаем экземпляр Flask
app = Flask(__name__)

# Загружаем список кандидатов
candidates = load_candidates()

@app.route("/")
def get_candidates():
    """
    Функция, которая возвращает список кандидатов
    """
    result = '<pre>'

    # Делаем цикл для вывода всех кандидатов
    for candidate in candidates:
        result += f"""
        Имя кандидата - {candidate["name"]}\n
        Позиция кандидата - {candidate["position"]}\n
        Навыки - {candidate["skills"]}\n
        """
    result += '</pre>\n'

    # Возвращаем список кандидатов
    return result

@app.route("/candidates/<int:pk>")
def page_profile(pk):
    """
    Функция, которая возвращает кандидата по заданному id
    """
    candidate = get_by_pk(pk)
    result = '<br>'
    result += candidate['name'] + '<br>'
    result += candidate['position'] + '<br>'
    result += candidate['skills'] + '<br>'

    # Возвращаем информацию о кандидате по заданному id
    return f"""
            <img src="{candidate['picture']}">
            <pre> {result} </pre>
            """

@app.route("/skills/<skill>")
def get_candidate_skills(skill):
    """
    Функция, показывающая кандидата с заданным навыком
    """
    candidate_skills = get_by_skill(skill)
    result = '<pre>'

    for candidate in candidate_skills:
        result += f"""
            {candidate["name"]}\n
            {candidate["position"]}\n
            {candidate["skills"]}\n
            """
    result += '</pre>\n'

    return result

app.run(host='127.0.0.2', port=80)
