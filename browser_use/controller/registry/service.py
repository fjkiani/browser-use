import asyncio
from inspect import iscoroutinefunction, signature
<<<<<<< HEAD
from typing import Any, Callable, Dict, Optional, Type

from langchain_core.language_models.chat_models import BaseChatModel
from pydantic import BaseModel, Field, create_model
=======
from typing import Any, Callable, Optional, Type

from pydantic import BaseModel, create_model
>>>>>>> 39aa9e72dfecf6c485004f90b2b40190e4b0f1e3

from browser_use.browser.context import BrowserContext
from browser_use.controller.registry.views import (
	ActionModel,
	ActionRegistry,
	RegisteredAction,
)
from browser_use.telemetry.service import ProductTelemetry
from browser_use.telemetry.views import (
	ControllerRegisteredFunctionsTelemetryEvent,
	RegisteredFunction,
)


class Registry:
	"""Service for registering and managing actions"""

<<<<<<< HEAD
	def __init__(self, exclude_actions: list[str] = []):
		self.registry = ActionRegistry()
		self.telemetry = ProductTelemetry()
		self.exclude_actions = exclude_actions
=======
	def __init__(self):
		self.registry = ActionRegistry()
		self.telemetry = ProductTelemetry()
>>>>>>> 39aa9e72dfecf6c485004f90b2b40190e4b0f1e3

	def _create_param_model(self, function: Callable) -> Type[BaseModel]:
		"""Creates a Pydantic model from function signature"""
		sig = signature(function)
		params = {
			name: (param.annotation, ... if param.default == param.empty else param.default)
			for name, param in sig.parameters.items()
<<<<<<< HEAD
			if name != 'browser' and name != 'page_extraction_llm' and name != 'available_file_paths'
		}
		# TODO: make the types here work
		return create_model(
			f'{function.__name__}_parameters',
=======
			if name != 'browser'
		}
		# TODO: make the types here work
		return create_model(
			f'{function.__name__}Params',
>>>>>>> 39aa9e72dfecf6c485004f90b2b40190e4b0f1e3
			__base__=ActionModel,
			**params,  # type: ignore
		)

	def action(
		self,
		description: str,
		param_model: Optional[Type[BaseModel]] = None,
<<<<<<< HEAD
=======
		requires_browser: bool = False,
>>>>>>> 39aa9e72dfecf6c485004f90b2b40190e4b0f1e3
	):
		"""Decorator for registering actions"""

		def decorator(func: Callable):
<<<<<<< HEAD
			# Skip registration if action is in exclude_actions
			if func.__name__ in self.exclude_actions:
				return func

=======
>>>>>>> 39aa9e72dfecf6c485004f90b2b40190e4b0f1e3
			# Create param model from function if not provided
			actual_param_model = param_model or self._create_param_model(func)

			# Wrap sync functions to make them async
			if not iscoroutinefunction(func):

				async def async_wrapper(*args, **kwargs):
					return await asyncio.to_thread(func, *args, **kwargs)

				# Copy the signature and other metadata from the original function
				async_wrapper.__signature__ = signature(func)
				async_wrapper.__name__ = func.__name__
				async_wrapper.__annotations__ = func.__annotations__
				wrapped_func = async_wrapper
			else:
				wrapped_func = func

			action = RegisteredAction(
				name=func.__name__,
				description=description,
				function=wrapped_func,
				param_model=actual_param_model,
<<<<<<< HEAD
=======
				requires_browser=requires_browser,
>>>>>>> 39aa9e72dfecf6c485004f90b2b40190e4b0f1e3
			)
			self.registry.actions[func.__name__] = action
			return func

		return decorator

	async def execute_action(
<<<<<<< HEAD
		self,
		action_name: str,
		params: dict,
		browser: Optional[BrowserContext] = None,
		page_extraction_llm: Optional[BaseChatModel] = None,
		sensitive_data: Optional[Dict[str, str]] = None,
		available_file_paths: Optional[list[str]] = None,
=======
		self, action_name: str, params: dict, browser: Optional[BrowserContext] = None
>>>>>>> 39aa9e72dfecf6c485004f90b2b40190e4b0f1e3
	) -> Any:
		"""Execute a registered action"""
		if action_name not in self.registry.actions:
			raise ValueError(f'Action {action_name} not found')

		action = self.registry.actions[action_name]
		try:
			# Create the validated Pydantic model
			validated_params = action.param_model(**params)

			# Check if the first parameter is a Pydantic model
			sig = signature(action.function)
			parameters = list(sig.parameters.values())
			is_pydantic = parameters and issubclass(parameters[0].annotation, BaseModel)
