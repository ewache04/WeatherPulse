# app/url_patterns/media_files.py
def get_media_files():
    return {
        "media": {
            'documents': 'documents',
            'photos': 'photos',
            'videos': 'videos'
        }
    }
