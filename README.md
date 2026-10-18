# City template

A 3D night city where every item is a building and every group is a district. Click a district to fly in, click a building to open its panel. Phones get the city on top and a large-print list underneath.

No build step and no dependencies beyond a browser: `index.html` loads three.js from a CDN.

**Start your own city:** click **Use this template** on GitHub, then follow [CONTRIBUTING.md](CONTRIBUTING.md). Using Claude Code? It picks up [CLAUDE.md](CLAUDE.md) automatically.

## Files

| File | What it is |
|---|---|
| `index.html` | The whole city. You normally never edit it. |
| `config.json` | Title, colours, where the data comes from, how often to refresh. |
| `data.json` | Sample data: districts, buildings, headline numbers. Replace with yours. |
| `server.py` | Optional tiny server (Python 3, no packages). Serves the files and `/api/data`. |

## Run it

```
python3 server.py
```
then open http://localhost:8095. (Opening `index.html` straight from disk will not work; browsers block loading the JSON files that way.)

## Your data

`config.json` → `dataUrl` points at any JSON with this shape (see `data.json` for a full example):

```json
{
  "updated": "any text",
  "summary": [ { "label": "Revenue", "value": "$48,200", "tone": "good" } ],
  "districts": [ { "id": "sales", "name": "Sales", "color": "#f5c542", "line": "one line under the sign" } ],
  "buildings": [ {
    "id": "acme", "district": "sales", "name": "Acme Corp",
    "style": "tower | spire | dome | twin | block", "height": 20, "lit": 0.8,
    "value": "+$12,400", "tone": "good | bad | (blank)", "status": "Renewal signed",
    "gauges": [ { "label": "Quota", "share": 0.82, "color": "#3fc56b" } ],
    "live":   [ { "text": "Upsell call Thursday", "value": "+$3,000", "tone": "good" } ],
    "stats":  [ ["Owner", "Sam"], ["Stage", "Customer"] ],
    "list":   [ ["Oct 14", "Renewal signed", "+$9,400", "good"] ],
    "history": [2, 4, 3, 6, 8],
    "about": "Free text shown in the panel."
  } ]
}
```

Everything except `id`, `district` and `name` is optional. Buildings lay themselves out (four to a row), districts arrange themselves in a grid. `live` items show in gold on the building's name card and count as "open" on the district sign. Two or more `gauges` show as thin bars on the card.

Point `dataUrl` at `/api/data` and edit `get_data()` in `server.py` to build the data from a database or another API. The page refetches every `refreshSeconds`, pauses while the tab is hidden, and only rebuilds the 3D city when buildings or districts are added, removed or restyled; changed numbers just repaint the cards.

## Put it online

* **Static host** (Netlify, Vercel, GitHub Pages, Cloudflare Pages): upload `index.html`, `config.json` and `data.json`, or set `dataUrl` to a JSON URL served elsewhere (it must allow cross-origin requests).
* **A server** (Railway, Render, Fly, any VPS): run `python3 server.py`; it listens on the `PORT` the host provides.

Keep secrets out of `data.json` and `config.json`: both are downloadable by anyone who can open the page.

## License

MIT. See [LICENSE](LICENSE).
