# Skycraft Launch Tools

A small launcher and installation-reference workspace for a local Skyrim and SkyCraft setup.

**Status:** Machine-specific launcher prototype  
**Built with:** Python, desktop launcher, JSON manifests

[Project guide](docs/PROJECT_GUIDE.md) · [Every file explained](docs/FILE_GUIDE.md) · [Licenses and dependencies](docs/LICENSE_REVIEW.md)

## Start here

- [launch-skycraft.py](launch-skycraft.py) — Start SkyCraft and its Windows Minecraft launcher in the same Proton prefix. Defines `requirements`, `show_error`, `main`.
- [installation-manifest.json](installation-manifest.json) — Structured installation manifest data; top-level fields: `skycraft_version`, `game`, `prefix`, `files`, `launch_prefix`, `dependencies`, `readiness_report`, `ready_for_user_launch`, `runtime_tested`.

## Repository layout

| Path | Role |
| --- | --- |

## Scope and current limits

Skyrim, SkyCraft, Minecraft, and SKSE are installed separately under their own terms. The recorded paths describe one workstation and must be adapted before use.

## License

Original project code retains **MIT** terms in [LICENSE](LICENSE). Third-party libraries, media, data, models, and tools retain their own terms. See the [license review](docs/LICENSE_REVIEW.md) and [dependency inventory](docs/DEPENDENCIES.csv).
