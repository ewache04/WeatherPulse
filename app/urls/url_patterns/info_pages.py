# app/url_patterns/info_pages.py
def get_info_pages(ext='html'):
    return {

        "our_team": {
            'render': f'info_templates/our_team/our_team.{ext}',
            'redirect': '/our_team'
        },
        "about": {
            'render': f'info_templates/about.{ext}',
            'redirect': '/about'
        },
    }
