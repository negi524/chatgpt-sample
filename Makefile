main: log/ chatgpt_sample/.env
	poetry run dev

test:
	poetry run pytest tests/

format:
	poetry run black chatgpt_sample/ tests/

type-check:
	poetry run mypy chatgpt_sample/
