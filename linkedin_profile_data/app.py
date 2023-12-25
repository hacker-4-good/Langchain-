from fastapi import FastAPI 
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
import uvicorn 

class User(BaseModel):
    name: str

from ice_breaker import ice_break

app = FastAPI() 

origins = ['http://localhost:8501']

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post('/process')
def process(user: User):
    person_info, person_pic_url = ice_break(name=user.name)

    return {
        'data':{
            'summary': person_info.summary,
            'interests': person_info.topic_of_interest,
            'facts': person_info.facts,
            'ice_breaker': person_info.ice_breaker, 
            'profile_pic_url': person_pic_url
        }
    }

if __name__=='__main__':
    uvicorn.run('app:app', host='127.0.0.1', port=8000, reload=True)