from app import db, app
from app import Item  # Replace 'YourModelName' with your model's class name

# Example records
items = [
    Item(name="iphone 10", price=100, barcode="123456789012", description="A versatile gadget for everyday use."),
    Item(name="Mac Book", price=200, barcode="234567890123", description="A premium gadget with advanced features."),
    Item(name="Car", price=50, barcode="345678901234", description="A handy tool for home repairs."),
    Item(name="Iron", price=300, barcode="456789012345", description="A state-of-the-art kitchen appliance."),
    Item(name="Washing machine", price=25, barcode="567890123456", description="An affordable and stylish accessory.")
]

# Add and commit to the database
with app.app_context():
    db.session.add_all(items)
    db.session.commit()

print("Dummy data inserted successfully!")
