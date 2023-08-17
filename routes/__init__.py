from fastapi.responses import FileResponse


def go_docs(app):
    @app.get("/")
    def redirect_docs():
        return FileResponse("./assets/html/home.html")

    @app.get('/assets/{file_path:path}')
    def static_assets(file_path):
        return FileResponse(f"./assets/{file_path}")
