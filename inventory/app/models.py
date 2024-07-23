from sqlmodel import Field, Relationship, SQLModel


class StorageBase(SQLModel):
    name: str
    capacity: int


class Storage(StorageBase, table=True):
    id: int | None = Field(default=None, primary_key=True)

    products: list["Product"] = Relationship(back_populates="storage")


class StorageIn(StorageBase):
    pass


class ProductBase(SQLModel):
    name: str
    quantity: int


class Product(ProductBase, table=True):
    id: int | None = Field(default=None, primary_key=True)

    storage_id: int | None = Field(default=None, foreign_key="storage.id")
    storage: Storage | None = Relationship(back_populates="products")


class ProductIn(ProductBase):
    pass
