# 2090 Labs

We build **Chronos**: a way to let AI agents change real data without a person reading every change.

Each agent run works on its own branch of the database. You see exactly which rows it changed. Rules you set once decide what merges on its own and what waits for a person. Every merge can be undone.

## What we make

| | |
|---|---|
| [**Chronos DB**](https://github.com/Abhishekxdg/Chronos-DB) | The database engine. A branch per agent run in about 2 microseconds, diffs, merge policies, undo. Speaks the Postgres wire protocol and MCP. Runs on its own, or beside the Postgres, MySQL, MariaDB or MongoDB you already run. |
| [**Chronos Gateway**](https://github.com/Abhishekxdg/chronos-gateway-releases) | A self-hosted service for products with their own agents. An agent sees one customer's rows, holds no database password, and its changes reach your database only through checked, approved merges. |

## Start here

```bash
curl -fsSL https://github.com/Abhishekxdg/Chronos-DB/releases/latest/download/install.sh | sh
```

- [Chronos DB documentation](https://chronosdb-docs.vercel.app/)
- [Gateway setup guide](https://github.com/Abhishekxdg/chronos-gateway-releases/blob/main/GUIDE.md)
- [chronos.2090.tech](https://chronos.2090.tech)

Both are in public beta: try them on a staging copy first.

## Talk to us

- A bug or a question about the engine: [Chronos DB issues](https://github.com/Abhishekxdg/Chronos-DB/issues)
- About the gateway: [Gateway issues](https://github.com/Abhishekxdg/chronos-gateway-releases/issues)
- A security problem: report it privately, as [SECURITY.md](https://github.com/Abhishekxdg/Chronos-DB/blob/main/SECURITY.md) says
