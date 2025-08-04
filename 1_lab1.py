# ---
# jupyter:
#   jupytext:
#     text_representation:
#       extension: .py
#       format_name: percent
#       format_version: '1.3'
#       jupytext_version: 1.17.1
#   kernelspec:
#     display_name: .venv
#     language: python
#     name: python3
# ---

# %% [markdown]
# ## Week 2 Day 1
#
# And now! Our first look at OpenAI Agents SDK
#
# You won't believe how lightweight this is..

# %% [markdown]
# <table style="margin: 0; text-align: left; width:100%">
#     <tr>
#         <td style="width: 150px; height: 150px; vertical-align: middle;">
#             <img src="../assets/tools.png" width="150" height="150" style="display: block;" />
#         </td>
#         <td>
#             <h2 style="color:#00bfff;">The OpenAI Agents SDK Docs</h2>
#             <span style="color:#00bfff;">The documentation on OpenAI Agents SDK is really clear and simple: <a href="https://openai.github.io/openai-agents-python/">https://openai.github.io/openai-agents-python/</a> and it's well worth a look.
#             </span>
#         </td>
#     </tr>
# </table>

# %%
# The imports

from dotenv import load_dotenv
from agents import Agent, Runner, trace



# %%
# The usual starting point

load_dotenv(override=True)


# %%

# Make an agent with name, instructions, model

agent = Agent(name="Jokester", instructions="You are a joke teller", model="gpt-4o-mini")

# %%
# Run the joke with Runner.run(agent, prompt) then print final_output

with trace("Telling a joke"):
    result = await Runner.run(agent, "Tell a joke about Autonomous AI Agents")
    print(result.final_output)

# %% [markdown]
# ## Now go and look at the trace
#
# https://platform.openai.com/traces
