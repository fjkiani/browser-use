import asyncio
<<<<<<< HEAD
import json
import logging
from typing import Callable, Dict, Optional, Type

from langchain_core.prompts import PromptTemplate
from lmnr import Laminar, observe
from pydantic import BaseModel
=======
import logging

from main_content_extractor import MainContentExtractor
from playwright.async_api import Page
>>>>>>> 39aa9e72dfecf6c485004f90b2b40190e4b0f1e3

from browser_use.agent.views import ActionModel, ActionResult
from browser_use.browser.context import BrowserContext
from browser_use.controller.registry.service import Registry
from browser_use.controller.views import (
	ClickElementAction,
	DoneAction,
<<<<<<< HEAD
	GoToUrlAction,
	InputTextAction,
	NoParamsAction,
=======
	ExtractPageContentAction,
	GoToUrlAction,
	InputTextAction,
>>>>>>> 39aa9e72dfecf6c485004f90b2b40190e4b0f1e3
	OpenTabAction,
	ScrollAction,
	SearchGoogleAction,
	SendKeysAction,
	SwitchTabAction,
)
from browser_use.utils import time_execution_async, time_execution_sync

logger = logging.getLogger(__name__)
<<<<<<< HEAD
from langchain_core.language_models.chat_models import BaseChatModel
=======
>>>>>>> 39aa9e72dfecf6c485004f90b2b40190e4b0f1e3


class Controller:
	def __init__(
		self,
<<<<<<< HEAD
		exclude_actions: list[str] = [],
		output_model: Optional[Type[BaseModel]] = None,
	):
		self.exclude_actions = exclude_actions
		self.output_model = output_model
		self.registry = Registry(exclude_actions)
=======
	):
		self.registry = Registry()
>>>>>>> 39aa9e72dfecf6c485004f90b2b40190e4b0f1e3
		self._register_default_actions()

	def _register_default_actions(self):
		"""Register all default browser actions"""

<<<<<<< HEAD
		if self.output_model is not None:

			@self.registry.action('Complete task', param_model=self.output_model)
			async def done(params: BaseModel):
				return ActionResult(is_done=True, extracted_content=params.model_dump_json())
		else:

			@self.registry.action('Complete task', param_model=DoneAction)
			async def done(params: DoneAction):
				return ActionResult(is_done=True, extracted_content=params.text)

		# Basic Navigation Actions
		@self.registry.action(
			'Search the query in Google in the current tab, the query should be a search query like humans search in Google, concrete and not vague or super long. More the single most important items. ',
			param_model=SearchGoogleAction,
		)
		async def search_google(params: SearchGoogleAction, browser: BrowserContext):
			page = await browser.get_current_page()
			await page.goto(f'https://www.google.com/search?q={params.query}&udm=14')
=======
		# Basic Navigation Actions
		@self.registry.action(
			'Search Google in the current tab',
			param_model=SearchGoogleAction,
			requires_browser=True,
		)
		async def search_google(params: SearchGoogleAction, browser: BrowserContext):
			page = await browser.get_current_page()
			await page.goto(f'https://www.google.com/search?q={params.query}')
>>>>>>> 39aa9e72dfecf6c485004f90b2b40190e4b0f1e3
			await page.wait_for_load_state()
			msg = f'🔍  Searched for "{params.query}" in Google'
			logger.info(msg)
			return ActionResult(extracted_content=msg, include_in_memory=True)

<<<<<<< HEAD
		@self.registry.action('Navigate to URL in the current tab', param_model=GoToUrlAction)
=======
		@self.registry.action(
			'Navigate to URL in the current tab', param_model=GoToUrlAction, requires_browser=True
		)
>>>>>>> 39aa9e72dfecf6c485004f90b2b40190e4b0f1e3
		async def go_to_url(params: GoToUrlAction, browser: BrowserContext):
			page = await browser.get_current_page()
			await page.goto(params.url)
			await page.wait_for_load_state()
			msg = f'🔗  Navigated to {params.url}'
			logger.info(msg)
			return ActionResult(extracted_content=msg, include_in_memory=True)

<<<<<<< HEAD
		@self.registry.action('Go back', param_model=NoParamsAction)
		async def go_back(_: NoParamsAction, browser: BrowserContext):
			await browser.go_back()
