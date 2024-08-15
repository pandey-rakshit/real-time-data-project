import pandas as pd
from src.models import Sale, session


def fetch_and_process_data():
    # Query the latest 10 records
    sales = session.query(Sale).order_by(Sale.timestamp.desc()).limit(10).all()

    # Convert to DataFrame
    data = {
        "id": [sale.id for sale in sales],
        "item": [sale.item for sale in sales],
        "quantity": [sale.quantity for sale in sales],
        "price": [sale.price for sale in sales],
        "timestamp": [sale.timestamp for sale in sales],
    }
    df = pd.DataFrame(data)

    # Example processing: calculate total sales value
    df["total_value"] = df["quantity"] * df["price"]

    print(df)
    return df
