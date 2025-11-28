import pytest


def test_status(client):
    response = client.get("/")
    response_json = response.get_json()
    
    assert response.status_code == 200
    assert response_json["message"] == "API running"


def test_create_user_sucess(client):
    req_body = {
        "username": "user_teste",
        "password": "123"
    }
    
    response = client.post("/user", json=req_body)
    response_json = response.get_json()
    
    assert response.status_code == 201
    assert response_json["message"] == "Usuário cadastrado com sucesso!"


def test_create_user_invalid(client):
    req_body = {
        "username": "user_teste"
    }
    
    response = client.post("/user", json=req_body)
    response_json = response.get_json()
    
    assert response.status_code == 401
    assert response_json["message"] == "Dados inválidos!"


def test_login(client):
    # First create a user
    req_body_create = {
        "username": "user_teste",
        "password": "123"
    }
    client.post("/user", json=req_body_create)
    
    # Then login
    req_body = {
        "username": "user_teste",
        "password": "123"
    }

    response = client.post("/login", json=req_body)
    response_json = response.get_json()

    assert response.status_code == 200
    assert response_json["message"] == "Usuário autenticado com sucesso!"


def test_logout(client):
    # First create and login a user
    req_body_create = {
        "username": "user_teste",
        "password": "123"
    }
    client.post("/user", json=req_body_create)
    
    req_body_login = {
        "username": "user_teste",
        "password": "123"
    }
    client.post("/login", json=req_body_login)
    
    # Then logout
    response = client.post("/logout")
    
    assert response.status_code == 200


def test_logout_without_session(client):
    response = client.post("/logout")
    
    assert response.status_code == 401


def test_delete_user(client):
    # Create a user
    req_body_create = {
        "username": "user_teste",
        "password": "123"
    }
    client.post("/user", json=req_body_create)
    
    # Login
    req_body_login = {
        "username": "user_teste",
        "password": "123"
    }
    client.post("/login", json=req_body_login)
    
    # Delete the user
    req_body = {
        "username": "user_teste"
    }
    response = client.delete("/user", json=req_body)
    response_json = response.get_json()
    
    assert response.status_code == 200
    assert response_json["message"] == "Usuário removido com sucesso!"
