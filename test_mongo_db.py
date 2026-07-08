from pymongo import MongoClient
uri = "mongodb+srv://username:password@networksecurity.u2sguaa.mongodb.net/?appName=NetworkSecurity"
client = MongoClient(uri)
try:
    client.admin.command("ping")
    print("Connected successfully")
    client.close()

except Exception as e:
    raise Exception(
        "The following error occurred: ", e)