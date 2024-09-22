from fastapi import FastAPI
from routers.application import router as application_router
from routers.password import router as password_router
from routers.account import router as account_router
from routers.passwordwk import router as passwordwk_router
from routers.autoregist import router as autoregist_router
from routers.otpctl import router as otpctl_router
from starlette.middleware.cors import CORSMiddleware

app = FastAPI()

# CORSエラーを回避するための設定
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],)

@app.get("/")
async def root():
    return {"message": "Hello World"}

app.include_router(application_router)
app.include_router(password_router)
app.include_router(account_router)
app.include_router(passwordwk_router)
app.include_router(autoregist_router)
app.include_router(otpctl_router)