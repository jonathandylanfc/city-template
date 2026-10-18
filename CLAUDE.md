# CLAUDE.md

Guidance for Claude Code (and people) working on this repository.

## What this is

A 3D "night city" dashboard: every item is a building, every group is a district. It is a template: people copy it ("Use this template" on GitHub) and turn it into their own city for their own data. Keep the template generic. Anything specific to one use belongs in that user's copy, not here.

## How it fits together

- `index.html` is the whole app: HTML, CSS and one ES module script. three.js 0.160.0 and its OrbitControls load from jsDelivr through an import map. There is no build step and no package manager. Keep it that way unless the owner asks otherwise.
- `config.json` holds the title, theme colours, `dataUrl`, `refreshSeconds` and panel headings.
- `data.json` is sample data and documents the data shape (also described in `README.md`). The page only ever reads data from `dataUrl`.
- `server.py` is an optional Python 3 standard-library server: it serves the folder and `/api/data`, which returns `get_data()`. It listens on `127.0.0.1:8095`, or on `0.0.0.0:$PORT` when a host sets `PORT`. It refuses to serve `.py` and `.md` files.

Inside `index.html`, in order: settings and data loading, scene setup, `facade()` and `block()` helpers, `makeBuilding()` (the five styles), `drawLabel()` (name cards, canvas sprites), `districtSign()`, `build()` (layout), camera helpers (`fly`, `fitBox`, `viewCamera`, `focus`, `unfocus`), UI (`renderViews`, `panel`, `list`, `tiles`), pointer handling, the render loop (`readable`, `tick`), then `load()` and the refresh timer.

## Data shape (the contract)

Buildings need `id`, `district` and `name`; everything else (`style`, `height`, `lit`, `value`, `tone`, `status`, `gauges`, `live`, `stats`, `list`, `history`, `about`) is optional and must stay optional. Districts need `id` and `name` (`color` and `line` optional). If you add a field, make it optional, document it in `README.md` and add an example to `data.json`. Never rename or remove an existing field: other people's data depends on it.

## Rules

- Escape every piece of data before it goes into HTML with `esc()`. Data can come from anywhere.
- Keep the render loop wrapped in try/catch (three.js stops its loop on an uncaught error).
- The city rebuilds only when its shape changes (districts, building ids, styles, heights, `lit`); number changes only repaint the name cards and signs. Keep that split: full rebuilds cause a visible hitch.
- Dispose of geometries, materials and textures you replace (`dispose()` helper).
- Phones (max-width 700px) get the list under a shorter canvas; check new UI at phone width too.
- No secrets in this repository. `config.json` and `data.json` are public to anyone who can open the page.
- Keep code comments short and plain; match the existing style (dense, one idea per line).

## Common tasks

- New building style: add a branch in `makeBuilding()` returning `{ g, w, d, top }` (`top` is where the name card sits), then mention it in `README.md` and use it in `data.json`.
- New panel section: add it in `panel()`, driven by an optional data field.
- Live data: change `get_data()` in `server.py`, or point `dataUrl` at another JSON endpoint (it must allow cross-origin requests if hosted elsewhere).

## Checking your work

Run `python3 server.py`, open http://localhost:8095, and check: the All view (signs visible, buildings small), each district button, clicking a building (panel opens, camera flies in, Back works), and phone width. The browser console must stay free of errors.
