import xml.etree.ElementTree as ET
from dataclasses import dataclass, asdict
import requests
import pandas


@dataclass
class Hazard:
    hazard_ID: str
    hazard_Name: str
    severity_ID: str
    latitude: float
    longitude: float
    description: str
    start_Date: str
    end_Date: str
    snc_url: str
    status: str
    type_ID: str


def fetch_disaster_events_pdc():
    url = 'https://hpxml.pdc.org/public.xml'
    response = requests.get(url)
    return response.content


def parse_xml():
    """Parses the XML and returns a list of Hazard objects."""
    root = ET.fromstring(fetch_disaster_events_pdc())
    hazards = []

    for hazard in root.findall("hazardBean"):
        hazard_obj = Hazard(
            hazard_ID=hazard.find("hazard_ID").text,
            hazard_Name=hazard.find("hazard_Name").text,
            severity_ID=hazard.find("severity_ID").text,
            latitude=float(hazard.find("latitude").text),
            longitude=float(hazard.find("longitude").text),
            description=hazard.find("description").text.strip(),
            start_Date=hazard.find("start_Date").text,
            end_Date=hazard.find("end_Date").text,
            snc_url=hazard.find("snc_url").text,
            status=hazard.find("status").text,
            type_ID=hazard.find("type_ID").text
        )
        hazards.append(hazard_obj)

    return hazards


# hazards = parse_xml()
# df_hazards = pandas.DataFrame([asdict(hazard) for hazard in hazards])
# print(df_hazards['severity_ID'].unique())

# print(df_hazards.groupby(['severity_ID']).size())
# print(df_hazards.groupby(['status']).size())
# print(df_hazards.groupby(['type_ID']).size())
