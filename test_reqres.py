import requests

BASE_URL = "https://reqres.in"

def test_get_users_status_code():
    # Enviar la petición GET usando la librería requests
    response = requests.get(f"{BASE_URL}/api/users?page=2")
    
    # 1. Validar que el Status Code sea 200 OK
    assert response.status_code == 200, f"Expected status 200, but got {response.status_code}"
    
    # 2. Validar que el tiempo de respuesta sea óptimo (menor a 1 segundo)
    assert response.elapsed.total_seconds() < 1.0, "Response time is too slow!"
    
    # 3. Validar el contenido del JSON analizando un campo específico
    data = response.json()
    assert data["data"][0]["email"] == "michael.lawson@reqres.in", "Email does not match expected value"

def test_create_user():
    # Definir los datos que enviaremos en el cuerpo de la petición (Payload)
    payload = {
        "name": "Ivan Suarez Alva",
        "job": "Lead QA Automation Engineer"
    }
    
    # Enviar la petición POST
    response = requests.post(f"{BASE_URL}/api/users", json=payload)
    
    # 1. Validar que el código de estado sea 201 Created
    assert response.status_code == 201, f"Expected status 201, but got {response.status_code}"
    
    # 2. Validar que la respuesta devuelva el nombre correcto del QA
    response_data = response.json()
    assert response_data["name"] == "Ivan Suarez Alva", "Name does not match"
    assert response_data["job"] == "Lead QA Automation Engineer", "Job title does not match"  

def test_update_user():
    # Datos actualizados para el usuario
    payload = {
        "name": "Ivan Suarez Alva",
        "job": "Lead QA Automation Engineer"
    }
    
    # Enviar la petición PUT al recurso 2
    response = requests.put(f"{BASE_URL}/api/users/2", json=payload)
    
    # 1. Validar Status Code 200 OK
    assert response.status_code == 200, f"Expected status 200, but got {response.status_code}"
    
    # 2. Validar que el puesto se haya actualizado correctamente en la respuesta JSON
    response_data = response.json()
    assert response_data["job"] == "Lead QA Automation Engineer", "Updated job title does not match"

def test_delete_user():
    # Enviar la petición DELETE al recurso 2
    response = requests.delete(f"{BASE_URL}/api/users/2")
    
    # Validar Status Code 204 No Content (estándar para borrado exitoso)
    assert response.status_code == 204, f"Expected status 204, but got {response.status_code}"  