from endee import Endee
from embeddings import generate_embedding

INDEX_NAME = "semantic_docs"

def semantic_search(query, top_k=3):
    query = query.strip()
    if not query:
        return []

    query_vector = generate_embedding(query)
    if query_vector is None:
        return []

    index = Endee().get_index(INDEX_NAME)

    return index.query(
        vector=query_vector,
        top_k=top_k
    )

if __name__ == "__main__":
    print("\n🔍 Endee Semantic Search")
    print("Type your query (type 'exit' to quit)\n")

    while True:
        query = input("Query: ")

        if query.lower() == "exit":
            print("👋 Exiting")
            break

        results = semantic_search(query)

        if not results:
            print("⚠️ No results found\n")
            continue

        for res in results:
            print(f"\nScore: {res['similarity']:.4f}")
            print(res['meta']['text'])
