from fastapi import FastAPI
from api import setup_curd
from routes import go_docs, setup_database_post_only_routes
import uvicorn

app = FastAPI()
go_docs(app)
setup_curd(app)
setup_database_post_only_routes(app)


def run():
    uvicorn.run(app, host="0.0.0.0", port=5300)


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=5300)
