# Browser Extension Auditor

Lightweight local tool to enumerate installed browser extensions (Chrome/Chromium family) and produce a simple risk assessment based on extension permissions. Designed for security analysts, incident responders, and developers who need a quick snapshot of browser extension risk on a Windows workstation.

> *Privacy-first:* the tool runs locally, reads only browser extension manifests, and writes results to local files. It does *not* transmit data externally.

---

## Badges

![Python](https://img.shields.io/badge/Python-3.8%2B-blue)
![Status](https://img.shields.io/badge/Status-Prototype-yellowgreen)
![Platform](https://img.shields.io/badge/Platform-Windows-lightgrey)
![License](https://img.shields.io/badge/License-MIT-yellow)

---

## Quick summary

- Detects Chrome/Chromium-based browser extensions by reading manifest files.
- Extracts extension name, ID, version, and declared permissions.
- Assigns a simple risk tier (LOW / MEDIUM / HIGH) based on sensitive permissions.
- Produces two outputs:
  - browser_extensions.json — machine-readable JSON.
  - browser_extensions_report.txt — human-readable report.

---

## Requirements

- Python 3.8 or later
- Runs on Windows (reads Chrome path from %LOCALAPPDATA%). Works for Chromium derivatives stored under the same directory structure.

Optional (recommended):
- Run with a user account that has read access to the browser profile directories.

---

## Installation

1. Clone the repo to your machine:

git clone https://github.com/<your-username>/browser-extension-auditor.git
cd browser-extension-auditor

2.	(Optional) Create and activate a virtual environment:

3.	python -m venv .venv
# Windows
.venv\Scripts\activate

3.	Run the auditor:
python browser_extension_auditor.py
Usage
	1.	Execute browser_extension_auditor.py from the project folder.
	2.	The script scans the default Chrome/Chromium user profile extension folder and prints progress.
	3.	On completion it writes:
	•	browser_extensions.json — a JSON array of detected extensions with fields: browser, extension_id, name, version, permissions, risk.
	•	browser_extensions_report.txt — formatted human-readable report.

⸻

Risk scoring (v1.0)
	•	HIGH — extensions that request powerful permissions such as tabs, webRequest, webRequestBlocking, or <all_urls>.
	•	MEDIUM — extensions that request clipboard access, broad storage, or other moderately risky permissions.
	•	LOW — extensions with minimal or no sensitive permissions.

This scoring is intentionally conservative and heuristic — audits should be followed by manual review.

⸻

Limitations
	•	v1.0 focuses on Chrome / Chromium-based browsers that store extensions under:
  %LOCALAPPDATA%\Google\Chrome\User Data\Default\Extensions

  EXAMPLE OUTPUT:

  [
  {
    "browser": "Chrome",
    "extension_id": "abcdefg123456",
    "name": "Example Extension",
    "version": "1.2.3",
    "permissions": ["storage", "tabs", "https:///"],
    "risk": "HIGH"
  }
]


Contributing

Contributions welcome. Open an issue to propose features or submit a pull request. Keep changes well documented and include tests for new functionality.


License

MIT License — see LICENSE file.
