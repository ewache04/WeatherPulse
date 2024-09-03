# app/url_patterns/base_layouts.py
def get_base_layout_patterns(ext='html'):
    return {
        "base": {
            'render': f'base.{ext}',
            'redirect': '/base'
        },

        "loading_indicator": {
            'render': f'loading_indicator.{ext}',
            'redirect': '/loading_indicator'
        },

        "footer": {
            'render': f'footer.{ext}',
            'redirect': '/footer'
        },
        "home_button": {
            'render': f'home_button.{ext}',
            'redirect': '/home_button'
        },
        "top_navbar": {
            'render': f'top_navbar.{ext}',
            'redirect': '/top_navbar'
        },
    }
