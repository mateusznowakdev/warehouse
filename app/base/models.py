from datetime import datetime, timezone

from sqlalchemy import DateTime, Dialect, TypeDecorator


class UTCDateTime(TypeDecorator):
    """Custom DateTime class for timezone-aware UTC datetimes in SQLite."""

    impl = DateTime
    cache_ok = True

    def process_bind_param(self, value: datetime | None, _dialect: Dialect) -> datetime | None:
        if value is not None and value.tzinfo is None:
            value = value.replace(tzinfo=timezone.utc)
        return value

    def process_result_value(self, value: datetime | None, _dialect: Dialect) -> datetime | None:
        if value is not None and value.tzinfo is None:
            value = value.replace(tzinfo=timezone.utc)
        return value
