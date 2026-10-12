"""False-Saturation Class scorer. Research-stage. Not a measurement of nature."""
from __future__ import annotations

def fsc_score(*, naive_closed, effective_open, same_likelihood, closure_reported, spoken, prior_overlap, evidence):
    if not (0 <= spoken <= 1 and 0 <= prior_overlap <= 1 and 0 <= evidence <= 1):
        raise ValueError("penalties out of range")
    gates = {
        "naive_closed": bool(naive_closed),
        "effective_open": bool(effective_open),
        "same_likelihood": bool(same_likelihood),
        "closure_reported": bool(closure_reported),
    }
    if not all(gates.values()):
        failed = [k for k, v in gates.items() if not v]
        return {"score": 0.0, "verdict": "NOT_FSC", "failed_gates": failed, "gates": gates}
    score = round(40 * evidence * (1 - spoken) * (1 - prior_overlap), 4)
    return {"score": score, "verdict": "FSC", "failed_gates": [], "gates": gates}

def _check():
    primary = fsc_score(naive_closed=True, effective_open=True, same_likelihood=True, closure_reported=True, spoken=0.60, prior_overlap=0.48, evidence=0.70)
    assert primary["verdict"] == "FSC" and primary["score"] == 5.824
    assert fsc_score(naive_closed=True, effective_open=False, same_likelihood=True, closure_reported=True, spoken=0, prior_overlap=0, evidence=1)["score"] == 0.0
    assert fsc_score(naive_closed=True, effective_open=True, same_likelihood=False, closure_reported=True, spoken=0, prior_overlap=0, evidence=1)["score"] == 0.0
    assert fsc_score(naive_closed=True, effective_open=True, same_likelihood=True, closure_reported=False, spoken=0, prior_overlap=0, evidence=1)["score"] == 0.0
    assert fsc_score(naive_closed=False, effective_open=True, same_likelihood=True, closure_reported=False, spoken=0.6, prior_overlap=0.48, evidence=0.7)["score"] == 0.0
    print("fsc_score ok", primary["score"])

if __name__ == "__main__":
    _check()
