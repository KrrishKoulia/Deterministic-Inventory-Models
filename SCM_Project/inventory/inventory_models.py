from typing import Optional , Literal
from pydantic import BaseModel ,Field

class InventoryParams(BaseModel):
    """Basic parameter for inventory operations."""
    D: float = Field(2000, gt = 0, description = 'Annual Demand (units per year)')
    T_total: int = Field(365, ge = 1,description = 'Data in the simulation horizon')
    LD: int = Field(0,ge = 0,description = 'Lead Time (days))')
    T: int = Field(10,ge = 0,description = 'Review Perriod (days))')
    Q: int = Field(0,ge = 0,description = 'Order Quanitity (units))')
    initial_ioh: float = Field(0,ge = 0,description = 'Initial Inventory on Hand (units)')