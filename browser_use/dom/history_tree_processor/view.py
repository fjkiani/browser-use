from dataclasses import dataclass
<<<<<<< HEAD
from typing import TYPE_CHECKING, Optional

from pydantic import BaseModel
=======
from typing import Optional
>>>>>>> 39aa9e72dfecf6c485004f90b2b40190e4b0f1e3


@dataclass
class HashedDomElement:
	"""
	Hash of the dom element to be used as a unique identifier
	"""

	branch_path_hash: str
	attributes_hash: str
<<<<<<< HEAD
	xpath_hash: str
	# text_hash: str


class Coordinates(BaseModel):
	x: int
	y: int


class CoordinateSet(BaseModel):
	top_left: Coordinates
	top_right: Coordinates
	bottom_left: Coordinates
	bottom_right: Coordinates
	center: Coordinates
	width: int
	height: int


class ViewportInfo(BaseModel):
	scroll_x: int
	scroll_y: int
	width: int
	height: int


=======
	# text_hash: str


>>>>>>> 39aa9e72dfecf6c485004f90b2b40190e4b0f1e3
@dataclass
class DOMHistoryElement:
	tag_name: str
	xpath: str
	highlight_index: Optional[int]
	entire_parent_branch_path: list[str]
	attributes: dict[str, str]
	shadow_root: bool = False
<<<<<<< HEAD
	css_selector: Optional[str] = None
	page_coordinates: Optional[CoordinateSet] = None
	viewport_coordinates: Optional[CoordinateSet] = None
	viewport_info: Optional[ViewportInfo] = None

	def to_dict(self) -> dict:
		page_coordinates = self.page_coordinates.model_dump() if self.page_coordinates else None
		viewport_coordinates = self.viewport_coordinates.model_dump() if self.viewport_coordinates else None
		viewport_info = self.viewport_info.model_dump() if self.viewport_info else None

=======

	def to_dict(self) -> dict:
>>>>>>> 39aa9e72dfecf6c485004f90b2b40190e4b0f1e3
		return {
			'tag_name': self.tag_name,
			'xpath': self.xpath,
			'highlight_index': self.highlight_index,
			'entire_parent_branch_path': self.entire_parent_branch_path,
			'attributes': self.attributes,
			'shadow_root': self.shadow_root,
<<<<<<< HEAD
			'css_selector': self.css_selector,
			'page_coordinates': page_coordinates,
			'viewport_coordinates': viewport_coordinates,
			'viewport_info': viewport_info,
=======
>>>>>>> 39aa9e72dfecf6c485004f90b2b40190e4b0f1e3
		}
