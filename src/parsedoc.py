import pymupdf
from typing import List

def parse_pdf(file_path: str) -> List[dict]:
    pages: List[dict] = []

    with pymupdf.open(file_path) as doc:
        for page in doc:
            pages.append({"text": page.get_text("text"), "page_number": page.number})

    return pages