from parsedoc import parse_pdf
from chunker import chunk_text
from embeddings import get_embeddings
from vectorstore import add_chunks
from answerer import answer

def main():
    parsed_pdf = parse_pdf("./testdoc.pdf")
    
    text = " ".join(page["text"] for page in parsed_pdf)
    chunked_text = chunk_text(text, 500, 100)

    vectors = get_embeddings(chunked_text)

    collection_name = "some_collection"
    add_chunks(chunked_text, vectors, collection_name)
    print(answer("What is harmonic?", collection_name))

if __name__ == "__main__":
    main()
