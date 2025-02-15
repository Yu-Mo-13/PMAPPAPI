from config import get_config
from fastapi import APIRouter, Request, HTTPException, status
from authlib.integrations.starlette_client import OAuth, OAuthError

oauth = OAuth()

oauth.register(
  name = "google",
  client_id = get_config("GOOGLE_CLIENT_ID"),
  client_secret = get_config("GOOGLE_CLIENT_SECRET"),
  server_metadata_url = "https://accounts.google.com/.well-known/openid-configuration",
  client_kwargs = {
    "scope": "openid email profile",
    "prompt": "consent"
  },
)

router = APIRouter()

@router.get("/login")
async def login(request: Request):
  redirect_uri = get_config("GOOGLE_CALLBACK_URI")
  return await oauth.google.authorize_redirect(request, redirect_uri)

@router.get("/login/callback")
async def login_callback(request: Request):
  try:
    token = await oauth.google.authorize_access_token(request)
  except OAuthError as e:
    raise HTTPException(
      status_code=status.HTTP_401_UNAUTHORIZED,
      detail="Failed to Authenticate",
    )
  
  user = token.get("userinfo")
  if not user:
    user = await oauth.google.userinfo(token=token)
  
  if not user:
    raise HTTPException(
      status_code=status.HTTP_400_BAD_REQUEST,
      detail="Bad Request",
    )
  
  return {
    "token": token,
    "user": user,
  }