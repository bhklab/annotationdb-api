from pydantic import BaseModel, ConfigDict
from typing import Optional


class ATCCode(BaseModel):
    code: str
    description: str


class ATCCodesOutput(BaseModel):
    levels: list[ATCCode]