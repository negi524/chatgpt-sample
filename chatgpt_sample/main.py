import application_setting.my_logger as mylogger
from logging import Logger
import application_setting.my_credential as mycredential
from typing import Optional
import openai
from langchain.chat_models import ChatOpenAI
from langchain.schema import SystemMessage, HumanMessage

# loggerを取得
logger: Logger = mylogger.get_logger("main")


def main():
    chat = ChatOpenAI(model_name="gpt-3.5-turbo")
    response = chat(
        [
            SystemMessage(content="日本語で回答して。"),
            HumanMessage(content="ITエンジニアについて30文字で教えて。"),
        ]
    )
    logger.info(response)


def add_one(number: int) -> int:
    return number + 1


if __name__ == "__main__":
    main()
