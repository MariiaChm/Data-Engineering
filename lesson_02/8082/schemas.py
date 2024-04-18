sales_schema = {
    "type": "record",
    "name": "Sales",
    "fields": [
        {"name": "client", "type": "string"},
        {"name": "purchase_date", "type": "string"},
        {"name": "product", "type": "string"},
        {"name": "price", "type": "float"}
    ]
}