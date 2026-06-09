#!/usr/bin/env python3
"""Business orchestration tree — top-level orchestrator that delegates to domain managers."""

import anthropic
from managers import email_manager, project_manager, research_manager, calendar_manager

client = anthropic.Anthropic()

SYSTEM_PROMPT = """You are a top-level business orchestrator. You receive requests from the business owner and route them to the appropriate specialist manager:

- EmailManager: drafting emails, writing follow-ups, communication strategy, triaging inbox
- ProjectManager: task planning, milestones, deadlines, project briefs, delegation
- ResearchManager: research reports, market analysis, summaries, competitive intelligence
- CalendarManager: scheduling meetings, setting reminders, calendar invites, time-blocking

For each request:
1. Identify which manager (or combination) is best suited
2. Call the appropriate manager tool(s) with a clear, focused sub-request
3. Synthesize the manager response(s) into a final answer for the user

If a request spans multiple domains (e.g., "schedule a meeting and draft the invite"), call both relevant managers and combine their output."""

tools = [
    {
        "name": "email_manager",
        "description": "Handles email drafting, communication, follow-ups, inbox triage, and outreach.",
        "input_schema": {
            "type": "object",
            "properties": {
                "request": {
                    "type": "string",
                    "description": "The email or communication task to perform.",
                }
            },
            "required": ["request"],
        },
    },
    {
        "name": "project_manager",
        "description": "Handles task management, project planning, milestones, delegation, and status tracking.",
        "input_schema": {
            "type": "object",
            "properties": {
                "request": {
                    "type": "string",
                    "description": "The project or task management request.",
                }
            },
            "required": ["request"],
        },
    },
    {
        "name": "research_manager",
        "description": "Handles research, analysis, reports, summaries, and competitive intelligence.",
        "input_schema": {
            "type": "object",
            "properties": {
                "request": {
                    "type": "string",
                    "description": "The research or analysis task to perform.",
                }
            },
            "required": ["request"],
        },
    },
    {
        "name": "calendar_manager",
        "description": "Handles scheduling, meetings, calendar invites, reminders, and time-blocking.",
        "input_schema": {
            "type": "object",
            "properties": {
                "request": {
                    "type": "string",
                    "description": "The scheduling or calendar task to perform.",
                }
            },
            "required": ["request"],
        },
    },
]

MANAGER_MAP = {
    "email_manager": email_manager.run,
    "project_manager": project_manager.run,
    "research_manager": research_manager.run,
    "calendar_manager": calendar_manager.run,
}


def run(user_request: str) -> str:
    messages = [{"role": "user", "content": user_request}]

    while True:
        response = client.messages.create(
            model="claude-opus-4-8",
            max_tokens=8192,
            thinking={"type": "adaptive"},
            system=SYSTEM_PROMPT,
            tools=tools,
            messages=messages,
        )

        tool_uses = [b for b in response.content if b.type == "tool_use"]

        if not tool_uses:
            return next(
                (b.text for b in response.content if b.type == "text"),
                "",
            )

        messages.append({"role": "assistant", "content": response.content})

        tool_results = []
        for tool_use in tool_uses:
            manager_fn = MANAGER_MAP[tool_use.name]
            result = manager_fn(tool_use.input["request"])
            tool_results.append(
                {
                    "type": "tool_result",
                    "tool_use_id": tool_use.id,
                    "content": result,
                }
            )

        messages.append({"role": "user", "content": tool_results})


def main():
    print("Business Orchestrator — type your request (Ctrl+C to quit)\n")
    while True:
        try:
            user_input = input("You: ").strip()
            if not user_input:
                continue
            print("\nOrchestrator: thinking...\n")
            result = run(user_input)
            print(f"Orchestrator:\n{result}\n")
        except KeyboardInterrupt:
            print("\nGoodbye.")
            break


if __name__ == "__main__":
    main()
