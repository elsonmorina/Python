contact_info = {
     "Alice": "555-123",
     "Bob": "234-123"
}

alice_phone =contact_info["Alice"]
print(alice_phone)

contact_info["Alice"] = "123-456"
print(contact_info)


contact_info["Eva"] = "345-345"
print(contact_info)

del contact_info["Bob"]
print(contact_info)

keys = contact_info.keys()
print(keys)

values = contact_info.values()
print(values)

items = contact_info.items()
print(items)
contact_information = {

    "Alice" : {
        "phone_number" : "123-555",
        "email": "alice@gmail.com",
        "birthday": "20/11/2000"
    } ,

    "Bob": {
        "phone_number" : "845-555",
        "email": "bob@gmail.com",
        "birthday": "27/11/2005"
    }
}

print(contact_information)
print(contact_information["Bob"])

