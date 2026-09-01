from data.crochet_info import CROCHET_INFO
from utils.display import print_title, show_message, pause


def show_tool_info(topic, title=None):
    info = CROCHET_INFO.get(topic)
    heading = title if title else topic.replace("_", " ")

    print_title(heading.upper())

    if info is None:
        show_message("Sorry, there is no information about this topic yet.")
    elif isinstance(info, dict):
        for short, meaning in info.items():
            show_message(f"  {short:<7} = {meaning}")
    else:
        show_message(info)

    pause()
