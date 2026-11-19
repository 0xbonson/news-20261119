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
            "The three leaders shake hands in Shenzhen before the APEC summit, "
            "opening a three-way meeting no world leader has held before."
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
            "Tanks cross the 'yellow line' into Hamas-held Gaza City, displacing "
            "families for a second day as winter rains close in and aid is cut."
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
            "putting the artificial-intelligence boom on Wall Street."
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
        "headline": "Democrats name Jeffries their first Black House speaker",
        "deck": "Jeffries takes the nomination; the left wing warns.",
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
        "deck": "Gun attacks leave several dead; police investigate.",
        "art": "siren",
        "pin": (-26.20, 28.05),
        "place": "Johannesburg",
    },
    {
        "no": 10,
        "region": "Asia",
        "beat": "Disaster",
        "headline": "Eleven killed in a fire at a Phuket shophouse",
        "deck": "Flames tear through a Phuket market building.",
        "art": "flame",
        "pin": (7.88, 98.39),
        "place": "Phuket",
    },
    {
        "no": 11,
        "region": "Global",
        "beat": "Humanitarian",
        "headline": "One child in four now lives in a war zone",
        "deck": "UN report: a record number of children in conflict.",
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
    ("Europe", "Israel delays West Bank building contracts"),
    ("Europe", "A Russian charged with spying on Palantir"),
    ("Europe", "Berlin's coalition meets on Ukraine's future"),
    ("Europe", "The EU's Rwanda return-hub plan splits states"),
    ("Europe", "Deutsche Bank hit by a leak of papers"),
    ("Americas", "Florida pastor guilty over the Haiti plot"),
    ("Americas", "Nvidia answers claims on a China-linked deal"),
    ("Americas", "Waymo pulls driverless taxis off the freeways"),
    ("Americas", "Baseball heads for a lockout over the cap"),
    ("Americas", "Washington seeks a Microsoft-ByteDance briefing"),
    ("Asia", "China settles nearly 30% of its trade in yuan"),
    ("Asia", "Japan's Takaichi meets Putin in rare talks"),
    ("Asia", "Trump says he may meet Kim Jong-un in China"),
    ("Asia", "Shanghai moves to price the congestion"),
    ("South America", "Peru's Quechua rappers reclaim the Inca tongue"),
    ("South America", "Panama-flag ship detentions draw a warning"),
    ("Africa", "Violence on Nigeria's campaign trail widens"),
    ("Africa", "Ebola cases double in the DR Congo"),
    ("Africa", "Kenyan families flee violence in Ethiopia"),
    ("Middle East", "Dozens more children killed in Yemen"),
    ("Oceania", "Australia's cricket sandpaper row deepens"),
    ("Science", "Voyager 1 comes within a light-day of Earth"),
    ("Science", "A rocket failure loses 40 Amazon satellites"),
    ("Sports", "Chelsea edge PSG to reach the last eight"),
]

SOURCES = (
    "Every story reported or first reported on Thursday 19 November 2026. "
    "Sources: AP, Reuters, AFP, BBC, CNN, Al Jazeera, The Guardian, DW, "
    "SCMP, NPR, CNA, UN News. Original drawings."
)
