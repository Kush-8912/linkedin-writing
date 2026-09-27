# Contributing

Pull requests are welcome, especially ones that come from using the skill on a real post.

## Good first contributions

- The checker missed a hype word or phrase your draft used. Add it to `HYPE` in `check.py`.
- The checker flagged something that was fine. Fix the rule, and add a case to `selftest()` that would have caught it.
- A step in the README didn't work on your machine.

Issues labeled [good first issue](https://github.com/shwetankg07/linkedin-writing/labels/good%20first%20issue) are small and scoped.

## Before opening a PR

```bash
python3 check.py --selftest
python3 check.py examples/*.txt
```

Both should finish with no errors. `check.py` uses only the Python standard library, so please keep it that way.

`voice.md` holds my personal rules. To change how the skill writes for everyone, edit `SKILL.md`. If you want your own voice, fork the repo and replace `voice.md`.
