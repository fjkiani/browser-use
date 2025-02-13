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

# Quick start

With pip:

```bash
pip install browser-use
```

install playwright:

```bash
playwright install
```

Spin up your agent:

```python
from langchain_openai import ChatOpenAI
from browser_use import Agent
import asyncio
from dotenv import load_dotenv
load_dotenv()

async def main():
    agent = Agent(
        task="Go to Reddit, search for 'browser-use', click on the first post and return the first comment.",
        llm=ChatOpenAI(model="gpt-4o"),
    )
    result = await agent.run()
    print(result)

asyncio.run(main())
```

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
```

# Demos







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


## More examples

For more examples see the [examples](examples) folder or join the [Discord](https://link.browser-use.com/discord) and show off your project.

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




