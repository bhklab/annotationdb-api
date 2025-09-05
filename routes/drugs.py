from fastapi import APIRouter 
from dotenv import load_dotenv
from models.drug import Drug


load_dotenv(override=True)

router = APIRouter(prefix="/drugs")  # Adding email part of route


@router.post("/many")
async def email_director(drugs: list[str]):

