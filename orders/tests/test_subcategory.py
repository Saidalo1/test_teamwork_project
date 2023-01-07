import pytest
from django.urls import reverse_lazy
from orders.models import SubCategory, Category


@pytest.mark.django_db
def test_create_model_subcategory():
    # category for subcategory
    temporarily = Category.objects.create(name="category 1")
    subcategory = SubCategory.objects.create(name='Happy SubCategory', category=temporarily)
    count = SubCategory.objects.count()
    assert subcategory.pk == 1
    assert subcategory.name == 'Happy SubCategory'
    assert count == 1


@pytest.mark.django_db
def test_create_subcategory_api(client):
    temporarily = Category.objects.create(name="category 2")
    url = reverse_lazy('subcategory-list')
    data = {
        'name': 'Happy SubCategory',
        'category': temporarily.id
    }
    response = client.post(url, data)
    print(response.data, response)
    assert response.status_code == 201
    assert response.data['name'] == data['name']


@pytest.fixture
def subcategory():
    temporarily = Category.objects.create(name="category 1")
    SubCategory.objects.create(name='SubCategory', category=temporarily)
    SubCategory.objects.create(name='SubCategorySubCategory', category=temporarily)


@pytest.mark.django_db
def test_subcategory_list_api(client, subcategory):
    url = reverse_lazy('subcategory-list')
    response = client.get(url)
    assert response.status_code == 200
    assert len(response.data) == 2


@pytest.mark.django_db
def test_subcategory_update_api(client, subcategory):
    subcategory = SubCategory.objects.first()
    url = reverse_lazy('subcategory-detail', args=(subcategory.pk,))
    data = {
        'name': 'My SubCategory',
        'category_id': 1
    }
    response = client.patch(url, data, content_type='application/json')
    assert response.status_code == 200
    assert response.data['name'] == data['name']
    assert response.data['id'] == subcategory.pk
