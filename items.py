from fastapi import APIRouter, Path

router = APIRouter(prefix="/item")

@router.get("/")
def items():
    return ['item1', 'item2', 'item3']


@router.get("/latest")
def get_latest_item(item_id:int):
    return {'item':{'id':'0', 'name': 'latest'}}

@router.get("/{item_id}")
def get_item_by_id(item_id:Annotated[int, Path(ge=1, le=1000)]):
    return {'item':{"id": item_id}}
