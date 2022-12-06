import requests


def test_get_method__general_url__expect_first_response():
    # FIXTURE
    url = "https://jsonplaceholder.typicode.com/"
    status = 200
    expected_result = {
        "userId": 1,
        "id": 1,
        "title": "sunt aut facere repellat provident occaecati excepturi optio reprehenderit",
        "body": "quia et suscipit\nsuscipit recusandae consequuntur expedita et cum\nreprehenderit molestiae ut ut quas totam\nnostrum rerum est autem sunt rem eveniet architecto"
    }

    # EXERCISE
    response = requests.get(url+"posts")

    # ASSERT
    result = response.json()
    assert response.status_code == status
    assert result[0] ==  expected_result


def test_get_method_by_id__general_url__expect_first_response():
    # FIXTURE
    id = 1
    url = f"https://jsonplaceholder.typicode.com/"
    status = 200
    expected_result = {
        "userId": 1,
        "id": 1,
        "title": "sunt aut facere repellat provident occaecati excepturi optio reprehenderit",
        "body": "quia et suscipit\nsuscipit recusandae consequuntur expedita et cum\nreprehenderit molestiae ut ut quas totam\nnostrum rerum est autem sunt rem eveniet architecto"
    }

    # EXERCISE
    response = requests.get(url+f"posts/{id}")

    # ASSERT
    result = response.json()
    assert response.status_code == status
    assert result ==  expected_result


def test_post_method__general_url__expect_post_body():
    # FIXTURE
    url = "https://jsonplaceholder.typicode.com/"
    status = 201
    body = {
        "title": 'Testando POST',
        "body": 'S206 - PYTEST',
        "userId": 1,
    }

    # EXERCISE
    response = requests.post(url+"posts", json=body)

    # ASSERT
    result = response.json()
    assert response.status_code == status

    del(result["id"])
    assert result == body


def test_put_method__general_url__expect_update_body():
    # FIXTURE
    url = "https://jsonplaceholder.typicode.com/"
    status = 200
    body = {
        "id": 1,
        "title": 'Atualização - PUT',
        "body": 'Novo body',
        "userId": 1,
    }

    # EXERCISE
    response = requests.put(url+"posts/1", json=body)

    # ASSERT
    result = response.json()
    assert response.status_code == status
    
    assert result == body


def test_delete_method__general_url__expect_status_code():
    # FIXTURE
    url = "https://jsonplaceholder.typicode.com/"
    status = 200

    # EXERCISE
    response = requests.delete(url+"posts/101")

    # ASSERT
    assert response.status_code == status
    assert response.json() == {}


def test_get_method_invalid_id__general_url__expect_empty_response():
    # FIXTURE
    id = "invalid_id"
    url = f"https://jsonplaceholder.typicode.com/"
    status = 404
    expected_result = {}

    # EXERCISE
    response = requests.get(url+f"posts/{id}")

    # ASSERT
    result = response.json()
    assert response.status_code == status
    assert result ==  expected_result
