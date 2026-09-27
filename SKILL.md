---
name: writing-linkedin-posts
description: Use when drafting, rewriting, or reviewing a LinkedIn post, especially one about a project, repo, launch, release, event, or something the author built or learned, or when a draft sounds like AI, a press release, or engagement bait.
---

# Writing LinkedIn Posts

## Overview

A good post reads like the person who built the thing explaining it to a smart friend. It opens on a concrete fact, tells one real story (the hard part, the finding, the mistake) and gets out. Every claim can be checked.

**Before writing, read `voice.md`.** It holds the author's personal rules, and it overrides this file.

## Gather facts first

Pull numbers from the source, not from memory: the repo README, `git log`, `gh repo view --json stargazerCount`, release notes, the live URL. If a fact can't be verified, leave it out or tell the author it needs checking. Don't estimate. Credit prior work by name when the project builds on it.

## The shape

The post is these parts, in this order:

1. **Hook: two short lines.** LinkedIn cuts off at about 200 characters with "...more". Line 1 is a concrete, surprising fact or tension. Line 2 turns it. Use no setup, no "I'm excited", no question.
2. **Context: one short paragraph.** The real problem, in first person, with specific nouns.
3. **What it is: plain sentences.** What it does, with the real numbers and names.
4. **The interesting part.** One hard problem, finding, or mistake, told as a story. An honest retraction beats a clean win.
5. **Optional `→` list.** 3 to 5 facts, one line each. Don't use `•`, `-`, or emoji bullets.
6. **Close: one dry line.** Then "Repo in the comments." or "Link in the comments."
7. **The separator line `──────── first comment ────────`**, then the links.
8. **Posting notes in parentheses** after the links, such as which visual to attach or what to deploy first.

Short paragraphs, one blank line between them. The body stays under 3000 characters (LinkedIn's hard limit), and 1200 to 2000 is the sweet spot.

## Quick reference

| Do | Instead of |
|---|---|
| Links in the first comment | Links in the body (LinkedIn buries outbound links) |
| No hashtags, or 2 to 3 at the very end if asked | A hashtag wall |
| "I built", "I found", "I got this wrong" | "Thrilled to announce", "Excited to share" |
| Numbers with units: "26 MB", "0.1s", "16 stars" | "blazing fast", "lightweight", "robust" |
| Commas and periods | Em dashes, semicolon-chained accomplishments |
| Ending on a fact or a dry line | "Thoughts?", "Agree?", "Let that sink in." |
| Naming who helped | Implying solo work on a team project |

## Output

Give plain text with no markdown, no blockquote, and no code fence, so it pastes straight into LinkedIn. If a drafts folder exists, save the post there as `NN-slug.txt`.

Then run the checker and fix everything it reports:

```bash
python3 check.py path/to/post.txt
```

## Series

For several posts about related work, write one light anchor post (the hook is the batch itself) and then one deep dive per project, a few days apart. Open with the most visual project and alternate heavy with light. Skip projects with nothing to link or nothing to say.

## Common mistakes

- **Inflating credit.** If the community cracked the protocol, say so and say what *you* added.
- **Guessed numbers.** Star counts, user counts and benchmarks all come from a source.
- **The hook is a summary.** "I built X, a tool for Y" is a description, not a hook. Lead with the strangest true fact.
- **Explaining the joke.** Understatement only works when nobody points at it.
- **Naming private people** (partners, friends, clients) without asking the author first.
