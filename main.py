import json
import os
from fastapi import FastAPI
from typing import Optional
import uvicorn
import re

from sqlalchemy import create_engine, text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from pydantic import BaseModel

port = os.environ.get('port')
endpoint = os.environ.get('endpoint')
pg_user = os.environ.get('user')
pg_pass = os.environ.get('password')
pg_db = os.environ.get('db')
pg_schema = os.environ.get('schema')
pg_host = os.environ.get('host')

SQLALCHEMY_DATABASE_URL = f"postgresql://{pg_user}:{pg_pass}@{pg_host}/{pg_db}"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

app = FastAPI()


class Data(BaseModel):
    name: Optional[str] = None
    email: Optional[str] = None
    txt: Optional[str] = None


@app.get("/"+endpoint+"/{q_path:path}")
async def select_get(q_path: str):
    result = await make_q(q_path, 'get')
    return result


@app.post("/"+endpoint+"/{q_path:path}")
async def select_post(q_path: str, data: Data):
    result = await make_q(q_path, 'ins', data=data)
    return result


@app.put("/"+endpoint+"/{q_path:path}")
async def select_patch(q_path: str, data: Data):
    result = await make_q(q_path, 'upd', data=data)
    return result


@app.delete("/"+endpoint+"/{q_path:path}")
async def select_delete(q_path: str):
    result = await make_q(q_path, 'del')
    return result


async def make_q(q_path: str, method: str, data=None):
    pattern = r'(\w+)\/*(\d*)\/*'
    groups = re.findall(pattern, q_path)
    out_path = [group[0] for group in groups]
    if method in ['ins', 'del', 'upd']:
        out_params = [group[1] for group in groups if group[1]]
    else:
        out_params = [group[1] if group[1] else '0' for group in groups]
    json_params = []
    if data is not None:
        json_params.append(f"'{json.dumps(dict(data))}'")

    res_query = f'select * from {pg_schema}.{"_".join(out_path)}_{method}({", ".join([*out_params, *json_params])});'
    with SessionLocal() as session:
        result = session.execute(text(res_query)).all()
        session.commit()

    print(res_query)
    if len(result) == 1:
        return result[0]
    return result


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=int(port))
