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
    account_number = "2212328891"
    bank_code = "057"
    secret_key = "sk_live_013af7a7a1a2dc72b325f77b7951f3c9fa452187"

    async with aiohttp.ClientSession() as session:
        result = await get_paystack_bank_info(session, account_number, bank_code, secret_key)
        bank_data=json.dumps(result, indent=4)
        return bank_data