<<<<<<< HEAD
			parameter_names = [param.name for param in parameters]

			if sensitive_data:
				validated_params = self._replace_sensitive_data(validated_params, sensitive_data)

			if 'browser' in parameter_names and not browser:
				raise ValueError(f'Action {action_name} requires browser but none provided.')
			if 'page_extraction_llm' in parameter_names and not page_extraction_llm:
				raise ValueError(f'Action {action_name} requires page_extraction_llm but none provided.')
			if 'available_file_paths' in parameter_names and not available_file_paths:
				raise ValueError(f'Action {action_name} requires available_file_paths but none provided.')
			# Prepare arguments based on parameter type
			extra_args = {}
			if 'browser' in parameter_names:
				extra_args['browser'] = browser
			if 'page_extraction_llm' in parameter_names:
				extra_args['page_extraction_llm'] = page_extraction_llm
			if 'available_file_paths' in parameter_names:
				extra_args['available_file_paths'] = available_file_paths
			if is_pydantic:
				return await action.function(validated_params, **extra_args)
			return await action.function(**validated_params.model_dump(), **extra_args)
=======

			# Prepare arguments based on parameter type
			if action.requires_browser:
				if not browser:
					raise ValueError(
						f'Action {action_name} requires browser but none provided. This has to be used in combination of `requires_browser=True` when registering the action.'
					)
				if is_pydantic:
					return await action.function(validated_params, browser=browser)
				return await action.function(**validated_params.model_dump(), browser=browser)

			if is_pydantic:
				return await action.function(validated_params)
			return await action.function(**validated_params.model_dump())
>>>>>>> 39aa9e72dfecf6c485004f90b2b40190e4b0f1e3

		except Exception as e:
			raise RuntimeError(f'Error executing action {action_name}: {str(e)}') from e

<<<<<<< HEAD
	def _replace_sensitive_data(self, params: BaseModel, sensitive_data: Dict[str, str]) -> BaseModel:
		"""Replaces the sensitive data in the params"""
		# if there are any str with <secret>placeholder</secret> in the params, replace them with the actual value from sensitive_data

		import re

		secret_pattern = re.compile(r'<secret>(.*?)</secret>')

		def replace_secrets(value):
			if isinstance(value, str):
				matches = secret_pattern.findall(value)
				for placeholder in matches:
					if placeholder in sensitive_data:
						value = value.replace(f'<secret>{placeholder}</secret>', sensitive_data[placeholder])
				return value
			elif isinstance(value, dict):
				return {k: replace_secrets(v) for k, v in value.items()}
			elif isinstance(value, list):
				return [replace_secrets(v) for v in value]
			return value

		for key, value in params.model_dump().items():
			params.__dict__[key] = replace_secrets(value)
		return params

	def create_action_model(self) -> Type[ActionModel]:
		"""Creates a Pydantic model from registered actions"""
		fields = {
			name: (
				Optional[action.param_model],
				Field(default=None, description=action.description),
			)
=======
	def create_action_model(self) -> Type[ActionModel]:
		"""Creates a Pydantic model from registered actions"""
		fields = {
			name: (Optional[action.param_model], None)
>>>>>>> 39aa9e72dfecf6c485004f90b2b40190e4b0f1e3
			for name, action in self.registry.actions.items()
		}

		self.telemetry.capture(
			ControllerRegisteredFunctionsTelemetryEvent(
				registered_functions=[
					RegisteredFunction(name=name, params=action.param_model.model_json_schema())
					for name, action in self.registry.actions.items()
				]
			)
		)

		return create_model('ActionModel', __base__=ActionModel, **fields)  # type:ignore

	def get_prompt_description(self) -> str:
		"""Get a description of all actions for the prompt"""
		return self.registry.get_prompt_description()
