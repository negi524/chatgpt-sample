import application_setting.my_logger as mylogger
from logging import Logger
import application_setting.my_credential as mycredential
from langchain import PromptTemplate
from langchain.chat_models import ChatOpenAI
from langchain.schema import SystemMessage, HumanMessage
from langchain.agents import load_tools, initialize_agent
from langchain.tools import AIPluginTool

# loggerを取得
logger: Logger = mylogger.get_logger("main")


def main():
    chat_with_plugin()
    # simple_chat()


def simple_chat():
    prompt = create_prompt_template()
    prompt_text = prompt.format(subject="ITエンジニア")

    chat = ChatOpenAI(model_name="gpt-3.5-turbo")

    response = chat(
        [
            SystemMessage(content="日本語で回答して。"),
            HumanMessage(content=prompt_text),
        ]
    )
    logger.info(response)


def chat_with_plugin():
    tool = AIPluginTool.from_plugin_url(
        "https://www.klarna.com/.well-known/ai-plugin.json"
    )
    tools = load_tools(["requests"])
    tools += [tool]

    chat = ChatOpenAI(model_name="gpt-3.5-turbo")

    agent_chain = initialize_agent(
        tools, chat, agent="zero-shot-react-description", verbose=True
    )
    response = agent_chain.run("what t shirts are available in klarna?")

    logger.info(response)


def create_prompt_template() -> PromptTemplate:
    """
    プロンプトのテンプレートを生成する
    """

    template = """
    {subject}について30文字で教えて。
    """

    return PromptTemplate(template=template, input_variables=["subject"])


if __name__ == "__main__":
    main()