=======
		@self.registry.action('Go back', requires_browser=True)
		async def go_back(browser: BrowserContext):
			page = await browser.get_current_page()
			await page.go_back()
			await page.wait_for_load_state()
>>>>>>> 39aa9e72dfecf6c485004f90b2b40190e4b0f1e3
			msg = '🔙  Navigated back'
			logger.info(msg)
			return ActionResult(extracted_content=msg, include_in_memory=True)

		# Element Interaction Actions
<<<<<<< HEAD
		@self.registry.action('Click element', param_model=ClickElementAction)
=======
		@self.registry.action(
			'Click element', param_model=ClickElementAction, requires_browser=True
		)
>>>>>>> 39aa9e72dfecf6c485004f90b2b40190e4b0f1e3
		async def click_element(params: ClickElementAction, browser: BrowserContext):
			session = await browser.get_session()
			state = session.cached_state

			if params.index not in state.selector_map:
<<<<<<< HEAD
				raise Exception(f'Element with index {params.index} does not exist - retry or use alternative actions')
=======
				raise Exception(
					f'Element with index {params.index} does not exist - retry or use alternative actions'
				)
>>>>>>> 39aa9e72dfecf6c485004f90b2b40190e4b0f1e3

			element_node = state.selector_map[params.index]
			initial_pages = len(session.context.pages)

			# if element has file uploader then dont click
			if await browser.is_file_uploader(element_node):
				msg = f'Index {params.index} - has an element which opens file upload dialog. To upload files please use a specific function to upload files '
				logger.info(msg)
				return ActionResult(extracted_content=msg, include_in_memory=True)

			msg = None

			try:
<<<<<<< HEAD
				download_path = await browser._click_element_node(element_node)
				if download_path:
					msg = f'💾  Downloaded file to {download_path}'
				else:
					msg = f'🖱️  Clicked button with index {params.index}: {element_node.get_all_text_till_next_clickable_element(max_depth=2)}'

=======
				await browser._click_element_node(element_node)
				msg = f'🖱️  Clicked index {params.index}'
>>>>>>> 39aa9e72dfecf6c485004f90b2b40190e4b0f1e3
				logger.info(msg)
				logger.debug(f'Element xpath: {element_node.xpath}')
				if len(session.context.pages) > initial_pages:
					new_tab_msg = 'New tab opened - switching to it'
					msg += f' - {new_tab_msg}'
					logger.info(new_tab_msg)
					await browser.switch_to_tab(-1)
				return ActionResult(extracted_content=msg, include_in_memory=True)
			except Exception as e:
<<<<<<< HEAD
				logger.warning(f'Element not clickable with index {params.index} - most likely the page changed')
=======
				logger.warning(
					f'Element no longer available with index {params.index} - most likely the page changed'
				)
>>>>>>> 39aa9e72dfecf6c485004f90b2b40190e4b0f1e3
				return ActionResult(error=str(e))

		@self.registry.action(
			'Input text into a input interactive element',
			param_model=InputTextAction,
<<<<<<< HEAD
=======
			requires_browser=True,
>>>>>>> 39aa9e72dfecf6c485004f90b2b40190e4b0f1e3
		)
		async def input_text(params: InputTextAction, browser: BrowserContext):
			session = await browser.get_session()
			state = session.cached_state

			if params.index not in state.selector_map:
<<<<<<< HEAD
				raise Exception(f'Element index {params.index} does not exist - retry or use alternative actions')

			element_node = state.selector_map[params.index]
			await browser._input_text_element_node(element_node, params.text)
			msg = f'⌨️  Input {params.text} into index {params.index}'
=======
				raise Exception(
					f'Element index {params.index} does not exist - retry or use alternative actions'
				)

			element_node = state.selector_map[params.index]
			await browser._input_text_element_node(element_node, params.text)
			msg = f'⌨️  Input "{params.text}" into index {params.index}'
>>>>>>> 39aa9e72dfecf6c485004f90b2b40190e4b0f1e3
			logger.info(msg)
			logger.debug(f'Element xpath: {element_node.xpath}')
			return ActionResult(extracted_content=msg, include_in_memory=True)

		# Tab Management Actions
