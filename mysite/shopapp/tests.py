from random import choices
from string import ascii_letters

from django.contrib.auth.models import User, Permission
from django.contrib.contenttypes.models import ContentType
from django.test import TestCase
from django.urls import reverse

from shopapp.models import Product, Order
from shopapp.utils import add_two_numbers


class AddTwoNumbersTestCase(TestCase):
    def test_add_two_numbers(self):
        result = add_two_numbers(2, 3)
        self.assertEquals(result, 5)


class ProductCreateViewTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpass')
        self.user.user_permissions.add(Permission.objects.get(codename='add_product'))
        self.product_name = "".join(choices(ascii_letters, k=10))
        Product.objects.filter(name=self.product_name).delete()

    def test_create_product(self):
        self.client.force_login(self.user)
        response = self.client.post(
            reverse("shopapp:product_create"),
            {
                "name": "Table",
                "price": "123.45",
                "description": "A good table",
                "discount": "10",
            }
        )
        self.assertRedirects(response, reverse("shopapp:products_list"))


class ProductDetailsViewTestCase(TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.user = User.objects.create(username="testuser")
        cls.product = Product.objects.create(
            name="Best Product",
            created_by=cls.user
        )

    @classmethod
    def tearDownClass(cls):
        cls.product.delete()
        cls.user.delete()

    def test_get_product(self):
        response = self.client.get(
            reverse('shopapp:product_details', kwargs={"pk": self.product.pk})
        )
        self.assertEquals(response.status_code, 200)

    def test_get_product_and_check_content(self):
        response = self.client.get(
            reverse('shopapp:product_details', kwargs={"pk": self.product.pk})
        )
        self.assertContains(response, self.product.name)


class OrderDetailViewTestCase(TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.user = User.objects.create_user(username='testuser', password='testpass')
        content_type = ContentType.objects.get_for_model(Order)
        permission = Permission.objects.get(content_type=content_type, codename='view_order')
        cls.user.user_permissions.add(permission)

    @classmethod
    def tearDownClass(cls):
        cls.user.delete()

    def setUp(self):
        self.order = Order.objects.create(
            delivery_address='Test Address',
            promo_code='TEST123',
            user=self.user
        )
        self.client.login(username='testuser', password='testpass')

    def tearDown(self):
        self.order.delete()

    def test_order_details(self):
        print(self.user.get_all_permissions())
        url = reverse('shopapp:order_detail', kwargs={'pk': self.order.pk})
        response = self.client.get(url)

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, self.order.delivery_address)
        self.assertContains(response, self.order.promo_code)
        self.assertEqual(response.context['order'].pk, self.order.pk)


class OrdersExportTestCase(TestCase):
    fixtures = [
        "users-fixture.json",
        "orders-fixture.json",
        "products-fixture.json",
    ]

    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.credentials = dict(username="Tester", password="qwerty")
        cls.user = User.objects.create_user(**cls.credentials)
        cls.user.is_staff = True
        cls.user.save()
        permissions = Permission.objects.get(codename="view_order")
        cls.user.user_permissions.add(permissions)

    @classmethod
    def tearDownClass(cls):
        cls.user.delete()
        super().tearDownClass()

    def setUp(self):
        self.client.login(**self.credentials)

    def test_export_orders(self):
        response = self.client.get(reverse('shopapp:orders_export'))
        self.assertEqual(response.status_code, 200)

        orders = Order.objects.all()
        expected_data = []
        for order in orders:
            order_data = {
                'order_id': order.id,
                'address': order.delivery_address,
                'promo_code': order.promo_code,
                'user_id': order.user.id,
                'product_ids': [product.id for product in order.products.all()]
            }
            expected_data.append(order_data)

        self.assertEqual(response.json(), {'orders': expected_data})
