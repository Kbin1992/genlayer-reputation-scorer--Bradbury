# 🧠 OnChain AI Reputation Scorer
### Built on GenLayer Bradbury Testnet

A decentralized reputation system powered by GenLayer Intelligent Contracts.  
Submit any claim with optional evidence URL — 5 independent AI validators fetch live web data, analyze credibility, and score 0–100 permanently on-chain. No centralized authority. No oracle needed.

---

## Live Demo

- **Frontend:** https://genlayer-reputation-scorer.vercel.app/
- **Contract:** 0xC98b670a84fa92301F898D74c32b08326F015F50
- **Network:** GenLayer Bradbury Testnet

---

## What It Does

Traditional smart contracts can't reason about language or fetch live web data. GenLayer changes this.

Submit a claim → validators fetch live evidence on-chain → 5 AI validators independently score credibility → verdict stored permanently on the blockchain.

**Verdict options:**
- ✅ **Credible** (70–100) — strong evidence supports the claim
- ⚠️ **Questionable** (30–69) — weak or mixed evidence found
- ❌ **Unverifiable** (0–29) — no supporting evidence found

---

## How It Works

```
User submits wallet + claim + optional URL
              ↓
leader_fn fetches evidence (gl.nondet.web.render)
              ↓
leader_fn calls AI (gl.nondet.exec_prompt)
              ↓
validator_fn checks each validator agrees on verdict
              ↓
gl.vm.run_nondet_unsafe reaches consensus
              ↓
Score + verdict stored on-chain via TreeMap
```

---

## Tech Stack

| Layer | Technology |
|-------|-----------|
| Blockchain | GenLayer Bradbury Testnet |
| Contract Language | Python Intelligent Contract |
| AI Consensus | `gl.vm.run_nondet_unsafe` + `validator_fn` |
| Web Fetching | `gl.nondet.web.render` |
| AI Prompting | `gl.nondet.exec_prompt` |
| Storage | `TreeMap[str, str]` |
| Frontend | HTML / CSS / JavaScript |

---

## Contract Details

**File:** `ReputationScorer.py`

**Key API used:**
```python
# { "Depends": "py-genlayer:1jb45aa8ynh2a9c9xn3b7qqh8sm5q93hwfp7jqmwsfhh8jpz09h6" }
```
This is the correct dependency string for Bradbury Testnet.

**Methods:**

| Method | Type | Description |
|--------|------|-------------|
| `score_claim(wallet, claim, url)` | Write | Scores a claim using AI + live web evidence |
| `get_last_result()` | Read | Returns the last verdict as JSON |
| `get_score(wallet)` | Read | Returns stored score for a wallet |

**Example response:**
```json
{
  "wallet": "0xYourWallet",
  "claim": "I am an active open source contributor",
  "score": 82,
  "verdict": "credible",
  "reason": "GitHub profile shows consistent commit history and public repos."
}
```

---

## Setup & Usage

### Prerequisites
- MetaMask wallet
- GenLayer Bradbury Testnet configured
- Free testnet GEN tokens

### Add GenLayer Bradbury to MetaMask
- **Network Name:** GenLayer Bradbury Testnet
- **RPC URL:** https://studio.genlayer.com:8443/api
- **Chain ID:** 42069
- **Currency:** GEN

### Get Testnet Tokens
→ [testnet-faucet.genlayer.foundation](https://testnet-faucet.genlayer.foundation)

### Deploy the Contract
1. Go to [studio.genlayer.com](https://studio.genlayer.com)
2. Create new contract → paste `ReputationScorer.py`
3. Click Deploy → copy your contract address
4. Replace `YOUR_CONTRACT_ADDRESS_HERE` in `index.html`

### Use the Frontend
1. Open `index.html` in browser (or deploy to Vercel)
2. Enter your wallet address + a claim
3. Optionally add an evidence URL
4. Click Score → wait 45–60 seconds for AI consensus
5. See your on-chain reputation score

---

## Example Claims to Try

```
Claim: "I am an active open source developer"
URL:   "https://github.com/yourusername"

Claim: "Bitcoin is the largest crypto by market cap"
URL:   "https://coinmarketcap.com"

Claim: "The Earth is flat"
URL:   (leave empty)

Claim: "GenLayer is an AI-powered blockchain"
URL:   "https://genlayer.com"
```

---

## Why GenLayer?

GenLayer Intelligent Contracts can:
- **Fetch live web data** directly on-chain — no oracle needed
- **Reason in natural language** using LLMs
- **Reach consensus** across 5 independent AI validators
- Handle **subjective decisions** traditional contracts cannot

The `gl.vm.run_nondet_unsafe` + `validator_fn` pattern used here is the correct Bradbury-compatible approach for non-deterministic consensus.

---

## Hackathon

Submitted to the **GenLayer Bradbury Builders Hackathon**
- Portal: [portal.genlayer.foundation](https://portal.genlayer.foundation)

---

## Builder Program

Built as part of the **GenLayer Incentivized Builder Program**.  
Learn more: [portal.genlayer.foundation](https://portal.genlayer.foundation)

---

## License

MIT
