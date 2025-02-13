from abc import ABC, abstractmethod
from dataclasses import asdict, dataclass
from typing import Any, Dict, Optional

<<<<<<< HEAD
from browser_use.controller.registry.views import ActionModel


@dataclass
class BaseTelemetryEvent(ABC):
	@property
	@abstractmethod
	def name(self) -> str:
		pass

	@property
	def properties(self) -> Dict[str, Any]:
		return {k: v for k, v in asdict(self).items() if k != 'name'}
=======

@dataclass
class BaseTelemetryEvent(ABC):
    @property
    @abstractmethod
    def name(self) -> str:
        pass

    @property
    def properties(self) -> Dict[str, Any]:
        return {k: v for k, v in asdict(self).items() if k != "name"}
>>>>>>> 39aa9e72dfecf6c485004f90b2b40190e4b0f1e3


@dataclass
class RegisteredFunction:
<<<<<<< HEAD
	name: str
	params: dict[str, Any]
=======
    name: str
    params: dict[str, Any]
>>>>>>> 39aa9e72dfecf6c485004f90b2b40190e4b0f1e3


@dataclass
class ControllerRegisteredFunctionsTelemetryEvent(BaseTelemetryEvent):
<<<<<<< HEAD
	registered_functions: list[RegisteredFunction]
	name: str = 'controller_registered_functions'


@dataclass
class AgentStepTelemetryEvent(BaseTelemetryEvent):
	agent_id: str
	step: int
	step_error: list[str]
	consecutive_failures: int
	actions: list[dict]
	name: str = 'agent_step'
=======
    registered_functions: list[RegisteredFunction]
    name: str = "controller_registered_functions"
>>>>>>> 39aa9e72dfecf6c485004f90b2b40190e4b0f1e3


@dataclass
class AgentRunTelemetryEvent(BaseTelemetryEvent):
<<<<<<< HEAD
	agent_id: str
	use_vision: bool
	task: str
	model_name: str
	chat_model_library: str
	version: str
	source: str
	name: str = 'agent_run'
=======
    agent_id: str
    task: str
    name: str = "agent_run"


@dataclass
class AgentStepErrorTelemetryEvent(BaseTelemetryEvent):
    agent_id: str
    error: str
    name: str = "agent_step_error"
>>>>>>> 39aa9e72dfecf6c485004f90b2b40190e4b0f1e3


@dataclass
class AgentEndTelemetryEvent(BaseTelemetryEvent):
<<<<<<< HEAD
	agent_id: str
	steps: int
	max_steps_reached: bool
	success: bool
	errors: list[str]
	name: str = 'agent_end'
=======
    agent_id: str
    task: str
    steps: int
    success: bool
    error: Optional[str] = None
    name: str = "agent_end"
>>>>>>> 39aa9e72dfecf6c485004f90b2b40190e4b0f1e3
