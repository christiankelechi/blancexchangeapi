import asyncio
import json
import aiohttp

async def get_paystack_bank_info(session, account_number, bank_code, secret_key):
    async with session.get(
        f"https://api.paystack.co/bank/resolve?account_number={account_number}&bank_code={bank_code}",
        headers={"Authorization": f"Bearer {secret_key}"},
    ) as response:
        return await response.json()

async def main():
    account_number = "0001234567"
    bank_code = "058"
    secret_key = "YOUR_SECRET_KEY"

    async with aiohttp.ClientSession() as session:
        result = await get_paystack_bank_info(session, account_number, bank_code, secret_key)
        print(json.dumps(result, indent=4))

asyncio.run(main())