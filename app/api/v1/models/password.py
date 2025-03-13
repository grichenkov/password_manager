from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column
from app.api.utils.sqlalchemy.base_db_model import BaseDBModel
from app.api.utils.sqlalchemy.annotated_fields import (
    integer_id,
    created_at_datetime,
    updated_at_datetime,
)


class PasswordEntryModel(BaseDBModel):
    __tablename__ = "passwords"
    __table_args__ = {"schema": "cheers_schema"}

    id: Mapped[integer_id]
    service_name: Mapped[str] = mapped_column(
        String, unique=True, nullable=False
    )
    encrypted_password: Mapped[str] = mapped_column(String, nullable=False)

    created_at: Mapped[created_at_datetime]
    updated_at: Mapped[updated_at_datetime]
