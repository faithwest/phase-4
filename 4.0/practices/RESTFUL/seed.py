from app import app, db
from models import Customer,Author,Book
from __future__ import print_function



def seed_data():
# Create customers
    customer1 = Customer(name="Jemohn", email="jemohn@gmail.com", phone='0789234567')
    customer1 = Customer(name="mon", email="mon@gmail.com", phone='0783234567')
    db.session.add(customer1)
    db.session.add(customer2)
    # Commit the changes
    db.session.commit()
    print("Customer1 name:", customer1.name)


    # Create authors
    author1 = Author(name="Tom", yob="1980")
    author2 = Author(name="Graham", yob="1997")
    authors = [author1, author2]
    db.session.add(author1)
    db.session.add_(author2)
    db.session.commit()



    # Create books with related author and customer information
    book1 = Book(title="A mystery about a boy.", author_id=author2.id,published_year=2010 ,price=3278, qty_in_stock=7)
    book2 = Book(title="The bad Boy", author_id=author1.id,published_year=2013 ,price=3245, qty_in_stock=9)

    db.session.add(book1)
    db.session.add_(book2)
    db.session.commit()
