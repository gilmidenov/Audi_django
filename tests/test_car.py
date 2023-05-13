from django.test import TestCase
from market.models import Car, Purchase, Order


class PurchaseTest(TestCase):
    def setUp(self):
        Car.objects.create(name="RS 6 AVANT")
        Car.objects.create(name="RS 6 AVANT")
        Car.objects.create(name="RS 4 AVANT")

    def test_car_create(self):
        self.assertEqual(Car.objects.all().count(), 3)
        car = Car.objects.get(name="RS 4 AVANT")
        self.assertEqual(car.name, "RS 4 AVANT")

    def test_car_left_function(self):
        car = Car.objects.get(name="RS 4 AVANT")
        Purchase.objects.create(car=car)
        Purchase.objects.create(car=car)
        Purchase.objects.create(car=car)

        Order.objects.create(car=car)

        self.assertEqual(car.car_left(), 2)

    def test_car_orders_by_client(self):
        car = Car.objects.get(name="RS 4 AVANT")
        Purchase.objects.create(car=car)
        Purchase.objects.create(car=car)
        Purchase.objects.create(car=car)

        url = f"/buy_car/{car.id}"
        response = self.client.post(url, {
            "name": "Adilzhana",
            "email": "gilmidenov@gmail.com",
            "phone": "87878564435"
        }
        )
        self.assertEqual(response.status_code, 302)
        self.assertEqual(car.car_left(), 2)