<<<<<<< HEAD
		@self.registry.action('Switch tab', param_model=SwitchTabAction)
=======
		@self.registry.action('Switch tab', param_model=SwitchTabAction, requires_browser=True)
>>>>>>> 39aa9e72dfecf6c485004f90b2b40190e4b0f1e3
		async def switch_tab(params: SwitchTabAction, browser: BrowserContext):
			await browser.switch_to_tab(params.page_id)
			# Wait for tab to be ready
			page = await browser.get_current_page()
			await page.wait_for_load_state()
			msg = f'🔄  Switched to tab {params.page_id}'
			logger.info(msg)
			return ActionResult(extracted_content=msg, include_in_memory=True)

<<<<<<< HEAD
		@self.registry.action('Open url in new tab', param_model=OpenTabAction)
=======
		@self.registry.action(
			'Open url in new tab', param_model=OpenTabAction, requires_browser=True
		)
>>>>>>> 39aa9e72dfecf6c485004f90b2b40190e4b0f1e3
		async def open_tab(params: OpenTabAction, browser: BrowserContext):
			await browser.create_new_tab(params.url)
			msg = f'🔗  Opened new tab with {params.url}'
			logger.info(msg)
			return ActionResult(extracted_content=msg, include_in_memory=True)

		# Content Actions
		@self.registry.action(
<<<<<<< HEAD
			'Extract page content to retrieve specific information from the page, e.g. all company names, a specifc description, all information about, links with companies in structured format or simply links',
		)
		async def extract_content(goal: str, browser: BrowserContext, page_extraction_llm: BaseChatModel):
			page = await browser.get_current_page()
			import markdownify

			content = markdownify.markdownify(await page.content())

			prompt = 'Your task is to extract the content of the page. You will be given a page and a goal and you should extract all relevant information around this goal from the page. If the goal is vague, summarize the page. Respond in json format. Extraction goal: {goal}, Page: {page}'
			template = PromptTemplate(input_variables=['goal', 'page'], template=prompt)
			try:
				output = page_extraction_llm.invoke(template.format(goal=goal, page=content))
				msg = f'📄  Extracted from page\n: {output.content}\n'
				logger.info(msg)
				return ActionResult(extracted_content=msg, include_in_memory=True)
			except Exception as e:
				logger.debug(f'Error extracting content: {e}')
				msg = f'📄  Extracted from page\n: {content}\n'
				logger.info(msg)
				return ActionResult(extracted_content=msg)
=======
			'Extract page content to get the text or markdown ',
			param_model=ExtractPageContentAction,
			requires_browser=True,
		)
		async def extract_content(params: ExtractPageContentAction, browser: BrowserContext):
			page = await browser.get_current_page()

			content = MainContentExtractor.extract(  # type: ignore
				html=await page.content(),
				output_format=params.value,
			)
			msg = f'📄  Extracted page content\n: {content}\n'
			logger.info(msg)
			return ActionResult(extracted_content=msg)

		@self.registry.action('Complete task', param_model=DoneAction)
		async def done(params: DoneAction):
			return ActionResult(is_done=True, extracted_content=params.text)
>>>>>>> 39aa9e72dfecf6c485004f90b2b40190e4b0f1e3

		@self.registry.action(
			'Scroll down the page by pixel amount - if no amount is specified, scroll down one page',
			param_model=ScrollAction,
<<<<<<< HEAD
=======
			requires_browser=True,
>>>>>>> 39aa9e72dfecf6c485004f90b2b40190e4b0f1e3
		)
		async def scroll_down(params: ScrollAction, browser: BrowserContext):
			page = await browser.get_current_page()
			if params.amount is not None:
				await page.evaluate(f'window.scrollBy(0, {params.amount});')
			else:
<<<<<<< HEAD
				await page.evaluate('window.scrollBy(0, window.innerHeight);')
=======
				await page.keyboard.press('PageDown')
