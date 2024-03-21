from use_cases.book import CreateBookUseCase, GetBookUseCase
from reber.entities.book import BookCreate


class GetBookController:
    def __init__(self, use_case: GetBookUseCase):
        self.use_case = use_case

    async def get(self, book_id) -> tuple[dict, int]:
        book = await self.use_case.execute(book_id)
        if not book:
            return {"detail": "Book not found"}, 404

        return book, 200


class CreateBookController:
    def __init__(self, use_case: CreateBookUseCase):
        self.use_case = use_case

    async def create(self, book: dict) -> tuple[dict, int]:
        book_instance = BookCreate(**book)
        return await self.use_case.execute(book_instance), 201
