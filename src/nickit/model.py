from datetime import datetime
from needle import Needle, tool


@tool
def get_now():
    """Get the current datetime"""
    return datetime.now().strftime('%Y-%m-%d %H:%M:%S')


def ask(prompt: str):
    agent = Needle(tools=[get_now])
    response = agent.run(prompt)
    return response['results']
