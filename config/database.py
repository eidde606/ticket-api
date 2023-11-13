from pymongo.mongo_client import MongoClient

import ssl

client = MongoClient(
    "mongodb+srv://eidde606:edian606@cluster0.h9pamtb.mongodb.net/?retryWrites=true&w=majority",
    ssl=True,
    ssl_ca_certs="path/to/ca-certificate.pem",
)
db = client.TicketDB
collection_name = db["tickets"]
