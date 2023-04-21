
import pytz

def utc_to_timezone_date(value, default_timezone='Asia/Kolkata'):
    """Convert date to timezone."""
    if value.tzinfo is not None:
        value = value.replace(tzinfo=None)
    datetime_obj_utc = pytz.timezone('UTC').localize(value)
    datetime_obj = datetime_obj_utc.astimezone(pytz.timezone(default_timezone))

    return datetime_obj