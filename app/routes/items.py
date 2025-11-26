from fastapi import APIRouter, Depends, HTTPException, status, Body
from sqlmodel import Session
from typing import List


from app.database import get_db
from app.schemas.item import ItemCreate, ItemResponse, ItemUpdate
from app.services.item_service import ItemService
from app.models.item import Item

router = APIRouter(prefix="/items", tags=["items"])

MAX_ITEMS_PER_PAGE = 1000


@router.get("/", response_model=List[ItemResponse])
def get_items(
    skip: int = 0, limit: int = 100, db: Session = Depends(get_db)
) -> List[Item]:
    """Récupère la liste des items avec pagination."""
    return ItemService.get_all(db, skip, limit)


@router.post("/", response_model=ItemResponse, status_code=status.HTTP_201_CREATED)
def create_item(
    item_data: ItemCreate = Body(...), db: Session = Depends(get_db)
) -> Item:
    """Creates a new item in the database.

    Accepts item data and stores the new item, returning the created item.

    Args:
        item_data (ItemCreate): The data for the item to create.
        db (Session): The database session dependency.

    Returns:
        ItemResponse: The created item.
    """
    return ItemService.create(db, item_data)


@router.get("/{item_id}", response_model=ItemResponse)
def get_item(item_id: int, db: Session = Depends(get_db)) -> Item:
    """Retrieves a single item by its ID.

    Returns the item if found, otherwise raises a 404 error.

    Args:
        item_id (int): The ID of the item to retrieve.
        db (Session): The database session dependency.

    Returns:
        ItemResponse: The requested item.

    Raises:
        HTTPException: If the item is not found.
    """
    if item := ItemService.get_by_id(db, item_id):
        return item
    else:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Item with id {item_id} not found",
        )


@router.put("/{item_id}", response_model=ItemResponse)
def update_item(
    item_id: int, item_data: ItemUpdate = Body(...), db: Session = Depends(get_db)
) -> Item:
    """Updates an existing item with new data.

    Returns the updated item if found, otherwise raises a 404 error.

    Args:
        item_id (int): The ID of the item to update.
        item_data (ItemUpdate): The new data for the item.
        db (Session): The database session dependency.

    Returns:
        ItemResponse: The updated item.

    Raises:
        HTTPException: If the item is not found.
    """
    if item := ItemService.update(db, item_id, item_data):
        return item
    else:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Item with id {item_id} not found",
        )


@router.delete("/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_item(item_id: int, db: Session = Depends(get_db)) -> None:
    """Deletes an item by its ID.

    Removes the item from the database if it exists, otherwise raises a 404 error.

    Args:
        item_id (int): The ID of the item to delete.
        db (Session): The database session dependency.

    Raises:
        HTTPException: If the item is not found.
    """
    deleted = ItemService.delete(db, item_id)
    if not deleted:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Item with id {item_id} not found",
        )
