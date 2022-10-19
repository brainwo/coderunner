# CodeRunner

> ⚠ You have been warned: this project enables remote code execution. Use only in trusted environment.

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
