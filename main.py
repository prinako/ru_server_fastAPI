from fastapi import FastAPI

app = FastAPI()

@app.get('/')
def api():
    return 'jjj'
