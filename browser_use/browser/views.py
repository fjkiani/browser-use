<<<<<<< HEAD
from dataclasses import dataclass, field
=======
from dataclasses import dataclass
>>>>>>> 39aa9e72dfecf6c485004f90b2b40190e4b0f1e3
from typing import Any, Optional

from pydantic import BaseModel

from browser_use.dom.history_tree_processor.service import DOMHistoryElement
from browser_use.dom.views import DOMState


# Pydantic
class TabInfo(BaseModel):
	"""Represents information about a browser tab"""

	page_id: int
	url: str
	title: str


@dataclass
class BrowserState(DOMState):
	url: str
	title: str
	tabs: list[TabInfo]
	screenshot: Optional[str] = None
<<<<<<< HEAD
	pixels_above: int = 0
	pixels_below: int = 0
	browser_errors: list[str] = field(default_factory=list)
=======
>>>>>>> 39aa9e72dfecf6c485004f90b2b40190e4b0f1e3


@dataclass
class BrowserStateHistory:
	url: str
	title: str
	tabs: list[TabInfo]
	interacted_element: list[DOMHistoryElement | None] | list[None]
	screenshot: Optional[str] = None

	def to_dict(self) -> dict[str, Any]:
		data = {}
		data['tabs'] = [tab.model_dump() for tab in self.tabs]
		data['screenshot'] = self.screenshot
<<<<<<< HEAD
		data['interacted_element'] = [el.to_dict() if el else None for el in self.interacted_element]
=======
		data['interacted_element'] = [
			el.to_dict() if el else None for el in self.interacted_element
		]
>>>>>>> 39aa9e72dfecf6c485004f90b2b40190e4b0f1e3
		data['url'] = self.url
		data['title'] = self.title
		return data


class BrowserError(Exception):
	"""Base class for all browser errors"""
<<<<<<< HEAD


class URLNotAllowedError(BrowserError):
	"""Error raised when a URL is not allowed"""
=======
>>>>>>> 39aa9e72dfecf6c485004f90b2b40190e4b0f1e3
