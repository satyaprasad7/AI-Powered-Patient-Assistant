from dotenv import load_dotenv
import os

load_dotenv()

from langchain_core.documents import Document
from langchain_community.vectorstores import FAISS
from langchain_openai import OpenAIEmbeddings


class VectorService:

    def __init__(self):

        with open(
            "app/data/medical_kb.txt",
            "r",
            encoding="utf-8"
        ) as f:
            text = f.readlines()

        docs = [
            Document(page_content=line.strip())
            for line in text
            if line.strip()
        ]

        embeddings = OpenAIEmbeddings()

        self.db = FAISS.from_documents(
            docs,
            embeddings
        )

    def search(self, query):

        return self.db.similarity_search(
            query,
            k=2
        )