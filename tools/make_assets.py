#!/usr/bin/env python3
"""Draws the organization profile's pictures (profile/assets/*.svg) in the Signal look of 2090.tech:
the void, one lime, hairlines, a signal bar, the year in a dot matrix. Run: python3 tools/make_assets.py"""
import os

OUT = os.path.join(os.path.dirname(__file__), "..", "profile", "assets")
VOID, PANEL, LINE, LIME, CHALK, MUTE, DIM = "#050505", "#0b0b0b", "#2c2c2c", "#c8ff2e", "#f2f2ee", "#9a9a94", "#5c5c58"
MONO = "ui-monospace,SFMono-Regular,'SF Mono',Menlo,Consolas,'Liberation Mono',monospace"
SANS = "-apple-system,BlinkMacSystemFont,'Segoe UI',Helvetica,Arial,sans-serif"
STILL = "@media (prefers-reduced-motion:reduce){*{animation:none!important}}"


def esc(s):
    return s.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")


def svg(w, h, title, body, css=""):
    return (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w} {h}" width="{w}" height="{h}" role="img" '
            f'aria-label="{esc(title)}"><title>{esc(title)}</title><style>'
            f'.m{{font-family:{MONO}}}.s{{font-family:{SANS}}}{css}{STILL}</style>'
            f'<rect x=".5" y=".5" width="{w - 1}" height="{h - 1}" rx="14" fill="{VOID}" stroke="{LINE}"/>{body}</svg>\n')


def write(name, text):
    os.makedirs(OUT, exist_ok=True)
    with open(os.path.join(OUT, name), "w") as f:
        f.write(text)


DIGITS = {
    "2": ["01110", "10001", "00001", "00010", "00100", "01000", "11111"],
    "0": ["01110", "10001", "10001", "10001", "10001", "10001", "01110"],
    "9": ["01110", "10001", "10001", "01111", "00001", "00010", "01100"],
}


def dots(text, x, y, pitch, r, cls="d"):
    """A word in a 5x7 dot matrix: lit dots in the lime, the rest as faint sockets."""
    out, i = [], 0
    for ch in text:
        for row, bits in enumerate(DIGITS[ch]):
            for col, b in enumerate(bits):
                cx, cy = x + col * pitch, y + row * pitch
                if b == "1":
                    out.append(f'<circle class="{cls}" style="animation-delay:{i * 12}ms" cx="{cx}" cy="{cy}" r="{r}" fill="{LIME}"/>')
                    i += 1
                else:
                    out.append(f'<circle cx="{cx}" cy="{cy}" r="{r * .45:.2f}" fill="{LINE}"/>')
        x += 6 * pitch
    return "".join(out)


def hero():
    w, h = 1200, 440
    n, x0, x1 = 64, 64, 1136
    cw = (x1 - x0) / n
    cells = []
    for i in range(n):
        cls = "c on" if i == 0 else "c nx" if i == 1 else "c"
        cells.append(f'<rect class="{cls}" style="animation-delay:{i * 90}ms" x="{x0 + i * cw:.1f}" y="352" width="{cw - 4:.1f}" height="26" rx="1.5"/>')
    css = (f".c{{fill:{LINE};animation:scan 5.76s linear infinite}}.on{{fill:{LIME}}}.nx{{fill:{LIME};fill-opacity:.4}}"
           f"@keyframes scan{{0%{{fill:{LIME};fill-opacity:1}}4%{{fill:{LIME};fill-opacity:.4}}8%,100%{{fill:{LINE};fill-opacity:1}}}}"
           ".d{animation:pop .5s ease-out backwards}@keyframes pop{from{opacity:0}to{opacity:1}}"
           ".up{animation:up .7s ease-out backwards}@keyframes up{from{opacity:0;transform:translateY(8px)}to{opacity:1;transform:none}}")
    body = (
        f'<text class="m" x="64" y="70" font-size="13" letter-spacing="2.4" fill="{MUTE}">2090/LABS</text>'
        f'<text class="m" x="1136" y="70" font-size="13" letter-spacing="2.4" fill="{MUTE}" text-anchor="end">AGENTS THAT WRITE · DATA YOU TRUST</text>'
        f'<line x1="64" y1="92" x2="1136" y2="92" stroke="{LINE}"/>'
        + dots("2090", 64, 140, 15, 5.4)
        + f'<text class="s up" style="animation-delay:.5s" x="436" y="232" font-size="92" font-weight="600" letter-spacing="-3" fill="{CHALK}">Labs</text>'
        f'<text class="s up" style="animation-delay:.7s" x="680" y="170" font-size="30" font-weight="600" letter-spacing="-.5" fill="{CHALK}">Let AI agents change real data.</text>'
        f'<text class="s up" style="animation-delay:.8s" x="680" y="208" font-size="30" font-weight="600" letter-spacing="-.5" fill="{LIME}">Keep the last word.</text>'
        f'<text class="s up" style="animation-delay:.95s" x="680" y="246" font-size="16" fill="{MUTE}">A branch for every agent run. Rules that decide what</text>'
        f'<text class="s up" style="animation-delay:.95s" x="680" y="270" font-size="16" fill="{MUTE}">merges. An undo for every merge.</text>'
        f'<text class="m" x="64" y="336" font-size="12" letter-spacing="2" fill="{DIM}">NOW</text>'
        f'<text class="m" x="1136" y="336" font-size="12" letter-spacing="2" fill="{DIM}" text-anchor="end">2090</text>'
        + "".join(cells)
        + f'<text class="m" x="64" y="406" font-size="12" letter-spacing="2" fill="{DIM}">WE BUILD CHRONOS</text>'
        f'<text class="m" x="1136" y="406" font-size="12" letter-spacing="2" fill="{DIM}" text-anchor="end">2090.TECH</text>')
    write("hero.svg", svg(w, h, "2090 Labs. Let AI agents change real data. Keep the last word. A branch for every agent run, rules that decide what merges, an undo for every merge.", body, css))


