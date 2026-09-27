# linkedin-writing

An agent skill for writing LinkedIn posts that sound like the person who built the thing, not a press release.

It covers the post shape (a two-line hook, one real story, links in the first comment), a personal voice file, and a small checker that catches links in the body, hashtags, emoji, em dashes and hype words.

## Install

```bash
git clone https://github.com/shwetankg07/linkedin-writing ~/Work/linkedin-writing
ln -s ~/Work/linkedin-writing ~/.claude/skills/writing-linkedin-posts
```

Then ask Claude Code to write a post about a repo or project. The skill loads on its own.

## Files

- `SKILL.md`: the post shape and rules
- `voice.md`: my personal voice rules. Fork the repo and replace this file with yours.
- `check.py`: lints a draft, standard library only. Run `python3 check.py post.txt`, or `--selftest`.
- `examples/`: two posts that pass the checker

## License

MIT
