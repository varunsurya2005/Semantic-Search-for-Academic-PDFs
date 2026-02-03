from endee import Endee

INDEX_NAME = "semantic_docs"

client = Endee()
client.delete_index(INDEX_NAME)

print("🗑️ Index deleted successfully")
