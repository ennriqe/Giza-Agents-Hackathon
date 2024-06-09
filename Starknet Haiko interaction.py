import asyncio
from starknet_py.contract import Contract
from starknet_py.net.account.account import Account
from starknet_py.net.models import StarknetChainId
from starknet_py.net.signer.stark_curve_signer import KeyPair
from starknet_py.net.full_node_client import FullNodeClient


# Not including these variables
address = ...
private_key = ...
node_url = ...

client = FullNodeClient(node_url=node_url)

deposit_call_data = [
    0x706c40d0e32c7508bb66c2274c2ffe52614aa30751fd23d3f6a5deffcbe402e,  # market_id
    1000000000000000000,  # base_amount
    491130484911633  # quote_amount
]

async def execute_transactions():
    account = Account(
        address=address,
        client=client,
        key_pair=KeyPair.from_private_key(private_key),
        chain=StarknetChainId.SEPOLIA_TESTNET)
    try:
        approve_contract_1 = await Contract.from_address(provider=account, address=0x04757e1150c243399a9accb7df2eb4b2956315b0effec8d5f26bb6065cf4edd2)
        deposit_tx = await approve_contract_1.functions["approve"].invoke_v1(
                    0x03c67e985e1902553e82db464c65e785aba17d7f853820b6225d6be840ff779a, 0,
                    max_fee=int(1e16))
        
        await deposit_tx.wait_for_acceptance()
        print('done')
        print(f"Approval successful: {deposit_tx.hash}")
        approve_contract_2 = await Contract.from_address(provider=account, address=0x052e4366eceb8234dfbc431cb9e8d1db1a062392300d68d35ec2fc09d99af2e2)


        deposit_tx = await approve_contract_2.functions["approve"].invoke_v1(
                    0x03c67e985e1902553e82db464c65e785aba17d7f853820b6225d6be840ff779a, 0,
                    max_fee=int(1e16)
                )
        await deposit_tx.wait_for_acceptance()

        print(f"Approval successful: {deposit_tx.hash}")

        deposit_contract = await Contract.from_address(
            provider=account,
            address=0x07263a8318aef20760c721df4fb7b9823f59a927a80e3289dcd6ef3e48ce9535,
        )

        # Get the current pool reserves and adjust them based on decimals 
        response_reserves = await deposit_contract.functions["get_balances"].call(market_id=deposit_call_data[0])       
        response_reserves = response_reserves[0]
        from decimal import Decimal

        base_decimals = Decimal('1e18')
        quote_decimals = Decimal('1e18')
        base_reserves = Decimal(response_reserves[0]) / base_decimals
        quote_reserves = Decimal(response_reserves[1]) / quote_decimals

        pool_ratio = base_reserves / quote_reserves
        desired_quote_amount = 0.05

        desired_base_amount = int(float(pool_ratio) * float(desired_quote_amount)) 

        print('desired_base_amount', desired_base_amount)

        print(int(desired_base_amount), int(desired_quote_amount))
        
        deposit_call_data[1] = int(desired_base_amount) #* 1e6) # convert to wei
        deposit_call_data[2] = int(desired_quote_amount) #* 1e18) # convert to wei 

        print(f"Adjusted deposit_call_data: {deposit_call_data}")
        print(deposit_call_data[0], deposit_call_data[1], deposit_call_data[2])
        deposit_tx = await deposit_contract.functions["deposit"].invoke_v1(
            
            market_id=deposit_call_data[0],
            base_amount=int(hex(deposit_call_data[1]), 16),
            quote_amount=int(hex(deposit_call_data[2]), 16),
            max_fee=int(1e16)
)
        print("success", deposit_tx)
        await deposit_tx.wait_for_acceptance()
        print(f"Deposit successful: {deposit_tx.hash}")
    except Exception as e:
        print(f"Error: {e}")
asyncio.run(execute_transactions())


