import os
from openai import OpenAI

LOCAL_FILE = os.path.join(os.path.dirname(__file__), "sample.txt")

def init(ctx):
    mode = os.environ.get("LLM_MODE", "mock")
    ctx.logger.info(f"ℹ️ LLM_MODE={mode}")

    if mode == "remote":
        endpoint = os.environ.get("REMOTE_LLM_ENDPOINT", "")
        api_key  = os.environ.get("LLM_API_KEY", "")
        if not endpoint or not api_key:
            ctx.logger.error("⚠️ REMOTE_LLM_ENDPOINT or LLM_API_KEY missing")
            raise ValueError("Missing remote LLM config")
        ctx.llm_client = OpenAI(base_url=f"{endpoint}/v1", api_key=api_key)
    elif mode == "local":
        endpoint = os.environ.get("LOCAL_LLM_ENDPOINT", "")
        if not endpoint:
            ctx.logger.error("⚠️ LOCAL_LLM_ENDPOINT missing")
            raise ValueError("Missing local LLM config")
        ctx.llm_client = OpenAI(base_url=f"{endpoint}/v1", api_key="local")
    else:
        ctx.logger.info("ℹ️ Mocking LLM response")
        ctx.llm_client = None  # mock mode

    ctx.logger.info(f"Initialized in {mode} mode")

def handler(ctx, event):
    ctx.logger.info(f"ℹ️ Handler called: {event}")
    content = open(LOCAL_FILE).read()
    summary = llm_summary(ctx, content)
    ctx.logger.info(f"↩️ Summary: {summary}")
    return {"summary": summary}

def llm_summary(ctx, content):
    if ctx.llm_client is None:
        return "[mock] This is a placeholder summary for local testing without an LLM."

    model      = os.environ.get("MODEL_NAME", "gpt-4o-mini")
    max_tokens = int(os.environ.get("MAX_TOKENS", "512"))
    query      = f"Summarize in 1-2 sentences:\n{content}"

    completion = ctx.llm_client.chat.completions.create(
        model=model,
        messages=[{"role": "user", "content": query}],
        max_tokens=max_tokens,
        stream=True,
    )
    out = "".join(
        chunk.choices[0].delta.content
        for chunk in completion
        if chunk.choices[0].delta.content
    )
    return out.split("</think>")[-1].strip()

# if __name__ == "__main__":
#     class Logger:
#         def info(self, msg): print(msg)
#         def error(self, msg): print(f"ERROR: {msg}")

#     class Ctx:
#         logger = Logger()

#     ctx = Ctx()
#     init(ctx)
#     handler(ctx, None)