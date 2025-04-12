import re

class UrlService():
    
    @staticmethod
    async def is_url_like(text: str) -> bool:
        pattern = (
            r'^(https?:\/\/)?'
            r'([a-zA-Z0-9-]+\.)+[a-zA-Z]{2,}'
            r'(\/[^\s]*)?'
            r'(\?[^\s]*)?'            
            r'(#[^\s]*)?$'
        )
        return re.fullmatch(pattern, text) is not None

