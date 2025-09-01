import openai
from config import OPENAI_API_KEY
import earning

client = openai.OpenAI(api_key=OPENAI_API_KEY)  # Instantiate client

def ask_llm(prompt):
    chat_response = client.chat.completions.create(
        model="o3-mini",  # or "gpt-3.5-turbo"
        messages=[
            {"role": "user", "content": prompt}
        ],
    )
    return chat_response.choices[0].message.content

def get_profit_insights(profit_summary):
    prompt = f"Given the following summary for Tencent, explain business drivers, potential risks, and strategic recommendations:\n{profit_summary}"
    return ask_llm(prompt)


earnings = earning.analyze_earnings()
summary_for_llm = earnings.head(2).to_string()
insights = get_profit_insights(summary_for_llm)

print(insights)
