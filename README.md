# False-Saturation Class (FSC) | 2026-10-12T17:40:00Z

**Timestamp:** Monday, 12 October 2026, 13:40 EDT / `2026-10-12T17:40:00Z`
**Author / director:** Haley Ann Bird (Fishers, IN) · GitHub `sENZ5hFx`
**Agent:** Grok by xAI. Non-ownership. Structural synthesis aid only.
**Status:** Research-stage classification. **Not** a physical discovery, peer review, or patent.
**SHA-256** of `fsc_result.json` before the hash field was inserted: `0c158d47e9b9d239897e755036dda65c86f32072469b44eddb0d7230bc0b3017`
**Prompt SHA-256:** `eff49879598ee4a9806513fd169159eb7de26809f7750a6989e85f95f4b809d6`
**Novelty (capped):** 0.27 · **Coherence:** 0.78 · **Primary score:** 5.824

> Timestamp is not a filing. A hypothesis about nature is not patentable. Scores are a heuristic, not measurements of nature. Copyright may attach to this expression only. A preprint is not peer review.

## What this session is for

The standing prompt asks for never-made discoveries across a 10-plane, ~150-field taxonomy. Coverage Hole Lattice owns that generator. CLOSED-2026-09-30 and later closures bind. This session does not mint 150 discoveries.

Skill `high-agency-partner` rule 7, plus rule 8 (older queue wins): False-Saturation Class was queued by RGC-2026-10-09 and explicitly not minted by RSC-2026-10-11. Kind-Substitution was only named on 2026-10-11. The older leftover is this session. Kind-Substitution stays queued.

## Primary insight

**False-Saturation Class (FSC).** A closure label is attached to a coarse or naive channel. A finer channel already inside the same likelihood stays open. The closure is false.

Kill: if the finer channel is also closed under the source's own definition, the closure was true and FSC scores 0. If the channels are not the same samples, FSC scores 0. If nobody reported closure, FSC scores 0.

## Type specimen (not our result)

Götsch & Baumdicker, *Hidden but Expanding Sampling Bias Distorts Prokaryotic Genome Collections*, bioRxiv preprint [10.64898/2026.09.29.755372](https://doi.org/10.64898/2026.09.29.755372) (posted 2026-10-05). Not peer-reviewed in any record retrieved today.

Retrieved, not recomputed:

- 402 prokaryotic species. 27,070 full genomes → 16,081 effective genomes after PhyloThin (59% remain). Abstract: effective sample count is 41% lower.
- Quoted page extraction, returned twice: *Akkermansia muciniphila* α naive = 1.11, α effective = 0.58, "changing its classification from closed to open."
- The equation and numerical threshold that define their α were **not** on the extracted page. This log does not translate those alphas into anyone else's formula.
- PDF bytes were not retrieved (HTTP 429). Re-verify the quote against the PDF before citing it outside this log.

The preprint already says this. `spoken=0.60`. Overlap with Tettelin open/closed pangenomes and with RGC's discovery-coefficient family: `prior_overlap=0.48`. Evidence capped at 0.70 because the threshold equation and the PDF bytes are missing. Score **5.824**. Novelty capped at **0.27** for the same reason.

PhyloThin, the 41% figure, and the Akkermansia flip belong to Götsch and Baumdicker. This page does not claim them.

## Controls (must be ~0)

| Case | Score | Why it is not FSC |
|---|---:|---|
| *Salmonella enterica* 86.6% oversampling, same preprint | 0 | Oversampling without a retrieved closed-to-open label |
| *Bordetella pertussis*, 593 effective genomes, lowest oversampling | 0 | Low bias is not a closure flip and is not a saturation proof |
| Prasoodanan et al. 2026, archaeal genome α ≤ 0 | 0 | They refuse to close the unbinned channel. RGC's kill, not FSC |
| Prasoodanan et al. 2026, widening-gap sentence | 0 | RGC primary. No closure label |

Unit gates, not specimens: both channels closed → 0; finer channel from a later technology → 0; no closure sentence → 0.

## Not claimed

- Not 150 per-realm discoveries.
- Not that microbial diversity is now closed, or now open, as a fact of nature.
- Not a new alpha, a new genome count, or a new species.
- Not RGC, RSC, DPC, PDC, FPC, ANC, or TPC re-issued.
- Not Kind-Substitution (queued).
- Not a patent. Timestamp is not a filing.

## Files

- `fsc_result.json` — scorer output. SHA-256 in `SHA256.txt`
- `fsc_score.py` — `fsc_score`
- `session_log.json` — prompt, prompt hash, decision trace
- `skills/` — high-agency-partner, skill-creator, false-saturation-class
