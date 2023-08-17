from fastapi import FastAPI
from api import setup_curd
from routes import go_docs
import uvicorn

app = FastAPI()
setup_curd(app)
go_docs(app)


def run():
    uvicorn.run(app, host="0.0.0.0", port=5300)


if __name__ == "__main__":
    run()
