# app/urls/urls_patterns
from app.urls.url_patterns.assistant_templates import get_assistant_templates
from app.urls.url_patterns.base_layouts import get_base_layout_patterns
from app.urls.url_patterns.info_pages import get_info_pages
from app.urls.url_patterns.media_files import get_media_files
from app.urls.url_patterns.static_files import get_static_files
from app.urls.url_patterns.weather_templates import get_weather_templates
from utils.sessions.session_utils import create_session


def set_urls_patterns():
    ext = 'html'
    return {
        **get_base_layout_patterns(ext),
        **get_weather_templates(ext),
        **get_info_pages(ext),
        **get_assistant_templates(ext),
        **get_static_files(),
        **get_media_files(),
        "index": {
            'render': f'index.{ext}',
            'redirect': '/'
        },
    }


def initialize_urls_patterns():
    url_patterns = set_urls_patterns()
    create_session('url_patterns', url_patterns)
    return url_patterns
