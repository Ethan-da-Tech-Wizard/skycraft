# Skycraft Launch Tools

A small launcher and installation-reference workspace for a local Skyrim and SkyCraft setup.

**Status:** Machine-specific launcher prototype  
**Built with:** Python, desktop launcher, JSON manifests

## Reading order

1. Read the root README for project purpose and setup navigation.
2. Follow the entry points below to find the implementation.
3. Use the file guide to locate individual modules, tests, assets, and configuration.
4. Check component licenses before redistributing dependencies or assets.

## Important paths

- [launch-skycraft.py](../launch-skycraft.py) — Start SkyCraft and its Windows Minecraft launcher in the same Proton prefix. Defines `requirements`, `show_error`, `main`.
- [installation-manifest.json](../installation-manifest.json) — Structured installation manifest data; top-level fields: `skycraft_version`, `game`, `prefix`, `files`, `launch_prefix`, `dependencies`, `readiness_report`, `ready_for_user_launch`, `runtime_tested`.

## Structure

| Path | Role |
| --- | --- |
| [docs/](../docs/) | Project documentation, decisions, and reference material (5 tracked entries). |

## Scope

Skyrim, SkyCraft, Minecraft, and SKSE are installed separately under their own terms. The recorded paths describe one workstation and must be adapted before use.

## Maintaining the guide

The file catalog is a source-inspection snapshot, not proof that every runtime path works. Update it when moving files or changing module responsibilities. The 2026-10-12 documentation review did not run every application, deploy services, or validate all historical performance claims.
