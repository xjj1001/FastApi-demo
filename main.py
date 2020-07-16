from typing import Optional

from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


#  交互式文档  http://127.0.0.1:8000/docs
#  替代API文档  http://127.0.0.1:8000/redoc

class Item(BaseModel):
    name: str
    price: float
    is_offer: Optional[bool] = None


@app.get("/")
def read_root():
    return {"hello": "world"}  # http://127.0.0.1:8000/  res: {"hello":"world"}


@app.get("/items/{items_id}")
def read_item(items_id: int, q: Optional[str] = None):
    return {"items_id": items_id, "q": q}
    # http://127.0.0.1:8000/items/2?q=10  res: {"items_id":2,"q":"10"}
    # http://127.0.0.1:8000/items/2  res: {"items_id":2,"q":null}


@app.put("/items/{items_id}")
def update_item(items_id: int, item: Item):
    return {"item_name": item.name, "item_id": items_id, "is_offer": item.is_offer}


@app.get("/users/me")
def get_me():
    return "get me"


@app.get("/users/{user_id}")
def get_user(user_id, p):
    return 'get user'

# http://127.0.0.1:8000/users/me?p=666  res: "get me"
# http://127.0.0.1:8000/users/me  res: "get me"
# 如果脑抽把路由设置成这样的话，一定要注意 get_me 和 get_user 的顺序


# 枚举类的使用
from enum import Enum


class ModelName(Enum):
    alexnet = "alexnet"
    resnet = "resnet"
    lenet = "lenet"


@app.get("/model/{model_name}")
def get_model(model_name: ModelName):
    if model_name == ModelName.alexnet:
        return {"model_name": model_name, "message": "Deep Learning FTW!"}
    elif model_name.value == "lenet":
        return {"model_name": model_name, "message": "LeCNN all the images"}
    else:
        return {"model_name": model_name, "message": "Have some residuals"}