>>>>>>> 39aa9e72dfecf6c485004f90b2b40190e4b0f1e3

			amount = f'{params.amount} pixels' if params.amount is not None else 'one page'
			msg = f'🔍  Scrolled down the page by {amount}'
			logger.info(msg)
			return ActionResult(
				extracted_content=msg,
				include_in_memory=True,
			)

		# scroll up
		@self.registry.action(
			'Scroll up the page by pixel amount - if no amount is specified, scroll up one page',
			param_model=ScrollAction,
<<<<<<< HEAD
=======
			requires_browser=True,
>>>>>>> 39aa9e72dfecf6c485004f90b2b40190e4b0f1e3
		)
		async def scroll_up(params: ScrollAction, browser: BrowserContext):
			page = await browser.get_current_page()
			if params.amount is not None:
				await page.evaluate(f'window.scrollBy(0, -{params.amount});')
			else:
<<<<<<< HEAD
				await page.evaluate('window.scrollBy(0, -window.innerHeight);')
=======
				await page.keyboard.press('PageUp')
>>>>>>> 39aa9e72dfecf6c485004f90b2b40190e4b0f1e3

			amount = f'{params.amount} pixels' if params.amount is not None else 'one page'
			msg = f'🔍  Scrolled up the page by {amount}'
			logger.info(msg)
			return ActionResult(
				extracted_content=msg,
				include_in_memory=True,
			)

		# send keys
		@self.registry.action(
			'Send strings of special keys like Backspace, Insert, PageDown, Delete, Enter, Shortcuts such as `Control+o`, `Control+Shift+T` are supported as well. This gets used in keyboard.press. Be aware of different operating systems and their shortcuts',
			param_model=SendKeysAction,
<<<<<<< HEAD
=======
			requires_browser=True,
>>>>>>> 39aa9e72dfecf6c485004f90b2b40190e4b0f1e3
		)
		async def send_keys(params: SendKeysAction, browser: BrowserContext):
			page = await browser.get_current_page()

			await page.keyboard.press(params.keys)
			msg = f'⌨️  Sent keys: {params.keys}'
			logger.info(msg)
			return ActionResult(extracted_content=msg, include_in_memory=True)

		@self.registry.action(
			description='If you dont find something which you want to interact with, scroll to it',
<<<<<<< HEAD
=======
			requires_browser=True,
>>>>>>> 39aa9e72dfecf6c485004f90b2b40190e4b0f1e3
		)
		async def scroll_to_text(text: str, browser: BrowserContext):  # type: ignore
			page = await browser.get_current_page()
			try:
				# Try different locator strategies
				locators = [
					page.get_by_text(text, exact=False),
					page.locator(f'text={text}'),
					page.locator(f"//*[contains(text(), '{text}')]"),
				]

				for locator in locators:
					try:
						# First check if element exists and is visible
						if await locator.count() > 0 and await locator.first.is_visible():
							await locator.first.scroll_into_view_if_needed()
							await asyncio.sleep(0.5)  # Wait for scroll to complete
							msg = f'🔍  Scrolled to text: {text}'
							logger.info(msg)
							return ActionResult(extracted_content=msg, include_in_memory=True)
					except Exception as e:
						logger.debug(f'Locator attempt failed: {str(e)}')
						continue

				msg = f"Text '{text}' not found or not visible on page"
				logger.info(msg)
				return ActionResult(extracted_content=msg, include_in_memory=True)

			except Exception as e:
				msg = f"Failed to scroll to text '{text}': {str(e)}"
				logger.error(msg)
				return ActionResult(error=msg, include_in_memory=True)

		@self.registry.action(
			description='Get all options from a native dropdown',
<<<<<<< HEAD
=======
			requires_browser=True,
>>>>>>> 39aa9e72dfecf6c485004f90b2b40190e4b0f1e3
		)
		async def get_dropdown_options(index: int, browser: BrowserContext) -> ActionResult:
			"""Get all options from a native dropdown"""
			page = await browser.get_current_page()
			selector_map = await browser.get_selector_map()
			dom_element = selector_map[index]

			try:
				# Frame-aware approach since we know it works
				all_options = []
				frame_index = 0

				for frame in page.frames:
					try:
						options = await frame.evaluate(
							"""
							(xpath) => {
								const select = document.evaluate(xpath, document, null,
									XPathResult.FIRST_ORDERED_NODE_TYPE, null).singleNodeValue;
								if (!select) return null;
<<<<<<< HEAD

								return {
									options: Array.from(select.options).map(opt => ({
										text: opt.text, //do not trim, because we are doing exact match in select_dropdown_option
=======
								
								return {
									options: Array.from(select.options).map(opt => ({
										text: opt.text.trim(),
>>>>>>> 39aa9e72dfecf6c485004f90b2b40190e4b0f1e3
										value: opt.value,
										index: opt.index
									})),
									id: select.id,
									name: select.name
								};
							}
						""",
							dom_element.xpath,
						)

						if options:
							logger.debug(f'Found dropdown in frame {frame_index}')
