import chromadb 

client = chromadb.PersistentClient(path="./chroma_data")



def add_chunks(chunks, embeddings, collection_name):

    collection = client.get_or_create_collection(name=collection_name)

    collection.add(
        documents = chunks,
        embeddings = embeddings,
        ids = [f"chunk_{i}" for i in range(len(chunks))]
    )
    

def search(query_embedding, collection_name, n_results):
    collection = client.get_or_create_collection(name=collection_name)

    results = collection.query(
        query_embeddings = [query_embedding],
        n_results = n_results
    )

    return results["documents"][0]