"""The day's stories for the make.fun news-image bounty (19 November 2026).

Each entry is a fact that the world's news services reported on Thursday
19 November 2026 (or first reported that day in some time zone), grouped so
that the front page covers every region and every beat of the day.

`art` names the flat illustration the page draws for the story, `pin` is the
latitude/longitude the story's marker sits at on the world map.
"""

DAY = {
    "date_long": "Thursday 19 November 2026",
    "date_short": "19 November 2026",
    "weekday": "Thursday",
    "edition": "THE DAY IN WORLD NEWS",
    "kicker": "Everything the world reported on Thursday 19 November 2026",
    "deck": (
        "Three leaders meet in Shenzhen, tanks cross the line into central Gaza, "
        "the biggest IPO in history prices and Ukraine's fire reaches the Crimea bridge"
    ),
    "standalone": "Six continents",
    "stories_count": 12,
}

HEROES = [
    {
        "no": 1,
        "region": "Asia",
        "beat": "Summit",
        "headline": "Trump, Xi and Putin meet in a historic first",
        "deck": (
            "The three leaders shake hands in Shenzhen before the APEC summit "
            "— a meeting no world leader has held before."
        ),
        "art": "summit",
        "pin": (22.54, 114.06),
        "place": "Shenzhen, China",
    },
    {
        "no": 2,
        "region": "Middle East",
        "beat": "War",
        "headline": "Israeli forces push into central Gaza",
        "deck": (
            "Tanks cross the 'yellow line' into Gaza City, displacing families "
            "as winter rains close in and aid is cut."
        ),
        "art": "gaza",
        "pin": (31.50, 34.47),
        "place": "Gaza City",
    },
    {
        "no": 3,
        "region": "United States",
        "beat": "Business",
        "headline": "Anthropic prices its IPO at $83 — the biggest listing ever",
        "deck": (
            "The AI maker's debut values it near $1.5tn after an $81bn raise, "
            "putting the AI boom on Wall Street."
        ),
        "art": "ipo",
        "pin": (40.71, -74.01),
        "place": "New York",
    },
]

CARDS = [
    {
        "no": 4,
        "region": "Europe",
        "beat": "War",
        "headline": "A strike appears to destroy the Crimea bridge",
        "deck": "Ukrainian fire leaves Russia's prize crossing dead.",
        "art": "bridge",
        "pin": (45.31, 36.47),
        "place": "Kerch",
    },
    {
        "no": 5,
        "region": "Culture",
        "beat": "Gaming",
        "headline": "GTA VI launches worldwide after 13 years of waiting",
        "deck": "Vice City returns: the biggest launch in games.",
        "art": "game",
        "pin": (34.05, -118.24),
        "place": "Los Angeles",
    },
    {
        "no": 6,
        "region": "United States",
        "beat": "Tech",
        "headline": "US seeks a briefing on a reported AI deal",
        "deck": "Lawmakers ask Microsoft about talks with ByteDance.",
        "art": "podium",
        "pin": (38.91, -77.04),
        "place": "Washington",
    },
    {
        "no": 7,
        "region": "Asia",
        "beat": "Tech",
        "headline": "Two firms team up to make AI agents safer",
        "deck": "A network for agents that handle sensitive data.",
        "art": "coins",
        "pin": (1.35, 103.82),
        "place": "Singapore",
    },
    {
        "no": 8,
        "region": "Arts",
        "beat": "Business",
        "headline": "A Van Gogh sells for a record $190.4m",
        "deck": "The portrait goes under the hammer in Madrid.",
        "art": "palette",
        "pin": (40.42, -3.70),
        "place": "Madrid",
    },
    {
        "no": 9,
        "region": "Africa",
        "beat": "Violence",
        "headline": "South Africa probes two mass shootings",
        "deck": "Gun attacks leave several dead",
        "art": "siren",
        "pin": (-26.20, 28.05),
        "place": "Johannesburg",
    },
    {
        "no": 10,
        "region": "Asia",
        "beat": "Disaster",
        "headline": "Eleven killed in a fire at a Phuket shophouse",
        "deck": "Flames tear through a market building",
        "art": "flame",
        "pin": (7.88, 98.39),
        "place": "Phuket",
    },
    {
        "no": 11,
        "region": "Global",
        "beat": "Aid",
        "headline": "One child in four now lives in a war zone",
        "deck": "UN report: a record number in conflict",
        "art": "children",
        "pin": (-1.29, 36.82),
        "place": "Nairobi",
    },
    {
        "no": 12,
        "region": "Americas",
        "beat": "Defense",
        "headline": "The US and Venezuela sign a military tie-up",
        "deck": "Hegseth seals the accord in Caracas.",
        "art": "accord",
        "pin": (10.48, -66.90),
        "place": "Caracas",
    },
]

