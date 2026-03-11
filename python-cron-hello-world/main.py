import os

secrets = {}

def init(ctx):
    global secrets
    # One time initialization comes here
    ctx.logger.info("Initialized...")
    ctx.logger.info(f"{os.environ.get('GREETING')}")
    secrets = ctx.secrets.get("credentials", {}) if ctx.secrets else {}

def handler(ctx, event):
    # Events Processing comes here
    ctx.logger.info(f"Handler {event}")
    ctx.logger.info(f"secrets: {secrets}")
    return "Hello World"