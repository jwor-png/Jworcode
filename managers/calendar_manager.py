import anthropic

client = anthropic.Anthropic()

SYSTEM_PROMPT = """You are a CalendarManager agent. You handle all scheduling and calendar tasks including:
- Planning meetings, calls, and events
- Drafting calendar invites with agendas
- Resolving scheduling conflicts and suggesting optimal times
- Setting reminders and time-blocking work sessions
- Writing meeting agendas and post-meeting summaries
- Managing recurring commitments and deadlines

Be precise with times, dates, and logistics. Always confirm timezone when relevant."""


def run(request: str) -> str:
    response = client.messages.create(
        model="claude-opus-4-8",
        max_tokens=4096,
        thinking={"type": "adaptive"},
        system=SYSTEM_PROMPT,
        messages=[{"role": "user", "content": request}],
    )
    return next(
        (block.text for block in response.content if block.type == "text"),
        "",
    )
