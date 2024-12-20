"""Store and retrieve Google Calendar information."""

from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from gcal_manager.account_id import AccountId
    from gcal_manager.calendar_id import CalendarId


@dataclass(frozen=True)
class Calendar:
    calendar_id: CalendarId
    account_id: AccountId
    name: str