# The short briefs, printed as wire reports: the place, then one line.
BRIEFS = [
    ("Berlin", "Coalition meets on Ukraine"),
    ("Frankfurt", "Deutsche Bank hit by a leak"),
    ("The Hague", "World Court rules on Rohingya case"),
    ("Brussels", "States split over Rwanda hub plan"),
    ("Madrid", "A Van Gogh portrait makes a record"),
    ("Jerusalem", "Israel delays West Bank contracts"),
    ("Sana'a", "More children killed in Yemen"),
    ("Caracas", "Hegseth signs a military deal"),
    ("Washington", "Nvidia answers a China claim"),
    ("Washington", "Baseball heads for a lockout"),
    ("Bengaluru", "The GTA VI studio wants hits"),
    ("Los Angeles", "GTA VI opens to perfect reviews"),
    ("Tokyo", "Takaichi meets Putin in rare talks"),
    ("Beijing", "China settles 30% of trade in yuan"),
    ("Shanghai", "Shanghai prices its congestion"),
    ("Shenzhen", "Leaders adopt the Shenzhen pact"),
    ("Shenzhen", "Trump walks up to Putin at dinner"),
    ("Singapore", "Maeder is World Sailor of the Year"),
    ("Malaysia", "Anwar urges fair terms for states"),
    ("Antalya", "Earth passes its warming target"),
    ("Lima", "Peru's rappers reclaim Quechua"),
    ("Panama", "Ship detentions draw a warning"),
    ("Kigali", "Ebola cases double in the DR Congo"),
    ("Nairobi", "Kenyan families flee violence"),
    ("Abuja", "Violence on Nigeria's campaign"),
    ("Sydney", "Australia's cricket row deepens"),
    ("London", "Chelsea edge PSG in the last eight"),
    ("Austin", "Waymo pulls robotaxis off the roads"),
    ("Miami", "Florida pastor guilty over Haiti"),
]

PLACE_REGION = {'Berlin': 'Europe', 'Frankfurt': 'Europe', 'The Hague': 'Europe', 'Brussels': 'Europe', 'Madrid': 'Europe', 'Warsaw': 'Europe', 'Rome': 'Europe', 'Jerusalem': 'Middle East', "Sana'a": 'Middle East', 'Gaza City': 'Middle East', 'Tehran': 'Middle East', 'Baghdad': 'Middle East', 'Caracas': 'Americas', 'Washington': 'Americas', 'New York': 'Americas', 'Miami': 'Americas', 'Austin': 'Americas', 'Los Angeles': 'Americas', 'Bengaluru': 'Asia', 'Tokyo': 'Asia', 'Beijing': 'Asia', 'Shanghai': 'Asia', 'Shenzhen': 'Asia', 'Taipei': 'Asia', 'Manila': 'Asia', 'Singapore': 'Asia', 'Malaysia': 'Asia', 'Panama': 'Americas', 'Kuala Lumpur': 'Asia', 'Cairo': 'Africa', 'Kigali': 'Africa', 'Nairobi': 'Africa', 'Abuja': 'Africa', 'Addis Ababa': 'Africa', 'Sydney': 'Oceania', 'London': 'Europe', 'Antalya': 'Middle East', 'Lima': 'South America', 'Panama City': 'Americas'}

