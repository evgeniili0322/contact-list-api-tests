from dataclasses import dataclass


@dataclass
class ContactData:
    first_name: str = 'John'
    last_name: str = 'Doe'
    birthdate: str = '1970-01-01'
    email: str = 'jdoe@fake.com'
    phone: str = '8005555555'


contact_data = ContactData()
