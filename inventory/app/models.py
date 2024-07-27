from sqlmodel import Field, Relationship, SQLModel
from pydantic import computed_field


class StorageBase(SQLModel):
    name: str
    description: str | None
    address: str
    phone_number: str
    capacity: int
    current_stock: int


class Storage(StorageBase, table=True):
    id: int | None = Field(default=None, primary_key=True)

    products: list["Product"] = Relationship(back_populates="storage")

    @computed_field
    def is_full(self) -> bool:
        return True if self.capacity <= self.current_stock else False


class StorageCreate(StorageBase):
    pass


class StoragePublic(StorageBase):
    id: int
    products: list["ProductStoragePublic"]


class StoragesPublic(StorageBase):
    id: int


class ProductBase(SQLModel):
    name: str
    quantity: int
    price: float
    weight: int


class Product(ProductBase, table=True):
    id: int | None = Field(default=None, primary_key=True)

    storage_id: int | None = Field(default=None, foreign_key="storage.id")
    storage: Storage = Relationship(back_populates="products")


class ProductCreate(ProductBase):
    pass


class ProductStoragePublic(ProductBase):
    id: int


class ProductPublic(ProductBase):
    id: int
    storage: Storage


class ProductImageBase(SQLModel):
    url: str


class ProductImage(ProductImageBase, table=True):
    id: int | None = Field(default=None, primary_key=True)

    product_id: int | None = Field(default=None, foreign_key="product.id")
