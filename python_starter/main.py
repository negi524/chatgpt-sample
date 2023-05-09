import application_setting.my_logger as mylogger
from logging import Logger
import application_setting.my_credential as mycredential
from typing import Optional
import openai

# loggerを取得
logger: Logger = mylogger.get_logger("main")


def main():
    openai.api_key = mycredential.OPENAI_API_KEY
    print(mycredential.OPENAI_API_KEY)
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "あなたは賢いAIです。"},
            {"role": "user", "content": "1たす1は？"},
        ],
    )
    print(response["choices"][0]["message"]["content"])


def add_one(number: int) -> int:
    return number + 1


if __name__ == "__main__":
    main()
