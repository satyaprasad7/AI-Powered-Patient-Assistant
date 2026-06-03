from app.services.vector_service import VectorService

class MedicalFAQ:

    def __init__(self):

        self.vector = VectorService()

    def answer(self, question):

        docs = self.vector.search(question)

        return "\n".join(
            [d.page_content for d in docs]
        )