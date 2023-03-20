from enum import Enum


class DocumentFormat(Enum):
    DOCX = "docx"
    EPUB = "epub"
    ODT = "odt"
    MD = "markdown"
    RTF = "rtf"
    HTML = "html"

    @staticmethod
    def int_to_DocumentFormat(value: int):
        match value:
            case 0: return DocumentFormat.DOCX
            case 1: return DocumentFormat.EPUB
            case 2: return DocumentFormat.ODT
            case 3: return DocumentFormat.MD
            case 4: return DocumentFormat.RTF
            case 5: return DocumentFormat.HTML
            case _: return None
