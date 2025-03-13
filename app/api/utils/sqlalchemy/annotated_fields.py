from datetime import UTC, datetime
from typing import Annotated

from sqlalchemy import DateTime, func, text
from sqlalchemy.dialects.postgresql import TIMESTAMP
from sqlalchemy.orm import mapped_column

dt_utcnow = Annotated[
    TIMESTAMP,
    mapped_column(
        TIMESTAMP(timezone=True),
        nullable=False,
        server_default=text("timezone('utc', now())"),
    ),
]

dt_with_tz = Annotated[
    TIMESTAMP, mapped_column(TIMESTAMP(timezone=True), nullable=False)
]

integer_id = Annotated[
    int, mapped_column(primary_key=True, nullable=False, autoincrement=True)
]

created_at_datetime = Annotated[
    datetime,
    mapped_column(
        DateTime(timezone=True), server_default=func.now(), nullable=False
    ),
]

updated_at_datetime = Annotated[
    datetime | None,
    mapped_column(
        DateTime(timezone=True),
        onupdate=lambda: datetime.now(tz=UTC),
        nullable=True,
        server_default=func.now(),
    ),
]

deleted_at_datetime = Annotated[
    datetime | None, mapped_column(DateTime(timezone=True), nullable=True)
]
