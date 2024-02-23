from typing import Optional, List
from beanie import Document
from pydantic import BaseModel, Field


class Cocktail(Document):
    class Settings:
        name = "recipes"

    name: str
    ingredients: List["Ingredient"]
    instructions: List[str]


class Ingredient(BaseModel):
    name: str
    quantity: Optional["IngredientQuantity"] = None


class IngredientQuantity(BaseModel):
    quantity: Optional[str] = None
    unit: Optional[str] = None


class IngredientAggregation(BaseModel):
    """ A model for an ingredient count. """

    id: str = Field(None, alias="_id")
    total: int


Cocktail.model_rebuild()
Ingredient.model_rebuild()
