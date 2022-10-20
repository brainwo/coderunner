# CodeRunner

> ⚠ You have been warned: this project enables remote code execution. Use only in trusted environment.

## Language Supported

To add more supported language, kindly contribute either with ticketing an issue or send a pull request. Current supported languages:

| Language   | Alias          | Runtime          |
| ---------- | -------------- | ---------------- |
| python     | py, python     | python3          |
| jaksel     | jaksel         | [jaksel][jaksel] |
| javascript | js, javascript | node             |
| typescript | ts, typescript | node             |
| lua        | lua            | lua              |
| julia      | julia          | julia            |
| duckscript | ds, duckscript | [duck][duck]     |

## Development

Some development dependecies used in this project are:

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
