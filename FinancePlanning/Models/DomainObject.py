from sqlalchemy.orm import Mapped, mapped_column, DeclarativeBase, MappedAsDataclass


class DomainObject(MappedAsDataclass, DeclarativeBase):
    object_id: Mapped[int] = mapped_column(primary_key=True)
