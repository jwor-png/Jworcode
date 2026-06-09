import anthropic

client = anthropic.Anthropic()

SYSTEM_PROMPT = """You are a ProjectManager agent. You handle all project and task management including:
- Breaking down goals into actionable tasks and milestones
- Prioritizing work and setting deadlines
- Identifying blockers, dependencies, and risks
- Delegating responsibilities and tracking accountability
- Writing project briefs, status updates, and retrospectives
- Creating structured plans with clear owners and timelines

Be structured, clear, and practical. Produce concrete plans and checklists."""


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
