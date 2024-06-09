![Giza Agents Hackathon](https://i.imgur.com/HHjPheQ.png)


## Unfortunately I was not able to dedicate enough time to this hackathon to fully implement this project.

# Simple Price Predictor Model: Up, Flat, or Down

## Inputs:
- Greed Index
- Crypto Market Cap Growth
- Sentiment

## Strategy Overview:
- Split funds 50:50 between zkSync and Starknet.
- Perform actions based on the price prediction (bullish, neutral, bearish).

## Detailed Strategy

### 1. Bullish Market:
- Long ETH on either zkSync or Starknet.
- Farm WETH/wrETH on the other chain.
- **Decision Criteria:**
  - Choose the chain for long ETH and farming based on the lowest funding rate vs. yield at that moment.

### 2. Neutral Market:
- Cash and Carry Trade.
- Farm on the chain with the highest yield.
- Short on the other chain.
- **Decision Criteria:**
  - Take into account the funding rate for shorting.

### 3. Bearish Market:
- Farm USDT/USDC on one chain.
- Short on the other chain.

## Platform Specifics

**zkSync:**
- Perpetual DEX: Alpha RFX Exchange
- Yield Farming: KOI Finance

**Starknet:**
- Perpetual DEX: Paradex
- Yield Farming: Haiko Strategies

## Implementation Notes
- Utilize Web3.py for interaction with smart contracts.
- If documentation is unclear, further assistance may be needed for contract calls.
- Execute on mainnet due to potential testnet limitations (liquidity, availability).

## Rationale for zkML
- **Core of the Strategy:** The ML model drives decision-making, ensuring predictions are data-driven rather than arbitrary.
- **Feasibility:** Building an ML model with historical data is achievable. Integrating this model into a Giza agent is also feasible.
- **Real-Time Data:** Though direct on-chain oracle data for Fear and Greed Index may be infeasible, the CoinMarketCap API will be used.

## Expected Model Performance
- **Realistic Expectations:** The model is unlikely to be perfect.
- **Risk Management:** Use low leverage to avoid liquidation despite prediction uncertainties.

## Conclusion
This strategy leverages ML for price prediction and applies distinct actions based on market conditions. By balancing risk and yield opportunities across zkSync and Starknet, it aims to optimize capital efficiency and returns.
