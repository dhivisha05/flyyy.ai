# ─── Pydantic Schema ───
from pydantic import BaseModel, Field
from typing import Optional


# This is the rule for a single item
class BOQItem(BaseModel):
    description: str = Field(description="The name/description of the material")
    brand: str = Field(description="The manufacturer or brand", default="Generic")
    quantity: float = Field(description="The number amount")
    unit: str = Field(description="How it is measured (like kg, meters, pieces)")
    category: str = Field(description="EPC industry category", default="uncategorized")

# This is the rule for the whole list
class BOQList(BaseModel):
    items: list[BOQItem]