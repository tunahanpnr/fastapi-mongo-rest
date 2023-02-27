from typing import Dict

import pytest

from app import crud
from app.tests.utils.user import create_mock_signup_user


@pytest.mark.asyncio
async def test_get_user(test_client, get_db):
    mock_user = create_mock_signup_user()
    inserted_id = await crud.user.create(get_db['users'], mock_user)
    db_user = await crud.user.get(get_db['users'], inserted_id)

    assert inserted_id == db_user['_id']


@pytest.mark.asyncio
async def test_get_multi_user(test_client, get_db):
    for i in range(5):
        mock_user = create_mock_signup_user()
        await crud.user.create(get_db['users'], mock_user)

    try:
        result = await crud.user.get_multi(get_db['users'])
    except Exception as e:
        pass
    assert len(result) > 0


@pytest.mark.asyncio
async def test_create_user(test_client, get_db):
    mock_user = create_mock_signup_user()
    inserted_id = await crud.user.create(get_db['users'], mock_user)
    db_user = await crud.user.get(get_db['users'], inserted_id)

    assert inserted_id == db_user['_id']


@pytest.mark.asyncio
async def test_update_user(test_client, get_db):
    mock_user = create_mock_signup_user()
    inserted_id = await crud.user.create(get_db['users'], mock_user)

    update_data = {'username': 'changed'}
    result = await crud.user.update(get_db['users'], inserted_id, update_data)
    assert result


@pytest.mark.asyncio
async def test_remove_user(test_client, get_db):
    mock_user = create_mock_signup_user()
    inserted_id = await crud.user.create(get_db['users'], mock_user)

    result = await crud.user.remove(get_db['users'], inserted_id)
    assert result
