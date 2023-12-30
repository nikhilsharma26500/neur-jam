from dotenv import load_dotenv, find_dotenv
import fireworks.client

load_dotenv(find_dotenv())


class LlamaAIHandler:
    def get_response_llama(self, model: str, user_query: str, api_key: str):
        FIREWORKS_API_KEY = api_key
        fireworks.client.api_key = FIREWORKS_API_KEY

        if FIREWORKS_API_KEY:
            query = fireworks.client.ChatCompletion.create(
                model=f"accounts/fireworks/models/{model}",
                messages=[
                    {
                        "role": "system",
                        "content": "You are a general purpose bot",
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