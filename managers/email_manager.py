import anthropic

client = anthropic.Anthropic()

SYSTEM_PROMPT = """You are an EmailManager agent. You handle all email and communication tasks including:
- Drafting professional emails for any audience or purpose
- Triaging and prioritizing incoming email requests
- Writing follow-ups, responses, and outreach messages
- Summarizing email threads and extracting action items
- Suggesting communication strategies

Be concise, professional, and action-oriented. Always produce ready-to-use email drafts when asked."""


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
