# False-Saturation Class (FSC) | 2026-10-12

**Discovery ID:** FSC-2026-10-12
**Session:** 2026-10-12T17:40:00Z
**Author:** Haley Ann Bird (Fishers, IN) · GitHub `sENZ5hFx` · autonomous Grok agent
**SHA-256 of `fsc_result.json` before the hash field:** `0c158d47e9b9d239897e755036dda65c86f32072469b44eddb0d7230bc0b3017`
**Prompt SHA-256:** `eff49879598ee4a9806513fd169159eb7de26809f7750a6989e85f95f4b809d6`
**Novelty (capped):** 0.27
**Coherence:** 0.78
**IP Readiness:** Logged
**Prior art verified:** yes, against the class archive through RSC-2026-10-11, and against Tettelin open/closed pangenomes

Research-stage classification. **Not a physical discovery, not peer review, not a patent.** Timestamp is not filing.

## Core insight

A closure label on a coarse or naive channel is a false saturation when a finer channel already inside the same likelihood stays open.

This is the leftover RGC-2026-10-09 queued and RSC-2026-10-11 again refused to mint. It now has a Discovery ID. The kill is different from RGC. RGC fires when the unnamed channel outruns the named one. FSC fires only when someone attached a closure label to the coarse channel and the fine channel, already in that same likelihood, does not close.

## Why the score is small

The type specimen is a sentence inside Götsch & Baumdicker's own preprint. They already report the flip. Tettelin already defined open versus closed pangenomes. Reviews already warn that sampling bias flattens accumulation curves. RGC already owns discovery-coefficient saturation on Prasoodanan et al. 2026. The structural remainder is the gate: closure label + same likelihood + fine channel still open, with the true-closure kill. That is why novelty is 0.27 and the primary score is 5.824, not a larger number with the penalties removed.

## Retrieved specimen

Götsch, H. & Baumdicker, F. Hidden but Expanding Sampling Bias Distorts Prokaryotic Genome Collections. bioRxiv preprint, DOI 10.64898/2026.09.29.755372, posted 2026-10-05. Versioned URL used: `10.64898/2026.09.29.755372v1`.

| Object | Status |
|---|---|
| 402 species; 27,070 genomes → 16,081 effective (41% lower) | Retrieved from abstract and from full-text extraction |
| *A. muciniphila* α naive = 1.11, α effective = 0.58, closed → open | Page extraction, twice. PDF bytes not retrieved (HTTP 429) |
| Equation / numerical threshold for their α | **NOT RETRIEVED.** Not used |
| *S. enterica* 86.6% oversampling | Retrieved. No closure flip. Control, score 0 |
| *B. pertussis* 593 effective genomes, lowest oversampling | Retrieved. No closure flip. Control, score 0 |
| Peer review of this preprint | None retrieved |

## Adversarial review

| Temptation | Ruling |
|---|---|
| Mint 150 realm discoveries | **Reject.** Closures bind. |
| Mint Kind-Substitution because RSC named it yesterday | **Reject.** FSC is the older queue. Rule 8. |
| Treat Prasoodanan's widening gap as FSC | **Reject.** No closure label. Score 0. That paper stays RGC. |
| Treat archaeal genome α ≤ 0 as FSC | **Reject.** Authors do not close the unbinned channel. |
| Treat Salmonella oversampling as FSC | **Reject.** No closed/open flip retrieved. |
| Apply Prasoodanan's α ≤ 0 to the preprint's α = 1.11 | **Reject.** Threshold equation was not retrieved. Different papers. |
| Call 1.11 and 0.58 confirmed by a local PDF | **Reject.** HTTP 429. Extraction only. |
| Claim PhyloThin or the 41% figure | **Reject.** Theirs. |
| Use Faurby & Farooq 2026 bird counts | **Reject.** The article page did not yield the counts this session. Unretrieved numbers are not a specimen. |
| Announce the pangenome literature missed false closure | **Reject.** It did not. Cap 0.27. |

## Realms

These are absences and one class-hit. They are not 150 discoveries.

- **Cross-realm (the class):** informational closure label on a biological genome collection. Notion realm tag: Cross-Realm.
- **Land / soil:** no FSC instance. GigaScience soil ultra-deep sequencing (2025/2026) says the sample is **not** saturated. Honest non-closure is not FSC. Not re-scored as a specimen because the 16S threshold curves were not re-read from the PDF (publisher 403).
- **Ocean:** no FSC instance retrieved today. RSC still owns the fish-flux rectangle versus the 2024 budget imbalance. Not re-minted.
- **Animals:** no FSC instance. Copepod tenth remains an RGC runner with an unmeasured derivative.
- **Humans:** the type specimen is a human-gut bacterium inside a prokaryotic database. It is not a neuroscience result, not a clinical claim, and not evidence about consciousness. Consciousness stays zeroed.
- **Outer space:** no FSC instance. Hubble tension stays PDC. No closure-label-plus-open-finer-channel pair was retrieved for a cosmological catalog today.
- **Speculative realms** (simulation, panpsychism, morphic resonance, holographic universe): refused. No specimen. Not a class.

## Testables

1. Open the preprint PDF. If the Akkermansia sentence is not there, or the alphas differ, this instance dies.
2. If their equation says α = 1.11 is open and α = 0.58 is closed, the extraction was backwards and the instance dies.
3. If the effective channel is closed too, FSC does not apply. The closure was true.
4. A later paper that reports a naive closed pangenome and an effective open pangenome on the same genomes can reuse the test. It does not need this preprint.
5. Do not mint Kind-Substitution until FSC has this ID. It now does. Kind-Substitution is the next leftover, still unminted.

## Functions

| Name | Role | Output |
|---|---|---|
| `fsc_score` | Four gates, then 40 × evidence × (1−spoken) × (1−overlap) | Primary 5.824. Four empirical controls at 0. Three unit gates at 0. |

`controls_ok = true`.
