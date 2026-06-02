from typing import List

def chunk_text(text: str, chunk_size: int, overlap: int) -> List[str]:
    chunked_text: List[str] = []

    start: int = 0
    while start < len(text):
        next_start = start + chunk_size - overlap
        end: int = start + chunk_size

        last_space: int = text.rfind(" ", start, end)
        if last_space != -1:
            end = last_space

        chunked_text.append(text[start:end])
        start = next_start

    return chunked_text