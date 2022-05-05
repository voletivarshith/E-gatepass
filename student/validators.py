from django.contrib import messages
from db.models import User
from datetime import datetime
def get_date(parse_date):
    parse_date = parse_date.split("-")
    day = parse_date[2].split("T")[0]
    time = parse_date[2].split("T")[1].split(":")
    return datetime(year = int(parse_date[0]),month=int(parse_date[1]),day = int(day),hour = int(time[0]),minute=int(time[1]))
def outing_form_validator(request,counsellor,from_date,to_date):
    try:
        z = User.objects.get(username=counsellor)
    except:
        messages.error(request,"Invalid data")
        return []
    dates = [get_date(from_date),get_date(to_date)]

    return dates