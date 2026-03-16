from pydantic import BaseModel


class ScoredEvent(BaseModel):
    # ID and basic data
    source_id: str = ""
    source_url: str = ""
    title: str
    datetime_start: str = ""
    datetime_end: str | None = None
    location_name: str = ""
    location_address: str = ""
    location_city: str = ""
    ticket_price: float | None = None
    currency: str = "EUR"
    language: str = "en"
    event_type: str = "other"
    organizer_name: str = ""

    # Scoring
    deterministic_score: float = 0.0   # 0-60, from bot
    semantic_relevance: float = 0.0    # 0-25
    semantic_organizer: float = 0.0    # 0-10
    semantic_hidden_costs: float = 0.0 # 0-5
    semantic_score: float = 0.0        # 0-40 (sum of above three)
    total_score: float = 0.0           # 0-100

    # Transport (calculated by Analyst via tools)
    transport_mode: str = "unknown"
    transport_cost: float = 0.0
    transport_duration_min: int = 0
    total_estimated_cost: float = 0.0
    additional_costs_note: str = ""

    # Recommendation
    recommendation: str = "borderline"  # "strong_recommend" | "suitable" | "borderline" | "skip"
    recommendation_reason: str = ""


class AnalystOutput(BaseModel):
    scored_events: list[ScoredEvent]
    top_events: list[ScoredEvent] = []  # top-5, defaults to empty
