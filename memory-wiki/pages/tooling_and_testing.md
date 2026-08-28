# Tooling and Testing Architecture

> **Last Updated:** 2026-08-27

This page details the standard tooling and testing workflows for the J.O.S.H.U.A. repository.

## The Unified Task Runner (`joshua.ps1`)

To streamline Operator and Agent experiences, the repository utilizes a unified PowerShell Task Runner CLI located at the repository root: `joshua.ps1`. This abstracts away the complexity of managing individual `.ps1` or Python scripts for operations.

### Core Commands
- `.\joshua.ps1 init <dir>`: Initializes a target directory as a fully functional, air-gapped Sovereign Node (creating the database pools, injecting MCP servers, and dropping `mcp_config.json`).
- `.\joshua.ps1 install`: Sets up host machine prerequisites.
- `.\joshua.ps1 ingest [dir]`: Scans the target directory (defaulting to `./docs` if omitted) and semantically chunks all markdown files, inserting them into the local LanceDB pool using the Nomic embedding model via Ollama.
- `.\joshua.ps1 test`: Discovers and executes the automated test suite using `pytest`.

## The Testing Framework (TDD Mandate)

All Python scripts within the repository are strictly bound by the Test-Driven Development (TDD) mandate.

- **Framework:** `pytest` is the authoritative testing harness.
- **Location:** All unit tests are stored in the `tests/` directory at the repository root.
- **Mocking Strategy:** Scripts that interact with the local filesystem or LanceDB database (e.g., `lancedb_mcp.py`) must use the standard `unittest.mock` library (`patch`, `MagicMock`) to simulate state (e.g., empty databases, missing tables) and ensure logic branches and telemetry payloads are verified without mutating the active memory pool.
