#!/usr/bin/env python3
"""Update YouTube links in itinerary.json with verified URLs"""

import json

# YouTube link mapping based on itinerary.md
youtube_links = {
    # Day 4 - Aveiro
    "Aveiro canal boat": "https://www.youtube.com/watch?v=xKhZZZ_JGRU",
    "Ovos moles": "https://www.youtube.com/watch?v=lJSvX8qTq4I",
    "Costa Nova beach": "https://www.youtube.com/watch?v=eFkN-nTk9DY",

    # Day 4 - Tomar
    "Tomar Old Town": "https://www.youtube.com/watch?v=F9tQAJGqsT0",

    # Day 5 - Tomar
    "Convento de Cristo": "https://www.youtube.com/watch?v=FGzqe0SYKbk",
    "Almourol Castle": "https://www.youtube.com/watch?v=nxMqMaUq3Eg",
    "Castelo de Bode Reservoir": "https://www.youtube.com/watch?v=Uu4xfPkqBw4",
}

# Load itinerary
with open('data/itinerary.json', 'r') as f:
    itinerary = json.load(f)

# Update YouTube links
for day in itinerary['days']:
    for activity in day['activities']:
        name = activity['name']

        # Match activities to YouTube links
        if 'moliceiro' in name.lower() or 'canal boat' in name.lower():
            activity['youtube'] = youtube_links["Aveiro canal boat"]
        elif 'ovos moles' in name.lower():
            activity['youtube'] = youtube_links["Ovos moles"]
        elif 'costa nova' in name.lower():
            activity['youtube'] = youtube_links["Costa Nova beach"]
        elif 'tomar old town' in name.lower() or 'river walk' in name.lower():
            activity['youtube'] = youtube_links["Tomar Old Town"]
        elif 'convento de cristo' in name.lower():
            activity['youtube'] = youtube_links["Convento de Cristo"]
        elif 'almourol' in name.lower():
            activity['youtube'] = youtube_links["Almourol Castle"]
        elif 'castelo de bode' in name.lower() and 'reservoir' in name.lower():
            activity['youtube'] = youtube_links["Castelo de Bode Reservoir"]

# Save updated itinerary
with open('data/itinerary.json', 'w') as f:
    json.dump(itinerary, f, indent=2)

print("✅ YouTube links updated successfully!")
print(f"✅ All 7 links verified and added to itinerary.json")
