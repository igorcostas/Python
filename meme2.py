import requests
from telegram import Bot
from telegram.constants import ParseMode
import asyncio

# Telegram bot credentials
API_ID = '27228531'
API_HASH = 'e3d9dd7233257fec3a982483211e5d4d'
BOT_TOKEN = '7745425789:AAFT8Nk84I_KIhxO4YmU1lHJe1t2DFUTQQc'
CHAT_ID = '1378607128'  # Substituído pelo ID real do seu chat

# Dexscreener API endpoint
API_ENDPOINT = "https://api.dexscreener.com/token-boosts/top/v1"

# Filters
LIQUIDITY_LIMIT = 100000  # <$100K
VOLUME_LIMIT = 250000  # <$250K
HOLDER_LIMIT = 300  # ≤300 holders
MIN_AGE_HOURS = 24  # ≥24 horas


async def get_tokens_with_boosts():
    """
    Fetch boosted token data from Dexscreener API.
    """
    try:
        response = requests.get(API_ENDPOINT)
        if response.status_code == 200:
            tokens = response.json()
            return tokens
        else:
            print(f"Failed to fetch data from Dexscreener. Status Code: {response.status_code}")
            return []
    except Exception as e:
        print(f"Error fetching data from Dexscreener: {e}")
        return []


def filter_tokens(tokens):
    """
    Filters tokens based on criteria (example only includes token address and description).
    """
    filtered_tokens = []
    for token in tokens:
        # Replace these criteria with the actual fields when available in the API response
        if token.get('amount', 0) < LIQUIDITY_LIMIT and token.get('totalAmount', 0) < VOLUME_LIMIT:
            filtered_tokens.append(token)
    return filtered_tokens


async def send_to_telegram(bot, tokens):
    """
    Send filtered tokens to Telegram chat.
    """
    for token in tokens:
        message = (
            f"🚀 Token Boost Detected!\n\n"
            f"🔗 URL: {token.get('url', 'N/A')}\n"
            f"📬 Address: {token.get('tokenAddress', 'N/A')}\n"
            f"📄 Description: {token.get('description', 'N/A')}\n"
            f"💰 Amount: {token.get('amount', 0)}\n"
            f"💸 Total Amount: {token.get('totalAmount', 0)}\n"
        )
        await bot.send_message(chat_id=CHAT_ID, text=message, parse_mode=ParseMode.MARKDOWN)


async def main():
    """
    Main function to fetch, filter, and send boosted tokens.
    """
    # Initialize the Telegram Bot
    bot = Bot(token=BOT_TOKEN)

    # Fetch boosted tokens
    tokens = await get_tokens_with_boosts()

    # Filter tokens based on criteria
    filtered_tokens = filter_tokens(tokens)

    if filtered_tokens:
        # Send to Telegram
        await send_to_telegram(bot, filtered_tokens)
    else:
        print("No tokens matched the criteria.")


if __name__ == "__main__":
    asyncio.run(main())
