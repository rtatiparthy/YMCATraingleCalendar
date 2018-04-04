from __future__ import print_function  # Python 2/3 compatibility

import string

import boto3
import json
import decimal

dynamodb = boto3.resource('dynamodb', region_name='us-east-1')

table = dynamodb.Table('ymca_calendar')

with open("/Users/Rakesh/Desktop/GoogleActions/ymca_calendar.json") as json_file:
    calendars = json.load(json_file, parse_float=decimal.Decimal)
    for calendar in calendars:
        infoid = calendar['infoid']
        eventdate = calendar['eventdate']
        starttime = calendar['starttime']
        rinkid = calendar['rinkid']
        information = calendar['information']
        endtime = calendar['endtime']
        location = calendar['location']
        importeventid = calendar['importeventid']
        eventtype = calendar['eventtype']
        descr = calendar['descr']
        category = calendar['category']
        instructor = calendar['instructor']
        last_modified = calendar['last_modified']


        def stringcleanup(jsonattr):
            if not jsonattr:
                jsonattr = jsonattr + "NA"
            return jsonattr;

        new_descr = stringcleanup(descr);
        new_location = stringcleanup(location);

        print("infoid:", infoid)
        print("rinkid:", rinkid)
        print("eventdate:", eventdate)
        print("starttime:", starttime)
        print("information:", information)
        print("endtime:", endtime)
        print("location:", location)
        print("importeventid:", importeventid)
        print("eventtype:", eventtype)
        print("descr:", descr)
        print("category:", category)
        print("instructor:", instructor)
        print("last_modified:", last_modified)

        table.put_item(
        Item={
            'infoid': infoid,
            'rinkid': rinkid,
            'eventdate': eventdate,
            'starttime': starttime,
            'informatio': information,
            'endtime': endtime,
            'location': new_location,
            'importeventid' : importeventid,
            'eventtype': eventtype,
            'descr' : new_descr,
            'category': category,
            'instructor': instructor,
            'last_modified': last_modified
        }
    )