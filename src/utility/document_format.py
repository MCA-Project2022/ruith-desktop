from enum import Enum


class DocumentFormat(Enum):
    DOCX = "docx"
    EPUB = "epub"

    @staticmethod
    def int_to_DocumentFormat(value: int):
        match value:
            case 0: return DocumentFormat.DOCX
            case 1: return DocumentFormat.EPUB
            case _: return None
