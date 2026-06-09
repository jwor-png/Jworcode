import anthropic

client = anthropic.Anthropic()

SYSTEM_PROMPT = """You are a ResearchManager agent. You handle all research and intelligence tasks including:
- Analyzing topics, markets, competitors, and trends
- Summarizing complex information into clear briefs
- Writing research reports and executive summaries
- Identifying key insights and actionable recommendations
- Comparing options and presenting trade-offs
- Structuring data and findings for decision-making

Be thorough, objective, and well-organized. Cite reasoning clearly and highlight key takeaways."""


def run(request: str) -> str:
    response = client.messages.create(
        model="claude-opus-4-8",
        max_tokens=8192,
        thinking={"type": "adaptive"},
        system=SYSTEM_PROMPT,
        messages=[{"role": "user", "content": request}],
    )
    return next(
        (block.text for block in response.content if block.type == "text"),
        "",
    )