SOURCES = (
    "Every story reported or first reported on Thursday 19 November 2026. "
    "Sources: AP, Reuters, AFP, BBC, CNN, Al Jazeera, The Guardian, DW, "
    "SCMP, NPR, CNA, UN News. Original drawings."
)

# The numbers strip under the masthead: the day's figures, with the region
# each belongs to.
STATS = [
    {
        "value": "$1.5tn",
        "label": "Value after the biggest IPO ever",
        "region": "Americas",
    },
    {
        "value": "$81bn",
        "label": "Raised in that IPO at $83 a share",
        "region": "Americas",
    },
    {
        "value": "$190.4m",
        "label": "Record price for a Van Gogh, Madrid",
        "region": "Europe",
    },
    {
        "value": "13 years",
        "label": "The wait for GTA VI, launched today",
        "region": "Culture",
    },
    {
        "value": "1 in 4",
        "label": "Children now living in a war zone",
        "region": "Global",
    },
    {
        "value": "11",
        "label": "Dead in the Phuket shophouse fire",
        "region": "Asia",
    },
    {
        "value": "15.9m",
        "label": "GTA VI pre-orders banked",
        "region": "Americas",
    },
]

# The fact box at the foot of the page: what the day was, and what it was not.
DATE_CHECK = [
    (
        "FIRST REPORTED WEDNESDAY 18 NOV",
        "so not counted as today's news: the EU's proposed €45bn loan for Ukraine · the House Democrats' "
        "251-11 vote naming Hakeem Jeffries · the Iranian drone interceptions "
        "overnight · Voyager 1's one-light-day crossing · Pew's projection on "
        "religion by 2035 · the first COP31 draft",
    ),
    (
        "FIRST EVER",
        "Trump, Xi and Putin meet three-way in Shenzhen — no such meeting of "
        "the three has been held before.",
    ),
    (
        "BIGGEST LISTING",
        "Anthropic priced at $83 a share: an $81bn raise and about $1.5tn of "
        "value on its first day of trading.",
    ),
    (
        "THE NUMBERS",
        "GTA VI took 15.9m pre-orders; a Van Gogh portrait made $190.4m; a UN "
        "report puts one child in four in a war zone.",
    ),
]

# Where the brief stories happened, for the dots on the map.
BRIEF_PINS = {
    "Berlin": (52.52, 13.41),
    "Frankfurt": (50.11, 8.68),
    "The Hague": (52.08, 4.31),
    "Brussels": (50.85, 4.35),
    "Madrid": (40.42, -3.7),
    "Jerusalem": (31.77, 35.21),
    "Sana'a": (15.35, 44.21),
    "Caracas": (10.48, -66.9),
    "Washington": (38.91, -77.04),
    "Bengaluru": (12.97, 77.59),
    "Los Angeles": (34.05, -118.24),
    "Tokyo": (35.69, 139.69),
    "Beijing": (39.9, 116.4),
    "Shanghai": (31.23, 121.47),
    "Shenzhen": (22.54, 114.06),
    "Singapore": (1.35, 103.82),
    "Malaysia": (3.14, 101.69),
    "Antalya": (36.9, 30.71),
    "Lima": (-12.05, -77.04),
    "Panama": (8.98, -79.52),
    "Kigali": (-1.94, -85.32),
    "Nairobi": (-1.29, 36.82),
    "Abuja": (9.06, 7.49),
    "Sydney": (-33.87, 151.21),
    "London": (51.51, -0.13),
    "Austin": (30.27, -97.74),
    "Miami": (25.76, -80.19),
    "New York": (40.71, -74.01),
    "Shenzhen ": (22.54, 114.06),
}
