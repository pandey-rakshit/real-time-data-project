import time
import random
from src.models import Sale, session


def simulate_and_insert_data():
    items = ["Item_A", "Item_B", "Item_C"]

    while True:
        item = random.choice(items)
        quantity = random.randint(1, 10)
        price = round(random.uniform(10.0, 100.0), 2)

        # Create a new sale record
        sale = Sale(item=item, quantity=quantity, price=price)
        session.add(sale)
        session.commit()

        print(f"Inserted: {item}, {quantity}, {price}, {sale.timestamp}")
        time.sleep(5)  # Wait for 5 seconds before generating the next data point
