<a href="https://2090.tech"><img src="https://raw.githubusercontent.com/2090-labs/.github/main/profile/assets/hero.svg" width="100%" alt="2090 Labs. Let AI agents change real data. Keep the last word. A branch for every agent run, rules that decide what merges, an undo for every merge."></a>

<div align="center">

[**Chronos DB**](https://github.com/2090-labs/Chronos-DB) &nbsp;·&nbsp;
[**Chronos Gateway**](https://github.com/2090-labs/chronos-gateway-releases) &nbsp;·&nbsp;
[**Docs**](https://chronosdb-docs.vercel.app/) &nbsp;·&nbsp;
[**Benchmarks**](https://github.com/2090-labs/Chronos-DB/blob/main/BENCHMARKS.md) &nbsp;·&nbsp;
[**chronos.2090.tech**](https://chronos.2090.tech)

[![Chronos DB](https://img.shields.io/github/v/release/2090-labs/Chronos-DB?label=Chronos%20DB&color=c8ff2e&style=flat-square&labelColor=050505)](https://github.com/2090-labs/Chronos-DB/releases/latest)
[![Chronos Gateway](https://img.shields.io/github/v/release/2090-labs/chronos-gateway-releases?label=Chronos%20Gateway&color=c8ff2e&style=flat-square&labelColor=050505)](https://github.com/2090-labs/chronos-gateway-releases/releases/latest)
![status](https://img.shields.io/badge/status-public%20beta-2c2c2c?style=flat-square&labelColor=050505)
![works beside](https://img.shields.io/badge/beside-Postgres%20%C2%B7%20MySQL%20%C2%B7%20MariaDB%20%C2%B7%20MongoDB-2c2c2c?style=flat-square&labelColor=050505)

</div>

<br>

An AI agent that can only read is a search box. One that can write is useful, and that is where teams stop: nobody wants to hand a model the production password and hope.

**We build Chronos so an agent can write, and you still decide what lands.** Each run works on its own branch of the database. You see every row it changed. Rules you set once let the small, safe changes merge by themselves and hold the rest for a person. And when something wrong does land, you put that one merge back.

<br>

<img src="https://raw.githubusercontent.com/2090-labs/.github/main/profile/assets/loop.svg" width="100%" alt="The life of an agent run: fork a world from main in about 2 microseconds, work in plain SQL that no one else sees, diff every changed row, check your merge policy, then merge into your database in one checked transaction. A merge outside the rules is held for a person. A merge can be undone for 30 days.">

<br>

## What we make

<table>
<tr>
<td width="50%" valign="top">
<a href="https://github.com/2090-labs/Chronos-DB"><img src="https://raw.githubusercontent.com/2090-labs/.github/main/profile/assets/card-db.svg" width="100%" alt="Chronos DB, the engine: a branch of the whole database for every agent run. Fork in about 2 microseconds, diffs, merge policies, undo, the Postgres wire protocol and MCP."></a>

Run it on its own, or beside the Postgres, MySQL, MariaDB or MongoDB you already have. `psql`, your drivers and your ORM connect as they do to Postgres.

[Quickstart](https://chronosdb-docs.vercel.app/quickstart) · [Concepts](https://chronosdb-docs.vercel.app/concepts) · [Releases](https://github.com/2090-labs/Chronos-DB/releases)
</td>
<td width="50%" valign="top">
<a href="https://github.com/2090-labs/chronos-gateway-releases"><img src="https://raw.githubusercontent.com/2090-labs/.github/main/profile/assets/card-gateway.svg" width="100%" alt="Chronos Gateway, the self-hosted service: for products whose own agents change customer data. One customer's rows per run, the agent holds no database password, approve in the console or your own UI."></a>

Self-hosted, in your network. Your app keeps talking to its database as it does today; the gateway sits beside it, never in front of it.

[Setup guide](https://github.com/2090-labs/chronos-gateway-releases/blob/main/GUIDE.md) · [Docs](https://chronos.2090.tech/docs) · [Releases](https://github.com/2090-labs/chronos-gateway-releases/releases)
</td>
</tr>
</table>

## One run, start to finish

<img src="https://raw.githubusercontent.com/2090-labs/.github/main/profile/assets/terminal.svg" width="100%" alt="A psql session. The agent creates a world, updates 84 leads and deletes 11, then asks to merge. The merge is held for review because the policy allows no deletes. A person reads the diff and approves, and the change is written to the database in one checked transaction.">

<img src="https://raw.githubusercontent.com/2090-labs/.github/main/profile/assets/stats.svg" width="100%" alt="About 2 microseconds to fork a world at any size. Works beside 4 databases. 30 days to undo a merge by its id. 31 MCP tools for an agent.">

## Try it in a minute

```bash
curl -fsSL https://github.com/2090-labs/Chronos-DB/releases/latest/download/install.sh | sh
chronos serve mydb                                       # Postgres protocol on 127.0.0.1:5433
claude mcp add chronos -- chronos mcp /path/to/mydb      # hand it to an agent
```

Linux and macOS. No telemetry. The script checks the build against the release's SHA-256 sums and never runs as root.

<details>
<summary><b>Already run a database? Put Chronos beside it</b></summary>

<br>

```bash
export CHRONOS_SOURCE_URL='postgres://agent_writer:...@staging-db:5432/crm?sslmode=verify-full'
chronos attach ./crm --tables public.leads,public.accounts
chronos serve ./crm
```

Agents work on a copy of those tables. Each approved merge is written to your database first, in one transaction, every row compared with what the agent saw. Guides: [Postgres](https://chronosdb-docs.vercel.app/guides/attach-postgres) · [MySQL and MariaDB](https://chronosdb-docs.vercel.app/guides/attach-mysql) · [MongoDB](https://chronosdb-docs.vercel.app/guides/attach-mongodb)

</details>

<details>
<summary><b>Where it stands, plainly</b></summary>

<br>

Both products are in **public beta**. Try them on a staging copy first. Chronos is not Postgres: it runs much of Postgres 16's SQL, not all of it. We publish the benchmarks we lose beside the ones we win, and what the engine does and does not guarantee.

[Where it stands](https://github.com/2090-labs/Chronos-DB#where-it-stands) · [Benchmarks, losses first](https://github.com/2090-labs/Chronos-DB/blob/main/BENCHMARKS.md#where-chronos-db-loses) · [What it guarantees](https://chronosdb-docs.vercel.app/guarantees)

</details>

## Talk to us

| | |
|---|---|
| A bug or a question about the engine | [Chronos DB issues](https://github.com/2090-labs/Chronos-DB/issues) · [Discussions](https://github.com/2090-labs/Chronos-DB/discussions) |
| About the gateway | [Gateway issues](https://github.com/2090-labs/chronos-gateway-releases/issues) |
| A security problem | Privately, as [SECURITY.md](https://github.com/2090-labs/Chronos-DB/blob/main/SECURITY.md) says |
| The company | [2090.tech](https://2090.tech) |

<br>

<a href="https://2090.tech"><img src="https://raw.githubusercontent.com/2090-labs/.github/main/profile/assets/footer.svg" width="100%" alt="2090 Labs, 2090.tech"></a>
