"""file run api. or main file"""

import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from src.infra.http.routes.owner.post import api
from src.infra.http.routes.owner.update import update_router
from src.infra.http.routes.owner.get import router_get

from src.infra.http.routes.veichle.post import router_post
from src.infra.http.routes.veichle.get import veichle_get
from src.infra.http.routes.veichle.update import router_pacth
from src.infra.http.routes.veichle.put import router_put

from src.infra.http.routes.agent.post import router_post_agent
from src.infra.http.routes.agent.login import router_login
from src.infra.http.routes.agent.get import agent_get
from src.infra.http.routes.admin.post import router_post as admin_post

from src.infra.models import *



app = FastAPI()
app.title = "Board Manager"
app.description = "API manager system for board manager"

app.include_router(api)
app.include_router(router_get)
app.include_router(update_router)
app.include_router(router_post)
app.include_router(router_put)
app.include_router(router_pacth)
app.include_router(veichle_get)
app.include_router(router_post_agent)
app.include_router(router_login)
app.include_router(agent_get)
app.include_router(admin_post)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
    allow_credentials=True
)

@app.get("/")
async def hello():
    return {
        "msg": "api board manager on air"
    }

if __name__ == "__main__":
    uvicorn.run(app, 
        host="0.0.0.0",
        port=1818
    )
