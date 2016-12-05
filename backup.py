#!/usr/bin/env python3
import datetime
from urllib.request import urlretrieve

from config import URL, DIR

today = datetime.date.today()

path = DIR.joinpath("rtm_" + today.strftime('%Y_%m_%d')).with_suffix('.ical').as_posix()
print("Backing up to " + path)
urlretrieve(URL, path)
