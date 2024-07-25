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

    images: list["ProductImage"] = Relationship(back_populates="product")
    storage_id: int | None = Field(default=None, foreign_key="storage.id")
    storage: Storage = Relationship(back_populates="products")


class ProductIn(ProductBase):
    pass


class ProductImageBase(SQLModel):
    url: str


class ProductImage(ProductImageBase, table=True):
    id: int = Field(default=None, primary_key=True)

    product_id: int | None = Field(default=None, foreign_key="product.id")
    product: Product | None = Relationship(back_populates="images")


class ProductImageIn(ProductImageBase):
    pass
