import os
import json
from pathlib import Path

def get_chrome_extensions():
    chrome_path = Path(os.getenv("LOCALAPPDATA")) / "Google/Chrome/User Data/Default/Extensions"
    if not chrome_path.exists():
        return None

    extensions = []
    for ext_id in chrome_path.iterdir():
        if ext_id.is_dir():
            version_dirs = list(ext_id.iterdir())
            if version_dirs:
                manifest = version_dirs[-1] / "manifest.json"
                if manifest.exists():
                    try:
                        with open(manifest, "r", encoding="utf-8") as mf:
                            data = json.load(mf)
                        extensions.append({
                            "extension_id": ext_id.name,
                            "name": data.get("name", "Unknown"),
                            "version": data.get("version", "Unknown"),
                            "permissions": data.get("permissions", []),
                        })
                    except:
                        pass
    return extensions

def risk_score(permissions):
    if any(p in permissions for p in ["tabs", "webRequest", "<all_urls>"]):
        return "HIGH"
    if any(p in permissions for p in ["clipboardRead", "clipboardWrite", "storage"]):
        return "MEDIUM"
    return "LOW"

def save_results(results):
    with open("browser_extensions.json", "w", encoding="utf-8") as jf:
        json.dump(results, jf, indent=4)

    with open("browser_extensions_report.txt", "w", encoding="utf-8") as tf:
        for r in results:
            tf.write(f"{r['browser']} — {r['name']} ({r['extension_id']})\n")
            tf.write(f"   Version: {r['version']}\n")
            tf.write(f"   Permissions: {', '.join(r['permissions']) or 'None'}\n")
            tf.write(f"   Risk: {r['risk']}\n\n")

def main():
    print("\n=== Browser Extension Auditor v1.0 ===")

    final = []

    chrome_ext = get_chrome_extensions()
    if chrome_ext:
        for ext in chrome_ext:
            final.append({
                "browser": "Chrome",
                **ext,
                "risk": risk_score(ext["permissions"])
            })

    if not final:
        print("No supported browsers found or no extensions installed.")
        return

    save_results(final)
    print("Scan complete! Output saved to:")
    print(" - browser_extensions.json")
    print(" - browser_extensions_report.txt")

if __name__ == "__main__":
    main()