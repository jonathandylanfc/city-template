# Building on the city template

## Make your own city

1. On GitHub, click **Use this template → Create a new repository**. You get your own copy to change freely.
2. Clone it, then run `python3 server.py` and open http://localhost:8095.
3. Edit `config.json` (title, colours) and replace `data.json` with your own districts and buildings, or point `dataUrl` at your own data. `README.md` describes the data shape.
4. Working with Claude Code? Open the folder and start `claude`. It reads `CLAUDE.md` automatically, so you can ask for things like "add a building style that looks like a lighthouse" or "load the buildings from our Google Sheet" without explaining the code first.

## Send an improvement back to the shared template

If you build something everyone could use (a new building style, a panel feature, a fix):

1. Keep it generic: no company names, data or keys.
2. Make any new data field optional and document it in `README.md` and `data.json`.
3. Open a pull request against the original template repository with a short description and a screenshot.