def loop():
    w, h = 1200, 400
    world = "M 210 268 C 270 268 270 150 330 150 L 810 150 C 870 150 870 268 930 268"
    css = (f".run{{offset-path:path('{world}');animation:run 7s cubic-bezier(.45,0,.55,1) infinite}}"
           "@keyframes run{0%{offset-distance:0%;opacity:0}6%{opacity:1}94%{opacity:1}100%{offset-distance:100%;opacity:0}}"
           ".dash{stroke-dasharray:5 7;animation:dash 1.6s linear infinite}@keyframes dash{to{stroke-dashoffset:-24}}"
           ".pulse{animation:pulse 7s ease-in-out infinite}@keyframes pulse{0%,86%{r:7}93%{r:12}100%{r:7}}")

    def node(x, y, label, sub, above=True, color=LIME):
        ty = y - 40 if above else y + 34
        return (f'<circle cx="{x}" cy="{y}" r="7" fill="{VOID}" stroke="{color}" stroke-width="2"/>'
                f'<text class="m" x="{x}" y="{ty}" font-size="13" letter-spacing="2" fill="{CHALK}" text-anchor="middle">{label}</text>'
                f'<text class="s" x="{x}" y="{ty + 19}" font-size="13" fill="{MUTE}" text-anchor="middle">{esc(sub)}</text>')

    body = (
        f'<text class="m" x="64" y="62" font-size="13" letter-spacing="2.4" fill="{MUTE}">THE LIFE OF AN AGENT RUN</text>'
        # main: the database everyone else keeps using
        f'<line x1="64" y1="268" x2="1136" y2="268" stroke="{CHALK}" stroke-width="2"/>'
        f'<text class="m" x="64" y="296" font-size="12" letter-spacing="2" fill="{DIM}">MAIN</text>'
        f'<text class="m" x="1136" y="296" font-size="12" letter-spacing="2" fill="{DIM}" text-anchor="end">YOUR DATABASE</text>'
        # the world: leaves main, works, comes back
        f'<path d="{world}" fill="none" stroke="{LIME}" stroke-width="2"/>'
        # held for a person
        f'<path class="dash" d="M 730 150 C 730 96 760 84 812 84" fill="none" stroke="{MUTE}" stroke-width="1.5"/>'
        f'<rect x="816" y="62" width="320" height="44" rx="6" fill="{PANEL}" stroke="{LINE}"/>'
        f'<text class="m" x="832" y="81" font-size="12" letter-spacing="2" fill="{CHALK}">HELD</text>'
        f'<text class="s" x="832" y="98" font-size="13" fill="{MUTE}">outside the rules: a person approves or drops it</text>'
        # undo
        f'<path class="dash" d="M 930 268 C 930 342 770 342 770 276" fill="none" stroke="{MUTE}" stroke-width="1.5"/>'
        f'<path d="M 764 286 L 770 274 L 776 286" fill="none" stroke="{MUTE}" stroke-width="1.5"/>'
        f'<text class="m" x="850" y="352" font-size="12" letter-spacing="2" fill="{CHALK}" text-anchor="middle">UNDO</text>'
        f'<text class="s" x="850" y="371" font-size="13" fill="{MUTE}" text-anchor="middle">put a merge back, for 30 days</text>'
        + node(210, 268, "FORK", "a world, in about 2 µs", above=False)
        + node(410, 150, "WORK", "plain SQL, seen by no one else")
        + node(570, 150, "DIFF", "every changed row")
        + node(730, 150, "RULES", "your merge policy", above=False)
        + f'<circle class="pulse" cx="930" cy="268" r="7" fill="{LIME}"/>'
        f'<text class="m" x="1010" y="230" font-size="13" letter-spacing="2" fill="{CHALK}" text-anchor="middle">MERGE</text>'
        f'<text class="s" x="1010" y="249" font-size="13" fill="{MUTE}" text-anchor="middle">one checked transaction</text>'
        f'<circle class="run" r="5" fill="{LIME}"/>')
    write("loop.svg", svg(w, h, "The life of an agent run: fork a world from main in about 2 microseconds, work in plain SQL that no one else sees, diff every changed row, check your merge policy, then merge into your database in one checked transaction. A merge outside the rules is held for a person. A merge can be undone for 30 days.", body, css))