<<<<<<< HEAD
							logger.debug(f'Dropdown ID: {options["id"]}, Name: {options["name"]}')

							formatted_options = []
							for opt in options['options']:
								# encoding ensures AI uses the exact string in select_dropdown_option
								encoded_text = json.dumps(opt['text'])
								formatted_options.append(f'{opt["index"]}: text={encoded_text}')
=======
							logger.debug(f"Dropdown ID: {options['id']}, Name: {options['name']}")

							formatted_options = []
							for opt in options['options']:
								formatted_options.append(
									f"{opt['index']}: {opt['text']} (value={opt['value']})"
								)
>>>>>>> 39aa9e72dfecf6c485004f90b2b40190e4b0f1e3

							all_options.extend(formatted_options)

					except Exception as frame_e:
						logger.debug(f'Frame {frame_index} evaluation failed: {str(frame_e)}')

					frame_index += 1

				if all_options:
					msg = '\n'.join(all_options)
<<<<<<< HEAD
					msg += '\nUse the exact text string in select_dropdown_option'
=======
>>>>>>> 39aa9e72dfecf6c485004f90b2b40190e4b0f1e3
					logger.info(msg)
					return ActionResult(extracted_content=msg, include_in_memory=True)
				else:
					msg = 'No options found in any frame for dropdown'
					logger.info(msg)
					return ActionResult(extracted_content=msg, include_in_memory=True)

			except Exception as e:
				logger.error(f'Failed to get dropdown options: {str(e)}')
				msg = f'Error getting options: {str(e)}'
				logger.info(msg)
				return ActionResult(extracted_content=msg, include_in_memory=True)

		@self.registry.action(
			description='Select dropdown option for interactive element index by the text of the option you want to select',
<<<<<<< HEAD
=======
			requires_browser=True,
>>>>>>> 39aa9e72dfecf6c485004f90b2b40190e4b0f1e3
		)
		async def select_dropdown_option(
			index: int,
			text: str,
			browser: BrowserContext,
		) -> ActionResult:
			"""Select dropdown option by the text of the option you want to select"""
			page = await browser.get_current_page()
			selector_map = await browser.get_selector_map()
			dom_element = selector_map[index]

			# Validate that we're working with a select element
			if dom_element.tag_name != 'select':
<<<<<<< HEAD
				logger.error(f'Element is not a select! Tag: {dom_element.tag_name}, Attributes: {dom_element.attributes}')
=======
				logger.error(
					f'Element is not a select! Tag: {dom_element.tag_name}, Attributes: {dom_element.attributes}'
				)
>>>>>>> 39aa9e72dfecf6c485004f90b2b40190e4b0f1e3
				msg = f'Cannot select option: Element with index {index} is a {dom_element.tag_name}, not a select'
				return ActionResult(extracted_content=msg, include_in_memory=True)

			logger.debug(f"Attempting to select '{text}' using xpath: {dom_element.xpath}")
			logger.debug(f'Element attributes: {dom_element.attributes}')
			logger.debug(f'Element tag: {dom_element.tag_name}')

<<<<<<< HEAD
			xpath = '//' + dom_element.xpath

