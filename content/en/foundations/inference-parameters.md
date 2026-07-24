---
title: "Inference Parameters"
weight: 13
description: The knobs that shape a model's output — temperature, top-p/top-k, max tokens, stop.
---

At request time a few parameters shape *how* the model generates. These are the everyday
knobs for controlling output.

## The core knobs

| Parameter | Controls | Typical use |
| ----------- | ---------- | ------------- |
| Temperature | Randomness | Low (~0) = focused/deterministic-ish; high = creative/varied |
| Top-p (nucleus) | Sampling from the top probability mass | Alternative to temperature; lower = safer |
| Top-k | Sampling from the top *k* candidates | Similar effect; caps the candidate pool |
| Max tokens | Length cap on the output | Prevent runaway or truncated responses |
| Stop sequences | Strings that end generation | Cut off at a delimiter you control |

## Temperature, in practice

- **Low** for extraction, classification, code, factual answers — you want consistency.
- **Higher** for brainstorming, copy, variety — you want range.
- Don't tune temperature *and* top-p aggressively at once; pick one lever.
- Even at temperature 0, output isn't guaranteed identical every time.

## `max_tokens` is a hard cap

If the model hits it mid-sentence, the response is truncated — raise the limit or stream long
outputs. Remember input + output share the [context window]({{< relref "/foundations/how-llms-work" >}}).

## A note on newer models

Some newer models are moving away from manual sampling knobs toward higher-level controls —
e.g. an **effort / reasoning** setting, or automatic ("adaptive") reasoning — and may reject
`temperature`/`top_p`/`top_k`. Check your provider's current API before assuming the classic
knobs are available.
