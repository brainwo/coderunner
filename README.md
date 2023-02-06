# CodeRunner

> ⚠ You have been warned: this project enables remote code execution. Use only in trusted environment.

## Language Supported

To add more supported language, kindly contribute either by ticketing an issue or send a pull request. Current supported languages:

| Language   | Alias          | Runtime          |
| ---------- | -------------- | ---------------- |
| python     | py, python     | python3          |
| jaksel     | jaksel         | [jaksel][jaksel] |
| javascript | js, javascript | node             |
| typescript | ts, typescript | node             |
| lua        | lua            | lua              |
| julia      | julia          | julia            |
| duckscript | ds, duckscript | [duck][duck]     |
| wren       | wren           | [wren][wren]     |
| fennel     | fnl, fennel    | [fennel][fennel] |

## Upcoming Support

| Language             | Description                                                         |
| -------------------- | ------------------------------------------------------------------- |
| [mun][mun]           | Currently has no prebuilt binaries or installation option via Cargo |
| [singlang][singlang] | Currently unmaintained and has no binary releases                   |

## Development

Some development dependencies used in this project includes:

-   [poetry](https://github.com/python-poetry/poetry)
-   [just](https://github.com/casey/just)
-   Any editor using [pyright](https://github.com/microsoft/pyright)

Initialize project:

-   Run `just init`

Run project:

-   Create a `secrets.env` file: [(about Discord token)](https://discordpy.readthedocs.io/en/stable/discord.html)

```
DISCORD_TOKEN=<your bot token here>
```

-   Run `just run`

[jaksel]: https://github.com/RioChndr/jaksel-language
[duck]: https://github.com/sagiegurari/duckscript
[mun]: https://github.com/mun-lang/mun
[wren]: https://github.com/wren-lang/wren
[singlang]: https://github.com/frizensami/singlang
[fennel]: https://github.com/bakpakin/Fennel
