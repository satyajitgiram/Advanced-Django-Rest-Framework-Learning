from locust import HttpUser, task, between 
from random import randint

class WebsiteUser(HttpUser):
    wait_time = between(1, 5)

    #viewing products
    @task(2)
    def view_products(self):
        collection_id = randint(1, 5)
        self.client.get(f'/store/products/?collecton_id={collection_id}', name='/store/products')

    #Viewing product Details
    @task(4)
    def view_product(self):
        product_id = randint(1, 10)
        self.client.get(f'/store/products/{product_id}/', name='/store/products/:id')

    #Add product to cart
    @task(1)
    def add_to_cart(self):
        product_id = randint(1, 10)
        self.client.post(f'/store/carts/{self.cart_id}/items/', json={'product_id':product_id, 'quantity':1}, name='/store/carts/:cart_id/items')

    def on_start(self):
        response = self.client.post('/store/carts/', name='/store/carts/')
        result = response.json()
        self.cart_id = result['id'] 