def terminal():
    w, h = 1200, 448
    lines = [
        ("c", "-- the agent, on its own branch of the whole database"),
        ("p", "bot=>", "create world run_42 with (task = 'clean up stale leads');"),
        ("p", "bot=>", "update leads set status = 'stale' where last_contact < now() - interval '1 year';"),
        ("o", "UPDATE 84"),
        ("p", "bot=>", "delete from leads where email is null;"),
        ("o", "DELETE 11"),
        ("p", "bot=>", "merge world run_42;"),
        ("h", "-- held for review: it deletes 11 rows, and the policy says max_deletes = 0"),
        ("c", "-- you: look at exactly what changed, then decide"),
        ("p", "you=>", "diff world run_42;"),
        ("p", "you=>", "merge world run_42;"),
        ("g", "-- approved: written to your database in one checked transaction"),
    ]
    css = ".l{animation:show 20s linear infinite backwards}@keyframes show{0%{opacity:0}1.5%,88%{opacity:1}92%,100%{opacity:0}}" \
          f".cur{{animation:blink 1.1s steps(1) infinite}}@keyframes blink{{50%{{opacity:0}}}}"
    rows, y = [], 96
    for i, ln in enumerate(lines):
        d = f'style="animation-delay:{i * 0.85:.2f}s"'
        if ln[0] == "p":
            who = LIME if ln[1].startswith("bot") else CHALK
            t = (f'<tspan fill="{who}">{esc(ln[1])}</tspan><tspan fill="{CHALK}"> {esc(ln[2])}</tspan>')
        else:
            color = {"c": DIM, "o": MUTE, "h": "#ffb454", "g": LIME}[ln[0]]
            t = f'<tspan fill="{color}">{esc(ln[1])}</tspan>'
        rows.append(f'<text class="m l" {d} x="64" y="{y}" font-size="15.5" xml:space="preserve">{t}</text>')
        y += 27
    body = (
        f'<path d="M .5 52 H {w - .5}" stroke="{LINE}"/>'
        f'<circle cx="34" cy="27" r="5.5" fill="{LINE}"/><circle cx="54" cy="27" r="5.5" fill="{LINE}"/><circle cx="74" cy="27" r="5.5" fill="{LINE}"/>'
        f'<text class="m" x="{w / 2}" y="32" font-size="12.5" letter-spacing="1.5" fill="{MUTE}" text-anchor="middle">psql postgres://127.0.0.1:5433/main</text>'
        + "".join(rows)
        + f'<rect class="cur" x="64" y="{y - 14}" width="9" height="18" fill="{LIME}"/>')
    write("terminal.svg", svg(w, h, "A psql session. The agent creates a world, updates 84 leads and deletes 11, then asks to merge. The merge is held for review because the policy allows no deletes. A person reads the diff and approves, and the change is written to the database in one checked transaction.", body, css))


