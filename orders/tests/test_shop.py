import pytest
from django.urls import reverse_lazy
from orders.models import Shop


@pytest.mark.django_db
def test_create_model_shop():
    shop = Shop.objects.create(name='Happy Shop')
    count = Shop.objects.count()
    assert shop.pk == 1
    assert shop.name == 'Happy Shop'
    assert count == 1


@pytest.mark.django_db
def test_create_shop_api(client):
    url = reverse_lazy('shop-list')
    data = {
        'name': 'Happy Shop'
    }
    response = client.post(url, data)
    assert response.status_code == 201
    assert response.data['name'] == data['name']


@pytest.fixture
def shops():
    Shop.objects.create(name='Shop')
    Shop.objects.create(name='ShopShop')


@pytest.mark.django_db
def test_shop_list_api(client, shops):
    url = reverse_lazy('shop-list')
    response = client.get(url)
    assert response.status_code == 200
    assert len(response.data) == 2


@pytest.mark.django_db
def test_shop_update_api(client, shops):
    shop = Shop.objects.first()
    url = reverse_lazy('shop-detail', args=(shop.pk,))
    data = {
        'name': 'My Shop'
    }
    response = client.patch(url, data, content_type='application/json')
    assert response.status_code == 200
    assert response.data['name'] == data['name']
    assert response.data['id'] == shop.pk
