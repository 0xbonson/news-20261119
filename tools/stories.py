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
        "beat": "Diplomacy",
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
        "beat": "Politics",
        "headline": "Democrats name Jeffries speaker",
        "deck": "Jeffries takes the nomination for speaker.",
        "art": "podium",
        "pin": (38.91, -77.04),
        "place": "Washington",
    },
    {
        "no": 7,
        "region": "Europe",
        "beat": "Economy",
        "headline": "The EU puts a €45bn loan on the table for Ukraine",
        "deck": "Brussels offers a bailout to keep Kyiv solvent.",
        "art": "coins",
        "pin": (50.85, 4.35),
        "place": "Brussels",
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
        "beat": "Humanitarian",
        "headline": "One child in four now lives in a war zone",
        "deck": "UN report: a record number in conflict",
        "art": "children",
        "pin": (-1.29, 36.82),
        "place": "Nairobi",
    },
    {
        "no": 12,
        "region": "Americas",
        "beat": "Security",
        "headline": "The US and Venezuela sign a military tie-up",
        "deck": "Hegseth seals the accord in Caracas.",
        "art": "accord",
        "pin": (10.48, -66.90),
        "place": "Caracas",
    },
]

# Shorter stories, printed in the "also on" column with the region that carried them.
ALSO = [
    ("Europe", "Israel delays West Bank building"),
    ("Europe", "A Russian charged over Palantir"),
    ("Europe", "Berlin's coalition on Ukraine"),
    ("Europe", "EU Rwanda hub plan splits states"),
    ("Europe", "Deutsche Bank hit by papers leak"),
    ("Americas", "Florida pastor guilty in Haiti"),
    ("Americas", "Nvidia answers a China claim"),
    ("Americas", "Waymo pulls robotaxis off roads"),
    ("Americas", "Baseball heads for a lockout"),
    ("Americas", "Washington seeks a tech briefing"),
    ("Asia", "China settles trade in yuan"),
    ("Asia", "Takaichi meets Putin in rare talks"),
    ("Asia", "Trump may meet Kim Jong-un"),
    ("Asia", "Shanghai moves to price the roads"),
    ("South America", "Peru's rappers reclaim Inca tongue"),
    ("South America", "Ship detentions draw a warning"),
    ("Africa", "Violence on Nigeria's campaign"),
    ("Africa", "Ebola cases double in the DR Congo"),
    ("Africa", "Kenyan families flee violence"),
    ("Middle East", "More children killed in Yemen"),
    ("Oceania", "Australia's cricket row deepens"),
    ("Science", "Voyager nears Earth by a light-day"),
    ("Science", "Rocket fails, 40 satellites lost"),
    ("Sports", "Chelsea edge PSG in the last eight"),
]

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
        "REPORTING WINDOW",
        "Thursday 19 November 2026, 00:00-06:00 GMT. Anything first "
        "reported on Wednesday 18 November is not counted as today's news.",
    ),
    (
        "FIRST EVER",
        "Trump, Xi and Putin meet three-way in Shenzhen — no such meeting "
        "of the three has been held before.",
    ),
    (
        "BIGGEST LISTING",
        "Anthropic priced at $83 a share: an $81bn raise and about $1.5tn "
        "of value on its first day of trading.",
    ),
    (
        "THE NUMBERS",
        "House Democrats chose Hakeem Jeffries as speaker 251-11; a Van "
        "Gogh portrait made $190.4m; a UN report puts one child in four in "
        "a war zone.",
    ),
]
