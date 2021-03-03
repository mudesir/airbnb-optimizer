from fastapi import FastAPI 
from fastapi import APIRouter
from fastapi.middleware.cors import CORSMiddleware
import uvicorn
from app import predict, review

description = """

    This our FastAPI DS API. To use this api follow the 
    instrucion. A predicted price along with top features
    will show in a JSON format. Below is an example on how
    to use it interactively.

    To Use These Interactive Docs:
        - Click on an endpoint below
        - Click the **Try it out** button
        - Edit the Request body or any parameters
        - Click the **Execute** button
        - Scroll down to see the Server response code & Details

<img src="https://getpaidforyourpad.com/wp-content/uploads/2016/06/Airbnb-Hosting-in-Washington-DC-2.jpg">
"""


app = FastAPI(
    title='AIRBNB-OPTIMIZER 🏡 🛌',
    description=description,
    docs_url='/',

)

# tags to show on FatsAPI 
#app.include_router(db.router, tags=['Database'])
app.include_router(predict.router, tags=['Data Science and Machine Learning'])
app.include_router(review.router, tags=['Information'])

app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
    allow_credentials=True,
    allow_methods=['*'],
    allow_headers=['*'],
)



if __name__ == '__main__':
    uvicorn.run(app)