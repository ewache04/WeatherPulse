# app/url_patterns/static_files.py
def get_static_files():
    return {
        "static": {
            'script': 'js/script.js',
            'styles': 'css/styles.css',
            'images': {
                'background_images': '/images/background_images',
                'team_members': '/images/team_members',
            }
        }
    }
