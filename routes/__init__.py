from fastapi.responses import FileResponse
from .database import setup_database_post_only_routes


def go_docs(app):
    @app.get("/")
    def home():
        return FileResponse("./assets/html/home.html")

    @app.get("/documentation")
    def documentation():
        return FileResponse("./assets/html/docs.html")

    @app.get('/assets/{file_path:path}')
    def static_assets(file_path):
        return FileResponse(f"./assets/{file_path}")
