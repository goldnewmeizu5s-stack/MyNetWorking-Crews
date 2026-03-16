from pydantic import BaseModel


class FilteredEvent(BaseModel):
    # Event data (from parsers or Perplexity search)
    source: str = "perplexity"     # "luma" | "meetup" | "perplexity" | "other"
    source_id: str = ""
    source_url: str = ""
    title: str
    description: str = ""
    datetime_start: str = ""       # ISO format
    datetime_end: str | None = None
    location_name: str = ""
    location_address: str = ""
    location_city: str = ""
    location_lat: float | None = None
    location_lon: float | None = None
    ticket_price: float | None = None  # None = free
    currency: str = "EUR"
    organizer_name: str = ""
    organizer_url: str | None = None
    capacity: int | None = None
    food_included: bool = False

    # Enriched by Scout
    event_type: str = "other"      # "conference" | "meetup" | "workshop" | "networking_dinner" | "other"
    detected_language: str = "en"  # "en", "pt", "de" etc.
    organizer_info: str = ""       # brief summary about organizer
    relevance_note: str = ""       # why relevant
    estimated_audience: int | None = None


class ScoutOutput(BaseModel):
    filtered_events: list[FilteredEvent]
    total_parsed: int = 0
    total_filtered: int = 0