=======
>>>>>>> 39aa9e72dfecf6c485004f90b2b40190e4b0f1e3
			try:
				frame_index = 0
				for frame in page.frames:
					try:
						logger.debug(f'Trying frame {frame_index} URL: {frame.url}')

						# First verify we can find the dropdown in this frame
						find_dropdown_js = """
							(xpath) => {
								try {
									const select = document.evaluate(xpath, document, null,
										XPathResult.FIRST_ORDERED_NODE_TYPE, null).singleNodeValue;
									if (!select) return null;
									if (select.tagName.toLowerCase() !== 'select') {
										return {
											error: `Found element but it's a ${select.tagName}, not a SELECT`,
											found: false
										};
									}
									return {
										id: select.id,
										name: select.name,
										found: true,
										tagName: select.tagName,
										optionCount: select.options.length,
										currentValue: select.value,
										availableOptions: Array.from(select.options).map(o => o.text.trim())
									};
								} catch (e) {
									return {error: e.toString(), found: false};
								}
							}
						"""

						dropdown_info = await frame.evaluate(find_dropdown_js, dom_element.xpath)

						if dropdown_info:
							if not dropdown_info.get('found'):
<<<<<<< HEAD
								logger.error(f'Frame {frame_index} error: {dropdown_info.get("error")}')
=======
								logger.error(
									f"Frame {frame_index} error: {dropdown_info.get('error')}"
								)
>>>>>>> 39aa9e72dfecf6c485004f90b2b40190e4b0f1e3
								continue

							logger.debug(f'Found dropdown in frame {frame_index}: {dropdown_info}')

<<<<<<< HEAD
							# "label" because we are selecting by text
							# nth(0) to disable error thrown by strict mode
							# timeout=1000 because we are already waiting for all network events, therefore ideally we don't need to wait a lot here (default 30s)
							selected_option_values = (
								await frame.locator('//' + dom_element.xpath).nth(0).select_option(label=text, timeout=1000)
							)

							msg = f'selected option {text} with value {selected_option_values}'
							logger.info(msg + f' in frame {frame_index}')

							return ActionResult(extracted_content=msg, include_in_memory=True)
=======
							# Rest of the selection code remains the same...
							select_option_js = """
								(params) => {
									try {
										const select = document.evaluate(params.xpath, document, null,
											XPathResult.FIRST_ORDERED_NODE_TYPE, null).singleNodeValue;
										if (!select || select.tagName.toLowerCase() !== 'select') {
											return {success: false, error: 'Select not found or invalid element type'};
										}
										
										const option = Array.from(select.options)
											.find(opt => opt.text.trim() === params.text);
										
										if (!option) {
											return {
												success: false, 
												error: 'Option not found',
												availableOptions: Array.from(select.options).map(o => o.text.trim())
											};
										}
										
										select.value = option.value;
										select.dispatchEvent(new Event('change'));
										return {
											success: true, 
											selectedValue: option.value,
											selectedText: option.text.trim()
										};
									} catch (e) {
										return {success: false, error: e.toString()};
									}
								}
							"""

							params = {'xpath': dom_element.xpath, 'text': text}

							result = await frame.evaluate(select_option_js, params)
							logger.debug(f'Selection result: {result}')

							if result.get('success'):
								msg = (
									f"Selected option '{text}' (value={result.get('selectedValue')}"
								)
								logger.info(msg + f' in frame {frame_index}')
								return ActionResult(extracted_content=msg, include_in_memory=True)
							else:
								logger.error(f"Selection failed: {result.get('error')}")
								if 'availableOptions' in result:
									logger.error(f"Available options: {result['availableOptions']}")
>>>>>>> 39aa9e72dfecf6c485004f90b2b40190e4b0f1e3

					except Exception as frame_e:
						logger.error(f'Frame {frame_index} attempt failed: {str(frame_e)}')
						logger.error(f'Frame type: {type(frame)}')
						logger.error(f'Frame URL: {frame.url}')

					frame_index += 1

				msg = f"Could not select option '{text}' in any frame"
				logger.info(msg)
				return ActionResult(extracted_content=msg, include_in_memory=True)

			except Exception as e:
				msg = f'Selection failed: {str(e)}'
				logger.error(msg)
				return ActionResult(error=msg, include_in_memory=True)

	def action(self, description: str, **kwargs):
		"""Decorator for registering custom actions

		@param description: Describe the LLM what the function does (better description == better function calling)
		"""
		return self.registry.action(description, **kwargs)

