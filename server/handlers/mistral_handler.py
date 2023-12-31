from dotenv import load_dotenv, find_dotenv
import fireworks.client


class MistralAIHandler:
    def get_response_MistralAI(
        self, model: str, system_message: str, user_query: str, api_key: str
    ):
        FIREWORKS_API_KEY = api_key
        fireworks.client.api_key = FIREWORKS_API_KEY

        if FIREWORKS_API_KEY:
            query = fireworks.client.ChatCompletion.create(
                model=f"accounts/fireworks/models/{model}",
                messages=[
                    {
                        "role": "system",
                        "content": system_message or "general purpose bot",
                    },
                    {
                        "role": "user",
                        "content": user_query,
                    },
                ],
                stream=False,
                n=1,
                max_tokens=1024,
                temperature=0.1,
                top_p=0.9,
                stop=[],
            )

            return query.choices[0].message.content

        else:
            raise ValueError("API key not found")
