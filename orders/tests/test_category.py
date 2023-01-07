import pytest
from django.urls import reverse_lazy
from orders.models import Category


@pytest.mark.django_db
def test_create_model_category():
    category = Category.objects.create(name='Happy Category')
    count = Category.objects.count()
    assert category.pk == 1
    assert category.name == 'Happy Category'
    assert count == 1


@pytest.mark.django_db
def test_create_category_api(client):
    url = reverse_lazy('category-list')
    data = {
        'name': 'Happy Category'
    }
    response = client.post(url, data)
    assert response.status_code == 201
    assert response.data['name'] == data['name']


@pytest.fixture
def category():
    Category.objects.create(name='Category')
    Category.objects.create(name='CategoryCategory')


@pytest.mark.django_db
def test_category_list_api(client, category):
    url = reverse_lazy('category-list')
    response = client.get(url)
    assert response.status_code == 200
    assert len(response.data) == 2


@pytest.mark.django_db
def test_category_update_api(client, category):
    category = Category.objects.first()
    url = reverse_lazy('category-detail', args=(category.pk,))
    data = {
        'name': 'My Category'
    }
    response = client.patch(url, data, content_type='application/json')
    assert response.status_code == 200
    assert response.data['name'] == data['name']
    assert response.data['id'] == category.pk