def card(name, kicker, title, lead, points, link, label):
    w, h = 590, 330
    pts = "".join(
        f'<rect x="40" y="{166 + i * 30}" width="8" height="8" fill="{LIME}" fill-opacity="{1 if i == 0 else .55}"/>'
        f'<text class="s" x="62" y="{175 + i * 30}" font-size="15" fill="{CHALK}">{esc(p)}</text>' for i, p in enumerate(points))
    body = (
        f'<text class="m" x="40" y="58" font-size="12.5" letter-spacing="2.4" fill="{MUTE}">{kicker}</text>'
        f'<text class="s" x="40" y="104" font-size="34" font-weight="600" letter-spacing="-.8" fill="{CHALK}">{esc(title)}</text>'
        f'<text class="s" x="40" y="134" font-size="15.5" fill="{MUTE}">{esc(lead)}</text>'
        + pts
        + f'<line x1="40" y1="282" x2="550" y2="282" stroke="{LINE}"/>'
        f'<text class="m" x="40" y="306" font-size="13" fill="{LIME}">{esc(link)}</text>'
        f'<text class="m" x="550" y="306" font-size="13" fill="{LIME}" text-anchor="end">→</text>')
    write(name, svg(w, h, label, body))


def stats():
    w, h = 1200, 170
    items = [("~2 µs", "to fork a world, at any size"), ("4", "databases it works beside"),
             ("30 days", "to undo a merge by its id"), ("31", "MCP tools for an agent")]
    body, cw = "", (w - 128) / 4
    for i, (big, small) in enumerate(items):
        x = 64 + i * cw
        if i:
            body += f'<line x1="{x - 24:.0f}" y1="44" x2="{x - 24:.0f}" y2="126" stroke="{LINE}"/>'
        body += (f'<text class="s" x="{x:.0f}" y="90" font-size="44" font-weight="600" letter-spacing="-1.2" fill="{LIME if i == 0 else CHALK}">{big}</text>'
                 f'<text class="s" x="{x:.0f}" y="120" font-size="14.5" fill="{MUTE}">{small}</text>')
    write("stats.svg", svg(w, h, "About 2 microseconds to fork a world at any size. Works beside 4 databases. 30 days to undo a merge by its id. 31 MCP tools for an agent.", body))


def footer():
    w, h = 1200, 96
    n, x0, x1 = 64, 64, 1136
    cw = (x1 - x0) / n
    cells = "".join(
        f'<rect x="{x0 + i * cw:.1f}" y="30" width="{cw - 4:.1f}" height="10" rx="1" fill="{LIME if i < 1 else LINE}" fill-opacity="{1 if i != 1 else 1}"/>'
        for i in range(n))
    body = (cells
            + f'<text class="m" x="64" y="70" font-size="12" letter-spacing="2" fill="{DIM}">2090/LABS</text>'
            f'<text class="m" x="600" y="70" font-size="12" letter-spacing="2" fill="{DIM}" text-anchor="middle">BUILT FOR THE YEARS BETWEEN NOW AND THEN</text>'
            f'<text class="m" x="1136" y="70" font-size="12" letter-spacing="2" fill="{DIM}" text-anchor="end">2090.TECH</text>')
    write("footer.svg", svg(w, h, "2090 Labs, 2090.tech", body))


hero()
loop()
terminal()
card("card-db.svg", "THE ENGINE", "Chronos DB", "A branch of the whole database for every agent run.",
     ["Fork in about 2 µs, at any size", "Diffs, merge policies, undo", "Postgres wire protocol and MCP"],
     "github.com/2090-labs/Chronos-DB", "Chronos DB, the engine: a branch of the whole database for every agent run. Fork in about 2 microseconds, diffs, merge policies, undo, the Postgres wire protocol and MCP.")
card("card-gateway.svg", "THE SERVICE", "Chronos Gateway", "For products whose own agents change customer data.",
     ["One customer's rows per run", "The agent holds no database password", "Approve in the console or your own UI"],
     "github.com/2090-labs/chronos-gateway-releases", "Chronos Gateway, the self-hosted service: for products whose own agents change customer data. One customer's rows per run, the agent holds no database password, approve in the console or your own UI.")
stats()
footer()
print("wrote", sorted(os.listdir(OUT)))
