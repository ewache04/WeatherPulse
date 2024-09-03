# app.py

def create_app():
    from app import create_app

    application = create_app()

    return application


if __name__ == '__main__':
    app = create_app()

    # Attempt to start the server on port 8000 first
    try:
        app.run(debug=True, port=8000)
    except OSError as e:
        print(f"Port 8000 is unavailable: {e}. Trying port 5000...")
        try:
            app.run(debug=True, port=5000)
        except OSError as e:
            print(f"Port 5000 is also unavailable: {e}. Please check your port settings.")
