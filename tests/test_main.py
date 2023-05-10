from chatgpt_sample.main import create_prompt_template
from langchain import PromptTemplate


def test_create_prompt_template():
    template = """
    {subject}について30文字で教えて。
    """
    assert create_prompt_template() == PromptTemplate(
        template=template, input_variables=["subject"]
    )
