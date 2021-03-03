"""Review learning information"""

from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter()

class ReviewInfo(BaseModel):
    number_of_reviews: int
    neighborhood: str

@router.post('/review_info')
async def review_neighborhood(info: ReviewInfo):
    result = "The number of review is: " + str(info.number_of_reviews) + " The neighborhood is: " + info.neighborhood
    return {"Information on review and neighborhood ": result}