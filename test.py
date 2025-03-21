import os
import requests
from dotenv import load_dotenv

# Carregar variáveis de ambiente do arquivo .env
load_dotenv()

BASE_URL = os.getenv("BASE_URL")
TOKEN = os.getenv("TOKEN")

def test_get_courses():
    
    url = f"{BASE_URL}/courses"
    headers = {"Authorization": f"Bearer {TOKEN}"}

    # Fazendo a requisição GET
    response = requests.get(url, headers=headers)

    # Validações
    assert response.status_code == 200, "Status code não é 200"
    data = response.json()
    assert isinstance(data, list), "Resposta não é uma lista"
    assert len(data) > 0, "Nenhum curso encontrado"
    
    # Mostrar a lista de cursos no console
    print("Lista de cursos:")
    for i, course in enumerate(data, 1):
        print(f"{i}. {course}")

# Executar a função fora da definição
if __name__ == "__main__":
    test_get_courses()
