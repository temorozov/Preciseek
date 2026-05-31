from parsedoc import parse_pdf
from chunker import chunk_text

def main():
    parsed_pdf = parse_pdf("./testdoc.pdf")
    
    text = " ".join(page["text"] for page in parsed_pdf)
    chunked_text = chunk_text(text, 500, 100)

    print(chunked_text)


if __name__ == "__main__":
    main()
