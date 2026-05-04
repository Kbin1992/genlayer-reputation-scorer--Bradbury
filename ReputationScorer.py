# { "Depends": "py-genlayer:1jb45aa8ynh2a9c9xn3b7qqh8sm5q93hwfp7jqmwsfhh8jpz09h6" }
from genlayer import *
import json

class ReputationScorer(gl.Contract):
    scores: TreeMap[str, str]
    last_result: str

    def __init__(self):
        self.last_result = ""

    @gl.public.write
    def score_claim(self, wallet: str, claim: str, evidence_url: str) -> None:
        prompt = f"""You are an on-chain reputation system.
A user with wallet {wallet} is claiming: "{claim}"

Score their claim from 0 to 100 based on credibility.
Respond ONLY as JSON, nothing else:
{{"score": 75, "verdict": "credible", "reason": "Claim seems credible"}}

verdict must be one of: "credible", "questionable", "unverifiable"
"""

        def leader_fn():
            evidence = ""
            if evidence_url:
                try:
                    page = gl.nondet.web.render(evidence_url, mode="text")
                    evidence = page[:1500]
                except:
                    evidence = "Could not fetch"
            full_prompt = prompt + f"\nEvidence: {evidence}"
            return gl.nondet.exec_prompt(full_prompt, response_format="json")

        def validator_fn(leaders_res) -> bool:
            if not isinstance(leaders_res, gl.vm.Return):
                return False
            my_result = leader_fn()
            return my_result.get("verdict") == leaders_res.calldata.get("verdict")

        result = gl.vm.run_nondet_unsafe(leader_fn, validator_fn)

        self.scores[wallet] = json.dumps(result)
        self.last_result = json.dumps({
            "wallet": wallet,
            "claim": claim,
            "score": result.get("score", 0),
            "verdict": result.get("verdict", "unverifiable"),
            "reason": result.get("reason", "")
        })

    @gl.public.view
    def get_last_result(self) -> str:
        return self.last_result

    @gl.public.view
    def get_score(self, wallet: str) -> str:
        if wallet in self.scores:
            return self.scores[wallet]
        return json.dumps({"score": 0, "verdict": "no score yet"})
