import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from src.routes.users import user_router
 
app = FastAPI(title="Simple FastAPI Backend")

app.include_router(user_router)
app.add_middleware(
			CORSMiddleware,
			allow_origins=["*"],
			allow_credentials=False,
			allow_methods=["*"],
			allow_headers=["*"],
		)
if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
