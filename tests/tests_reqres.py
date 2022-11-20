from requests import Response
from pytest_voluptuous import S
from schemas import schemas
from utils.base_session import reqres_session


def test_get_single_user():
    result = reqres_session().get(
        url='/api/users/2'
    )

    assert result.status_code == 200
    assert result.json() == S(schemas.get_single_user_schema)


def test_create_user():
    name = 'Chikchirik'
    job = 'Potato'

    result = reqres_session().post(
        url='/api/users',
        json={
            'name': name,
            'job': job
        }
    )

    assert result.status_code == 201
    assert result.json() == S(schemas.create_user_schema)
    assert result.json()['name'] == name
    assert result.json()['job'] == job


def test_update_user():
    name = 'Jared'
    job = 'vampire'

    result: Response = reqres_session().put(
        url='/api/users/2',
        json={
            'name': name,
            'job': job
        }
    )

    assert result.status_code == 200
    assert result.json()['name'] == name
    assert result.json()['job'] == job
    assert result.json() == S(schemas.update_user_schema)


def test_register_successful():
    email = 'eve.holt@reqres.in'
    password = 'pistol'

    result: Response = reqres_session().post(
        url='/api/register',
        json={
            'email': email,
            'password': password
        }
    )

    assert result.status_code == 200
    assert result.json() == S(schemas.register_successful_schema)


def test_login_successful():
    email = 'eve.holt@reqres.in'
    password = 'cityslicka'

    result: Response = reqres_session().post(
        url='/api/login',
        json={
            'email': email,
            'password': password
        }
    )

    assert result.status_code == 200
    assert result.json() ==S(schemas.login_successful_schema)