from pymongo.mongo_client import MongoClient
import certifi

ca = certifi.where()

uri = "mongodb+srv://bickyjha055_db_user:<add_password>@cluster0.7elfao1.mongodb.net/?retryWrites=true&w=majority"

try:
    client = MongoClient(
        uri,
        tls=True,
        tlsCAFile=ca
    )

    client.admin.command('ping')
    print("✅ Successfully connected to MongoDB Atlas!")

except Exception as e:
    print("❌ Connection Error:")
    print(e)