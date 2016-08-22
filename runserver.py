from vendor import create_app
app = create_app()
app.run('192.168.33.33', 8000, debug=True)
