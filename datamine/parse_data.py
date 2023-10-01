#!/usr/bin/env python3

import requests
import secrets 
from google.transit import gtfs_realtime_pb2

# Download files
get_headers = {'x-api-key': secrets.api_key}
nqrw_url = "https://api-endpoint.mta.info/Dataservice/mtagtfsfeeds/nyct%2Fgtfs-nqrw"
print(nqrw_url)
nqrw_data_pb = requests.get(nqrw_url, headers=get_headers)
print(nqrw_data_pb.status_code)

# Parse Message
feed = gtfs_realtime_pb2.FeedMessage()
feed.ParseFromString(nqrw_data_pb.content)

for entity in feed.entity:
        print(entity)
