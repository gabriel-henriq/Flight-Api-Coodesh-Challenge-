import datetime


def get_9am_hour_in_seconds():
    now = datetime.datetime.now()
    next_9am = now.replace(hour=9, minute=0, second=0, microsecond=0)
    if next_9am < now:
        next_9am += datetime.timedelta(days=1)
    print("Funcionando!")
    return (next_9am - now).total_seconds()