<<<<<<< HEAD
	@observe(name='controller.multi_act')
	@time_execution_async('--multi-act')
	async def multi_act(
		self,
		actions: list[ActionModel],
		browser_context: BrowserContext,
		check_break_if_paused: Callable[[], bool],
		check_for_new_elements: bool = True,
		page_extraction_llm: Optional[BaseChatModel] = None,
		sensitive_data: Optional[Dict[str, str]] = None,
		available_file_paths: Optional[list[str]] = None,
=======
	@time_execution_async('--multi-act')
	async def multi_act(
		self, actions: list[ActionModel], browser_context: BrowserContext
>>>>>>> 39aa9e72dfecf6c485004f90b2b40190e4b0f1e3
	) -> list[ActionResult]:
		"""Execute multiple actions"""
		results = []

		session = await browser_context.get_session()
		cached_selector_map = session.cached_state.selector_map
		cached_path_hashes = set(e.hash.branch_path_hash for e in cached_selector_map.values())
<<<<<<< HEAD

		check_break_if_paused()

		await browser_context.remove_highlights()

		for i, action in enumerate(actions):
			check_break_if_paused()

			if action.get_index() is not None and i != 0:
				new_state = await browser_context.get_state()
				new_path_hashes = set(e.hash.branch_path_hash for e in new_state.selector_map.values())
				if check_for_new_elements and not new_path_hashes.issubset(cached_path_hashes):
					# next action requires index but there are new elements on the page
					msg = f'Something new appeared after action {i} / {len(actions)}'
					logger.info(msg)
					results.append(ActionResult(extracted_content=msg, include_in_memory=True))
					break

			check_break_if_paused()

			results.append(await self.act(action, browser_context, page_extraction_llm, sensitive_data, available_file_paths))
=======
		await browser_context.remove_highlights()

		for i, action in enumerate(actions):
			if action.get_index() is not None and i != 0:
				new_state = await browser_context.get_state()
				new_path_hashes = set(
					e.hash.branch_path_hash for e in new_state.selector_map.values()
				)
				if not new_path_hashes.issubset(cached_path_hashes):
					# next action requires index but there are new elements on the page
					logger.info(f'Something new appeared after action {i } / {len(actions)}')
					break

			results.append(await self.act(action, browser_context))
>>>>>>> 39aa9e72dfecf6c485004f90b2b40190e4b0f1e3

			logger.debug(f'Executed action {i + 1} / {len(actions)}')
			if results[-1].is_done or results[-1].error or i == len(actions) - 1:
				break

			await asyncio.sleep(browser_context.config.wait_between_actions)
			# hash all elements. if it is a subset of cached_state its fine - else break (new elements on page)

		return results

	@time_execution_sync('--act')
<<<<<<< HEAD
	async def act(
		self,
		action: ActionModel,
		browser_context: BrowserContext,
		page_extraction_llm: Optional[BaseChatModel] = None,
		sensitive_data: Optional[Dict[str, str]] = None,
		available_file_paths: Optional[list[str]] = None,
	) -> ActionResult:
		"""Execute an action"""

		try:
			for action_name, params in action.model_dump(exclude_unset=True).items():
				if params is not None:
					with Laminar.start_as_current_span(
						name=action_name,
						input={
							'action': action_name,
							'params': params,
						},
						span_type='TOOL',
					):
						result = await self.registry.execute_action(
							action_name,
							params,
							browser=browser_context,
							page_extraction_llm=page_extraction_llm,
							sensitive_data=sensitive_data,
							available_file_paths=available_file_paths,
						)

						Laminar.set_span_output(result)

=======
	async def act(self, action: ActionModel, browser_context: BrowserContext) -> ActionResult:
		"""Execute an action"""
		try:
			for action_name, params in action.model_dump(exclude_unset=True).items():
				if params is not None:
					# remove highlights
					result = await self.registry.execute_action(
						action_name, params, browser=browser_context
					)
>>>>>>> 39aa9e72dfecf6c485004f90b2b40190e4b0f1e3
					if isinstance(result, str):
						return ActionResult(extracted_content=result)
					elif isinstance(result, ActionResult):
						return result
					elif result is None:
						return ActionResult()
					else:
						raise ValueError(f'Invalid action result type: {type(result)} of {result}')
			return ActionResult()
		except Exception as e:
			raise e
