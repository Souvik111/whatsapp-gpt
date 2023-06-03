from fastapi import FastAPI, Path
import uvicorn
from pydantic import BaseModel
from fun import wachat

app=FastAPI()



@app.get('/')
def index():
    return {'Welcome'}

@app.get('/qna')
async def ask_qna(query: str):
    return "Souvik:  "+wachat(query).replace('\"',' ')


if __name__=='__main__':
    uvicorn.run(app, host='127.0.0.1', port=5000)