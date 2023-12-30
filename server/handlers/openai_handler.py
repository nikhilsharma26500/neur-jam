from openai import OpenAI


class OpenAIHandler:
    def get_response_openAI(
        self, model: str, system_message: str, user_query: str, api_key: str
    ):
        client = OpenAI(api_key=api_key)
        response = client.chat.completions.create(
            model=model,
            response_format={"type": "text"},
            messages=[
                {"role": "system", "content": system_message or "general purpose bot"},
                {"role": "user", "content": user_query},
            ],
        )

        output = response.choices[0].message.content
        return output
