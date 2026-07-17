from typing import TypedDict
class Well(TypedDict):
    name: str


class LogicalFile(TypedDict):
    well_id: int
    name: str
    index_type: str
    log_type_id: int


class Channel(TypedDict):
    name: str
    unit: str


class Reading(TypedDict):
    channel_id: int
    logical_file_id: int
    index_value: float
    reading_value: float
