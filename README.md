<<<<<<< HEAD
<picture>
  <source media="(prefers-color-scheme: dark)" srcset="./static/browser-use-dark.png">
  <source media="(prefers-color-scheme: light)" srcset="./static/browser-use.png">
  <img alt="Shows a black Browser Use Logo in light color mode and a white one in dark color mode." src="./static/browser-use.png"  width="full">
</picture>

<h1 align="center">Enable AI to control your browser 🤖</h1>

[![GitHub stars](https://img.shields.io/github/stars/gregpr07/browser-use?style=social)](https://github.com/gregpr07/browser-use/stargazers)
[![Discord](https://img.shields.io/discord/1303749220842340412?color=7289DA&label=Discord&logo=discord&logoColor=white)](https://link.browser-use.com/discord)
[![Documentation](https://img.shields.io/badge/Documentation-📕-blue)](https://docs.browser-use.com)
[![Cloud](https://img.shields.io/badge/Cloud-☁️-blue)](https://cloud.browser-use.com)
[![Twitter Follow](https://img.shields.io/twitter/follow/Gregor?style=social)](https://x.com/gregpr07)
[![Twitter Follow](https://img.shields.io/twitter/follow/Magnus?style=social)](https://x.com/mamagnus00)
[![Weave Badge](https://img.shields.io/endpoint?url=https%3A%2F%2Fapp.workweave.ai%2Fapi%2Frepository%2Fbadge%2Forg_T5Pvn3UBswTHIsN1dWS3voPg%2F881458615&labelColor=#EC6341)](https://app.workweave.ai/reports/repository/org_T5Pvn3UBswTHIsN1dWS3voPg/881458615)


Folder structure:
Directory structure:
└── browser-use-browser-use/
    ├── README.md
    ├── LICENSE
    ├── SECURITY.md
    ├── codebeaver.yml
    ├── conftest.py
    ├── pyproject.toml
    ├── pytest.ini
    ├── .env.example
    ├── .pre-commit-config.yaml
    ├── .python-version
    ├── browser_use/
    │   ├── README.md
    │   ├── __init__.py
    │   ├── logging_config.py
    │   ├── utils.py
    │   ├── agent/
    │   │   ├── prompts.py
    │   │   ├── service.py
    │   │   ├── tests.py
    │   │   ├── views.py
    │   │   └── message_manager/
    │   │       ├── service.py
    │   │       ├── tests.py
    │   │       └── views.py
    │   ├── browser/
    │   │   ├── browser.py
    │   │   ├── context.py
    │   │   ├── views.py
    │   │   └── tests/
    │   │       ├── screenshot_test.py
    │   │       └── test_clicks.py
    │   ├── controller/
    │   │   ├── service.py
    │   │   ├── views.py
    │   │   └── registry/
    │   │       ├── service.py
    │   │       └── views.py
    │   ├── dom/
    │   │   ├── __init__.py
    │   │   ├── buildDomTree.js
    │   │   ├── service.py
    │   │   ├── views.py
    │   │   ├── history_tree_processor/
    │   │   │   ├── service.py
    │   │   │   └── view.py
    │   │   └── tests/
    │   │       ├── extraction_test.py
    │   │       └── process_dom_test.py
    │   └── telemetry/
    │       ├── service.py
    │       └── views.py
    ├── docs/
    │   ├── README.md
    │   ├── development.mdx
    │   ├── introduction.mdx
    │   ├── mint.json
    │   ├── quickstart.mdx
    │   ├── cloud/
    │   │   ├── implementation.mdx
    │   │   └── quickstart.mdx
    │   ├── customize/
    │   │   ├── agent-settings.mdx
    │   │   ├── browser-settings.mdx
    │   │   ├── custom-functions.mdx
    │   │   ├── output-format.mdx
    │   │   ├── real-browser.mdx
    │   │   ├── sensitive-data.mdx
    │   │   ├── supported-models.mdx
    │   │   └── system-prompt.mdx
    │   ├── development/
    │   │   ├── contribution-guide.mdx
    │   │   ├── local-setup.mdx
    │   │   ├── observability.mdx
    │   │   ├── roadmap.mdx
    │   │   └── telemetry.mdx
    │   ├── images/
    │   └── logo/
    ├── eval/
    │   └── gpt-4o.py
    ├── examples/
    │   ├── simple.py
    │   ├── browser/
    │   │   ├── real_browser.py
    │   │   └── using_cdp.py
    │   ├── custom-functions/
    │   │   ├── advanced_search.py
    │   │   ├── clipboard.py
    │   │   ├── file_upload.py
    │   │   ├── notification.py
    │   │   └── save_to_file_hugging_face.py
    │   ├── features/
    │   │   ├── custom_output.py
    │   │   ├── custom_system_prompt.py
    │   │   ├── custom_user_agent.py
    │   │   ├── download_file.py
    │   │   ├── follow_up_tasks.py
    │   │   ├── initial_actions.py
    │   │   ├── multi-tab_handling.py
    │   │   ├── multiple_agents_same_browser.py
    │   │   ├── parallel_agents.py
    │   │   ├── pause_agent.py
    │   │   ├── planner.py
    │   │   ├── restrict_urls.py
    │   │   ├── result_processing.py
    │   │   ├── save_trace.py
    │   │   ├── sensitive_data.py
    │   │   ├── small_model_for_extraction.py
    │   │   └── validate_output.py
    │   ├── integrations/
    │   │   ├── discord/
    │   │   │   ├── discord_api.py
    │   │   │   └── discord_example.py
    │   │   └── slack/
    │   │       ├── README.md
    │   │       ├── slack_api.py
    │   │       └── slack_example.py
    │   ├── models/
    │   │   ├── azure_openai.py
    │   │   ├── bedrock_claude.py
    │   │   ├── deepseek-r1.py
    │   │   ├── deepseek.py
    │   │   ├── gemini.py
    │   │   ├── gpt-4o.py
    │   │   ├── ollama.py
    │   │   └── qwen.py
    │   ├── notebook/
    │   │   └── agent_browsing.ipynb
    │   ├── ui/
    │   │   ├── command_line.py
    │   │   └── gradio_demo.py
    │   └── use-cases/
    │       ├── README.md
    │       ├── captcha.py
    │       ├── check_appointment.py
    │       ├── find_and_apply_to_jobs.py
    │       ├── online_coding_agent.py
    │       ├── post-twitter.py
    │       ├── scrolling_page.py
    │       ├── shopping.py
    │       ├── test_cv.txt
    │       ├── twitter_cookies.txt
    │       ├── twitter_post_using_cookies.py
    │       └── web_voyager_agent.py
    ├── static/
    ├── tests/
    │   ├── conftest.py
    │   ├── test_agent_actions.py
    │   ├── test_attach_chrome.py
    │   ├── test_context.py
    │   ├── test_core_functionality.py
    │   ├── test_dropdown.py
    │   ├── test_dropdown_complex.py
    │   ├── test_dropdown_error.py
    │   ├── test_excluded_actions.py
    │   ├── test_full_screen.py
    │   ├── test_gif_path.py
    │   ├── test_mind2web.py
    │   ├── test_models.py
    │   ├── test_qwen.py
    │   ├── test_react_dropdown.py
    │   ├── test_save_conversation.py
    │   ├── test_self_registered_actions.py
    │   ├── test_service.py
    │   ├── test_stress.py
    │   ├── test_vision.py
    │   └── mind2web_data/
    │       └── processed.json
    └── .github/
        ├── ISSUE_TEMPLATE/
        │   ├── bug_report.yml
        │   ├── config.yml
        │   ├── docs_issue.yml
        │   └── feature_request.yml
        └── workflows/
            └── publish.yml



🌐 Browser-use is the easiest way to connect your AI agents with the browser. 

💡 See what others are building and share your projects in our [Discord](https://link.browser-use.com/discord) - we'd love to see what you create!

🌩️ Skip the setup - try our hosted version for instant browser automation! [Try it now](https://cloud.browser-use.com).
=======
<img src="./static/browser-use.png" alt="Browser Use Logo" width="full"/>

<br/>

[![GitHub stars](https://img.shields.io/github/stars/gregpr07/browser-use?style=social)](https://github.com/gregpr07/browser-use/stargazers)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python 3.11+](https://img.shields.io/badge/python-3.11+-blue.svg)](https://www.python.org/downloads/)
[![Discord](https://img.shields.io/discord/1303749220842340412?color=7289DA&label=Discord&logo=discord&logoColor=white)](https://link.browser-use.com/discord)

Make websites accessible for AI agents 🤖.

Browser use is the easiest way to connect your AI agents with the browser. If you have used Browser Use for your project feel free to show it off in our [Discord](https://link.browser-use.com/discord).
>>>>>>> 39aa9e72dfecf6c485004f90b2b40190e4b0f1e3

# Quick start

With pip:

```bash
pip install browser-use
```

<<<<<<< HEAD
install playwright:
=======
(optional) install playwright:
>>>>>>> 39aa9e72dfecf6c485004f90b2b40190e4b0f1e3

```bash
playwright install
```

Spin up your agent:

```python
from langchain_openai import ChatOpenAI
from browser_use import Agent
import asyncio
<<<<<<< HEAD
from dotenv import load_dotenv
load_dotenv()

async def main():
    agent = Agent(
        task="Go to Reddit, search for 'browser-use', click on the first post and return the first comment.",
=======

async def main():
    agent = Agent(
        task="Find a one-way flight from Bali to Oman on 12 January 2025 on Google Flights. Return me the cheapest option.",
>>>>>>> 39aa9e72dfecf6c485004f90b2b40190e4b0f1e3
        llm=ChatOpenAI(model="gpt-4o"),
    )
    result = await agent.run()
    print(result)

asyncio.run(main())
```

<<<<<<< HEAD
Add your API keys for the provider you want to use to your `.env` file.

```bash
OPENAI_API_KEY=
```

For other settings, models, and more, check out the [documentation 📕](https://docs.browser-use.com).


### Test with UI

You can test [browser-use with a UI repository](https://github.com/browser-use/web-ui)

Or simply run the gradio example:

```
uv pip install gradio
```

```bash
python examples/ui/gradio_demo.py
=======
And don't forget to add your API keys to your `.env` file.

```bash
OPENAI_API_KEY=
ANTHROPIC_API_KEY=
>>>>>>> 39aa9e72dfecf6c485004f90b2b40190e4b0f1e3
```

# Demos

<<<<<<< HEAD






<br/><br/>

[Task](https://github.com/browser-use/browser-use/blob/main/examples/use-cases/shopping.py): Add grocery items to cart, and checkout.

[![AI Did My Groceries](https://github.com/user-attachments/assets/d9359085-bde6-41d4-aa4e-6520d0221872)](https://www.youtube.com/watch?v=L2Ya9PYNns8)


<br/><br/>


Prompt: Add my latest LinkedIn follower to my leads in Salesforce.

![LinkedIn to Salesforce](https://github.com/user-attachments/assets/1440affc-a552-442e-b702-d0d3b277b0ae)

<br/><br/>

[Prompt](https://github.com/browser-use/browser-use/blob/main/examples/use-cases/find_and_apply_to_jobs.py): Read my CV & find ML jobs, save them to a file, and then start applying for them in new tabs, if you need help, ask me.'

https://github.com/user-attachments/assets/171fb4d6-0355-46f2-863e-edb04a828d04

<br/><br/>

[Prompt](https://github.com/browser-use/browser-use/blob/main/examples/browser/real_browser.py): Write a letter in Google Docs to my Papa, thanking him for everything, and save the document as a PDF.

![Letter to Papa](https://github.com/user-attachments/assets/242ade3e-15bc-41c2-988f-cbc5415a66aa)

<br/><br/>

[Prompt](https://github.com/browser-use/browser-use/blob/main/examples/custom-functions/save_to_file_hugging_face.py): Look up models with a license of cc-by-sa-4.0 and sort by most likes on Hugging face, save top 5 to file.

https://github.com/user-attachments/assets/de73ee39-432c-4b97-b4e8-939fd7f323b3


<br/><br/>

=======
<div style="font-size: 4em;">
    Prompt: Read my CV & find ML jobs, save them to a file, and then start applying for them in new tabs, if you need help, ask me.' (8x speed)
</div>

https://github.com/user-attachments/assets/171fb4d6-0355-46f2-863e-edb04a828d04

<div style="font-size: 4em;">
    Prompt: Find flights on kayak.com from Zurich to Beijing from 25.12.2024 to 02.02.2025. (8x speed)
</div>

![flight search 8x 10fps](https://github.com/user-attachments/assets/ea605d4a-90e6-481e-a569-f0e0db7e6390)

<div style="font-size: 4em;">
    Prompt: Look up models with a license of cc-by-sa-4.0 and sort by most likes on Hugging face, save top 5 to file. (1x speed)
</div>

https://github.com/user-attachments/assets/de73ee39-432c-4b97-b4e8-939fd7f323b3

# Features ⭐

- Vision + html extraction
- Automatic multi-tab management
- Extract clicked elements XPaths and repeat exact LLM actions
- Add custom actions (e.g. save to file, push to database, notify me, get human input)
- Self-correcting
- Use any LLM supported by LangChain (e.g. gpt4o, gpt4o mini, claude 3.5 sonnet, llama 3.1 405b, etc.)
- Parallelize as many agents as you want

## Register custom actions

If you want to add custom actions your agent can take, you can register them like this:

You can use BOTH sync or async functions.

```python
from browser_use.agent.service import Agent
from browser_use.browser.service import Browser
from browser_use.controller.service import Controller

# Initialize controller first
controller = Controller()

@controller.action('Ask user for information')
def ask_human(question: str, display_question: bool) -> str:
	return input(f'\n{question}\nInput: ')
```

Or define your parameters using Pydantic

```python
class JobDetails(BaseModel):
  title: str
  company: str
  job_link: str
  salary: Optional[str] = None

@controller.action('Save job details which you found on page', param_model=JobDetails, requires_browser=True)
async def save_job(params: JobDetails, browser: Browser):
	print(params)

  # use the browser normally
  page = browser.get_current_page()
	page.go_to(params.job_link)
```

and then run your agent:

```python
model = ChatAnthropic(model_name='claude-3-5-sonnet-20240620', timeout=25, stop=None, temperature=0.3)
agent = Agent(task=task, llm=model, controller=controller)

await agent.run()
```

## Parallelize agents

In 99% cases you should use 1 Browser instance and parallelize the agents with 1 context per agent.
You can also reuse the context after the agent finishes.

```python
browser = Browser()
```

```python
for i in range(10):
    # This create a new context and automatically closes it after the agent finishes (with `__aexit__`)
    async with browser.new_context() as context:
        agent = Agent(task=f"Task {i}", llm=model, browser_context=context)

        # ... reuse context
```

If you would like to learn more about how this works under the hood you can learn more at [playwright browser-context](https://playwright.dev/python/docs/api/class-browsercontext).

### Context vs Browser

If you don't specify a `browser` or `browser_context` the agent will create a new browser instance and context.

## Get XPath history

To get the entire history of everything the agent has done, you can use the output of the `run` method:

```python
history: list[AgentHistory] = await agent.run()

print(history)
```

## Browser configuration

You can configure the browser using the `BrowserConfig` and `BrowserContextConfig` classes.

The most important options are:

- `headless`: Whether to run the browser in headless mode
- `keep_open`: Whether to keep the browser open after the script finishes
- `disable_security`: Whether to disable browser security features (very useful if dealing with cross-origin requests like iFrames)
- `cookies_file`: Path to a cookies file for persistence
- `minimum_wait_page_load_time`: Minimum time to wait before getting the page state for the LLM input
- `wait_for_network_idle_page_load_time`: Time to wait for network requests to finish before getting the page state
- `maximum_wait_page_load_time`: Maximum time to wait for the page to load before proceeding anyway
>>>>>>> 39aa9e72dfecf6c485004f90b2b40190e4b0f1e3

## More examples

For more examples see the [examples](examples) folder or join the [Discord](https://link.browser-use.com/discord) and show off your project.

<<<<<<< HEAD
# Vision

Tell your computer what to do, and it gets it done.

## Roadmap

- [ ] Improve memory management
- [ ] Enhance planning capabilities
- [ ] Improve self-correction
- [ ] Fine-tune the model for better performance
- [ ] Create datasets for complex tasks
- [ ] Sandbox browser-use for specific websites
- [ ] Implement deterministic script rerun with LLM fallback
- [ ] Cloud-hosted version
- [ ] Add stop/pause functionality
- [ ] Improve authentication handling
- [ ] Reduce token consumption
- [ ] Implement long-term memory
- [ ] Handle repetitive tasks reliably
- [ ] Third-party integrations (Slack, etc.)
- [ ] Include more interactive elements
- [ ] Human-in-the-loop execution
- [ ] Benchmark various models against each other
- [ ] Let the user record a workflow and browser-use will execute it
- [ ] Improve the generated GIF quality
- [ ] Create various demos for tutorial execution, job application, QA testing, social media, etc.

## Contributing

We love contributions! Feel free to open issues for bugs or feature requests. To contribute to the docs, check out the `/docs` folder.

## Local Setup

To learn more about the library, check out the [local setup 📕](https://docs.browser-use.com/development/local-setup).

## Cooperations

We are forming a commission to define best practices for UI/UX design for browser agents.
Together, we're exploring how software redesign improves the performance of AI agents and gives these companies a competitive advantage by designing their existing software to be at the forefront of the agent age.

Email [Toby](mailto:tbiddle@loop11.com?subject=I%20want%20to%20join%20the%20UI/UX%20commission%20for%20AI%20agents&body=Hi%20Toby%2C%0A%0AI%20found%20you%20in%20the%20browser-use%20GitHub%20README.%0A%0A) to apply for a seat on the committee.
## Citation

If you use Browser Use in your research or project, please cite:


    
```bibtex
@software{browser_use2024,
  author = {Müller, Magnus and Žunič, Gregor},
  title = {Browser Use: Enable AI to control your browser},
  year = {2024},
  publisher = {GitHub},
  url = {https://github.com/browser-use/browser-use}
}
```
 


 <div align="center"> <img src="https://github.com/user-attachments/assets/402b2129-b6ac-44d3-a217-01aea3277dce" width="400"/> 
 
[![Twitter Follow](https://img.shields.io/twitter/follow/Gregor?style=social)](https://x.com/gregpr07)
[![Twitter Follow](https://img.shields.io/twitter/follow/Magnus?style=social)](https://x.com/mamagnus00)
 
 </div> 

<div align="center">
Made with ❤️ in Zurich and San Francisco
 </div> 




=======
## Telemetry

We collect anonymous usage data to help us understand how the library is being used and to identify potential issues. There is no privacy risk, as no personal information is collected. We collect data with PostHog.

You can opt out of telemetry by setting the `ANONYMIZED_TELEMETRY=false` environment variable.

# Contributing

Contributions are welcome! Feel free to open issues for bugs or feature requests.

## Local Setup

1. Create a virtual environment and install dependencies:

```bash
# To install all dependencies including dev
pip install . ."[dev]"
```

2. Add your API keys to the `.env` file:

```bash
cp .env.example .env
```

or copy the following to your `.env` file:

```bash
OPENAI_API_KEY=
ANTHROPIC_API_KEY=
```

You can use any LLM model supported by LangChain by adding the appropriate environment variables. See [langchain models](https://python.langchain.com/docs/integrations/chat/) for available options.

### Building the package

```bash
hatch build
```

Feel free to join the [Discord](https://link.browser-use.com/discord) for discussions and support.

---

<div align="center">
  <b>Star ⭐ this repo if you find it useful!</b><br>
  Made with ❤️ by the Browser-Use team
</div>
>>>>>>> 39aa9e72dfecf6c485004f90b2b40190e4b0f1e3
