from django.db import models

class OrderManager(models.Manager):
    def process_purchase(self, post_data, session):
        """
        Securely handles the purchase logic, calculates totals from DB prices,
        and saves relevant data to session for the safe redirect.
        """
        product_id = post_data.get('product_id')
        quantity = int(post_data.get('quantity', 1))
        
        # Securely fetch price from DB instead of relying on form inputs
        product = Product.objects.get(id=product_id)
        current_charge = product.price * quantity
        
        # Save order to DB
        self.create(quantity_ordered=quantity, total_price=current_charge)
        
        # Aggregate totals for ALL combined historical orders
        totals = self.aggregate(
            total_items=models.Sum('quantity_ordered'),
            total_spent=models.Sum('total_price')
        )
        
        # Pass data safely to the view via Session
        session['last_charge'] = float(current_charge)
        session['total_items'] = totals['total_items'] or 0
        session['total_spent'] = float(totals['total_spent'] or 0)

class Product(models.Model):
    description = models.CharField(max_length=45)
    price = models.DecimalField(decimal_places=2, max_digits=5)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Order(models.Model):
    quantity_ordered = models.IntegerField()
    total_price = models.DecimalField(decimal_places=2, max_digits=6)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    # Attach our Fat Model Manager
    objects = OrderManager()