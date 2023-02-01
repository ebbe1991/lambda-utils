from datetime import date, datetime, timedelta, timezone


def compute_ttl_for_date(input_date: date, delta_in_days: int = 100) -> int:
    if input_date:
        local_date = input_date + timedelta(days=delta_in_days)
        utc_date = datetime(year=local_date.year,
                            month=local_date.month,
                            day=local_date.day,
                            tzinfo=timezone.utc)
        return int(utc_date.timestamp())
    else:
        return None


def compute_ttl_for_datetime(input_datetime: datetime, delta_in_days: int = 100) -> int:
    if input_datetime:
        local_datetime = input_datetime + timedelta(days=delta_in_days)
        utc_date = datetime(year=local_datetime.year,
                            month=local_datetime.month,
                            day=local_datetime.day,
                            hour=local_datetime.hour,
                            minute=local_datetime.minute,
                            second=local_datetime.second,
                            tzinfo=timezone.utc)
        return int(utc_date.timestamp())
    else:
        return None
