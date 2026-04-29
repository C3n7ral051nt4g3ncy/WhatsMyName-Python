#!/usr/bin/env python3
# File name       : whatsmyname.py
# By              : C3n7ral051nt4g3ncy
# Version         : Version 1.3.0
# Support         : Please do not support me, Support this project --> https://github.com/WebBreacher/WhatsMyName

import sys
import time
import argparse
import json
import csv
import requests
from datetime import datetime
from tqdm import tqdm
from concurrent.futures import ThreadPoolExecutor, as_completed

# ── Constants ─────────────────────────────────────────────────────────────────

WMN_DATA_URL = "https://raw.githubusercontent.com/WebBreacher/WhatsMyName/main/wmn-data.json"

HEADERS = {
    "Accept": "text/html, application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
    "Accept-Language": "en-US;q=0.9,en;q=0.8",
    "Accept-Encoding": "gzip, deflate",
    "User-Agent": (
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
        "AppleWebKit/537.36 (KHTML, like Gecko) "
        "Chrome/104.0.0.0 Safari/537.36"
    ),
}

# ── Banner ─────────────────────────────────────────────────────────────────────

def banner():
    print(
        """\033[39m\033[1m
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣀⢀⠀⠀⣰⣿⣿⣿⡆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣿⠃⣾⣿⡄⠹⢿⣿⡿⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣤⣶⣤⣼⣿⣿⣿⣿⣶⣦⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀   ⢀⣴⡶⠀⠘⣿⣿⣿⣿⣿⣿⣿⣿⣟⢿⠇⢀ ⣶⡆⢰⣶⣄⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀  ⢀⣴⡿⠋⠀⠀⠀⠀⢿⣿⣿⣿⣿⣿⣇⢻⣿⣮⣀ ⣘⠻⠀  ⠙⢿⣷⣄⠀⠀⠀⠀⠀
⠀⠀⠀ ⢀⣴⡿⠋⠀⠀⠀⠀⠀⠀⠀⠈⠉⣽⣿⣿⣿⣌⠛⠻⠿⠿⠿⠇⠀⠀⠀⠀⠀⠀ ⠙⢿⣷⣄⠀⠀⠀
⠀⢀⣴⡿⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢿⣿⣿⢿⣿⣿⡖⣰⣶⠂⠀⠀⠀⠀⠀⠀⠀⠀ ⠀ ⠙⢿⣷⣄⠀
⠀⠻⣿⣦⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠸⣿⣿⡀⠈⠙⢠⣿⠏⠀⠀⠀⠀⠀⠀⠀⠀⠀ ⠀ ⢀⣴⣿⠟⠀
⠀⠀ ⠈⠻⣿⣦⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⡇⠀⢀⣿⡟⣰⡄⠀⠀⠀⠀⠀⠀⠀ ⢀⣴⣿⠟⠁⠀⠀
⠀⠀⠀⠀  ⠈⠻⣿⣦⡀⠀⠀⠀⠀⠀⢀⣿⣿⠇⠀⣾⡿⢠⣿⡇⠀⠀⠀⠀⠀⢀⣴⣿⠟⠁⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀   ⠈⠻⣿⣦⠀⠀⠀⢸⣿⣿⠀⣼⣿⠁⠈⠉⠀⠀⠀⠀⢰⣿⠟⠁⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠈⠁⠀⠀⠀⠀⠀⠀⠀⠙⠉⠀⠙⠁⠀⠀⠀⠀⠀⠀⠀⠀⠈⠁⠀
             < WebBreacher >
         \033[32m\033[1m
       ╦ ╦┬ ┬┌─┐┌┬┐┌─┐╔╦╗┬ ┬╔╗╔┌─┐┌┬┐┌─┐
       ║║║├─┤├─┤ │ └─┐║║║└┬┘║║║├─┤│││├┤ 
       ╚╩╝┴ ┴┴ ┴ ┴ └─┘╩ ╩ ┴ ╝╚╝┴ ┴┴ ┴└─┘ Version 1.3.0
        \033[39m\033[1m
       by C3n7ral051nt4g3ncy
       github.com/WebBreacher/WhatsMyName\n\n
      \033[32m\033[1mUsage: python3 whatsmyname.py -h\033[0m\n\n"""
    )


# ── Site checker ───────────────────────────────────────────────────────────────

def check_site(site: dict, username: str) -> dict:
    """
    Check a single site for the username.

    Returns a result dict with keys:
        name, url_check, url_pretty, status ("found" | "not_found" | "error"),
        http_code, error_msg, elapsed_ms

    url_check  – the URL actually fetched (uri_check); kept for debugging.
    url_pretty – the human-facing profile URL (uri_pretty when present,
                 otherwise falls back to uri_check).
    """
    url_check  = site["uri_check"].format(account=username)
    url_pretty = site.get("uri_pretty", site["uri_check"]).format(account=username)
    result = {
        "name":       site["name"],
        "url_check":  url_check,
        "url_pretty": url_pretty,
        "status":     "not_found",
        "http_code":  None,
        "error_msg":  None,
        "elapsed_ms": None,
    }

    try:
        res = requests.get(url_check, headers=HEADERS, timeout=10)
        result["http_code"]  = res.status_code
        result["elapsed_ms"] = int(res.elapsed.total_seconds() * 1000)

        estring_pos = site["e_string"] in res.text
        estring_neg = site["m_string"] in res.text

        if res.status_code == site["e_code"] and estring_pos and not estring_neg:
            result["status"] = "found"

    except requests.exceptions.Timeout:
        result["status"]    = "error"
        result["error_msg"] = "Timeout"
    except requests.exceptions.ConnectionError as exc:
        result["status"]    = "error"
        result["error_msg"] = f"ConnectionError: {exc}"
    except Exception as exc:
        result["status"]    = "error"
        result["error_msg"] = str(exc)

    return result

# ── Scan runner ────────────────────────────────────────────────────────────────

def scan_username(sites: list, username: str, max_workers: int = 20) -> list:
    """
    Concurrently check all sites for *username*.
    Returns a list of result dicts (one per site), sorted by status then name.
    """
    all_results = []

    with ThreadPoolExecutor(max_workers=max_workers) as executor:
        futures = {executor.submit(check_site, site, username): site for site in sites}

        with tqdm(total=len(sites), desc="Checking sites", unit="site") as pbar:
            for future in as_completed(futures):
                try:
                    result = future.result()
                except Exception as exc:
                    site = futures[future]
                    result = {
                        "name":       site["name"],
                        "url_check":  site["uri_check"].format(account=username),
                        "url_pretty": site.get("uri_pretty", site["uri_check"]).format(account=username),
                        "status":     "error",
                        "http_code":  None,
                        "error_msg":  str(exc),
                        "elapsed_ms": None,
                    }

                all_results.append(result)

                if result["status"] == "found":
                    tqdm.write("\033[32m" + "-" * 80)
                    tqdm.write(f"\033[32m[+] \033[1mFound\033[0m\033[32m ✓  {result['name']}\033[0m")
                    tqdm.write(f"\033[32m    {result['url_pretty']}\033[0m")
                    tqdm.write("\033[32m" + "-" * 80)

                pbar.update(1)

    # Sort: found first, then not_found, then errors; alphabetical within each group
    order = {"found": 0, "not_found": 1, "error": 2}
    all_results.sort(key=lambda r: (order[r["status"]], r["name"].lower()))
    return all_results

# ── Output helpers ─────────────────────────────────────────────────────────────

def _timestamp() -> str:
    return datetime.now().strftime("%Y%m%d_%H%M%S")


def save_json_log(username: str, results: list) -> str:
    """Write every site result to a JSON log file."""
    filename = f"wmn_{username}_{_timestamp()}.json"
    payload = {
        "username":   username,
        "scanned_at": datetime.now().isoformat(),
        "total":      len(results),
        "found":      sum(1 for r in results if r["status"] == "found"),
        "not_found":  sum(1 for r in results if r["status"] == "not_found"),
        "errors":     sum(1 for r in results if r["status"] == "error"),
        "results":    results,
    }
    with open(filename, "w", encoding="utf-8") as fh:
        json.dump(payload, fh, indent=2, ensure_ascii=False)
    return filename


def save_csv_log(username: str, results: list) -> str:
    """Write every site result to a CSV file."""
    filename = f"wmn_{username}_{_timestamp()}.csv"
    fieldnames = ["status", "name", "url_pretty", "url_check", "http_code", "elapsed_ms", "error_msg"]
    with open(filename, "w", newline="", encoding="utf-8") as fh:
        writer = csv.DictWriter(fh, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(results)
    return filename


def save_html_report(username: str, results: list) -> str:
    """Generate a colour-coded HTML report covering all results."""
    filename = f"wmn_{username}_{_timestamp()}.html"

    def _row_colour(status: str) -> str:
        return {"found": "#d4edda", "not_found": "#f8f9fa", "error": "#f8d7da"}.get(status, "")

    # ── Found-only quick-reference block ──────────────────────────────────────
    found_results = [r for r in results if r["status"] == "found"]
    found_rows = ""
    for r in found_results:
        found_rows += (
            f'<tr>'
            f'<td>{r["name"]}</td>'
            f'<td><a href="{r["url_pretty"]}" target="_blank">{r["url_pretty"]}</a></td>'
            f'</tr>\n'
        )

    # ── Full results table (found first, then not_found, then errors) ─────────
    all_rows = ""
    for r in results:
        colour = _row_colour(r["status"])
        if r["status"] == "found":
            link = f'<a href="{r["url_pretty"]}" target="_blank">{r["url_pretty"]}</a>'
        else:
            link = r["url_pretty"]
        all_rows += (
            f'<tr style="background:{colour}">'
            f'<td>{r["status"]}</td>'
            f'<td>{r["name"]}</td>'
            f'<td style="word-break:break-all">{link}</td>'
            f'<td>{r["http_code"] or ""}</td>'
            f'<td>{r["elapsed_ms"] or ""}</td>'
            f'<td>{r["error_msg"] or ""}</td>'
            f"</tr>\n"
        )

    found_count = len(found_results)
    error_count = sum(1 for r in results if r["status"] == "error")
    nf_count    = sum(1 for r in results if r["status"] == "not_found")
    scanned_at  = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    # Only render the found section if there are hits
    found_section = ""
    if found_results:
        found_section = f"""
<h2>&#10003; Accounts found ({found_count})</h2>
<table class="found-table">
  <thead><tr><th>Site</th><th>Profile URL</th></tr></thead>
  <tbody>
{found_rows}  </tbody>
</table>
<h2>Full results</h2>"""

    html = f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<title>WhatsMyName — {username}</title>
<style>
  body  {{ font-family: Arial, sans-serif; margin: 2em; }}
  h1, h2 {{ color: #333; }}
  h2  {{ margin-top: 1.8em; }}
  .stats {{ display: flex; gap: 2em; margin-bottom: 1.5em; }}
  .stat  {{ padding: .6em 1.2em; border-radius: 6px; font-weight: bold; }}
  .found     {{ background: #d4edda; color: #155724; }}
  .not_found {{ background: #f8f9fa; color: #6c757d; border: 1px solid #dee2e6; }}
  .error     {{ background: #f8d7da; color: #721c24; }}
  table  {{ width: 100%; border-collapse: collapse; font-size: .9em; margin-bottom: 1em; }}
  th, td {{ border: 1px solid #dee2e6; padding: 6px 10px; text-align: left; }}
  th     {{ background: #e9ecef; position: sticky; top: 0; }}
  .found-table td, .found-table th {{ background: #d4edda; border-color: #b8dac3; }}
  .found-table th {{ color: #155724; }}
  input  {{ margin-bottom: 1em; padding: 6px; width: 300px; font-size: .95em; }}
</style>
</head>
<body>
<h1>WhatsMyName — <em>{username}</em></h1>
<p>Scanned at {scanned_at} &nbsp;|&nbsp; {len(results)} sites checked</p>
<div class="stats">
  <span class="stat found">&#10003; Found: {found_count}</span>
  <span class="stat not_found">— Not found: {nf_count}</span>
  <span class="stat error">&#9888; Errors: {error_count}</span>
</div>
{found_section}
<input type="text" id="filter" placeholder="Filter by site name or status…"
       oninput="filterTable(this.value)">
<table id="results">
  <thead>
    <tr>
      <th>Status</th><th>Site</th><th>Profile URL</th>
      <th>HTTP</th><th>ms</th><th>Error</th>
    </tr>
  </thead>
  <tbody>
{all_rows}  </tbody>
</table>
<script>
function filterTable(q) {{
  q = q.toLowerCase();
  document.querySelectorAll('#results tbody tr').forEach(tr => {{
    const name   = tr.cells[1].textContent.toLowerCase();
    const status = tr.cells[0].textContent.toLowerCase();
    tr.style.display = (name.includes(q) || status.includes(q)) ? '' : 'none';
  }});
}}
</script>
</body>
</html>"""

    with open(filename, "w", encoding="utf-8") as fh:
        fh.write(html)
    return filename


# ── Entry point ────────────────────────────────────────────────────────────────

def main():
    banner()

    # ── Fetch WMN data ──
    try:
        response = requests.get(WMN_DATA_URL, timeout=15)
        response.raise_for_status()
        data = response.json()
    except Exception as exc:
        print(f"\033[31m[!] Failed to fetch WMN data: {exc}\033[0m")
        sys.exit(1)

    # ── Argument parser ──
    parser = argparse.ArgumentParser(
        description=(
            "Scan all sites on Project WhatsMyName for a target username "
            "and wait for \033[32m\033[1mpositive\033[0m identification."
        )
    )
    parser.add_argument("-u", "--username",     help="\033[32m\033[1m\nTarget username\033[0m")
    parser.add_argument("-s", "--singlesearch", nargs="*",
                        help="\033[32m\033[1m\nSingle site search (provide site name(s))\033[0m")
    parser.add_argument("-f", "--fulllist",     action="store_true",
                        help="\033[32m\033[1m\nView full sites list\033[0m")
    parser.add_argument("-c", "--countsites",   action="store_true",
                        help="\033[32m\033[1m\nNumber of supported sites\033[0m")
    parser.add_argument("--no-html",  action="store_true", help="Skip HTML report")
    parser.add_argument("--no-csv",   action="store_true", help="Skip CSV log")
    parser.add_argument("--no-json",  action="store_true", help="Skip JSON log")
    parser.add_argument("--workers",  type=int, default=20,
                        help="Concurrent worker threads (default: 20)")

    args = parser.parse_args()

    # ── --fulllist ──
    if args.fulllist:
        for _ in tqdm(range(10)):
            time.sleep(0.06)
        for site in data["sites"]:
            print(
                f"\n  ╔════════════════╦══════════════════════════════════╗"
                f"\n  ║ WEBSITE NAME:  ║ ✅  \033[1m{site['name']}\033[0m"
                f"\n  ╚════════════════╩══════════════════════════════════╝"
            )

    # ── --countsites ──
    if args.countsites:
        for _ in tqdm(range(10)):
            time.sleep(0.1)
        total = sum(1 for s in data["sites"] if "uri_check" in s)
        print(
            f"\033[32m\033[1mTotal\033[0m\033[32m sites supported on "
            f"\033[1mProject WhatsMyName\033[0m → {total}"
        )

    # ── --username ──
    if args.username:
        username = args.username
        sites    = data["sites"]

        if args.singlesearch:
            targets = {s.lower() for s in args.singlesearch}
            sites   = [s for s in sites if s["name"].lower() in targets]
            if not sites:
                print("\033[31m[!] No matching sites found for your -s filter.\033[0m")
                sys.exit(1)

        print(f"\n\033[1mScanning {len(sites)} site(s) for username:\033[0m \033[32m{username}\033[0m\n")
        results = scan_username(sites, username, max_workers=args.workers)

        found  = [r for r in results if r["status"] == "found"]
        errors = [r for r in results if r["status"] == "error"]
        nf     = [r for r in results if r["status"] == "not_found"]

        # ── Summary ──
        print(f"\n{'─' * 50}")
        print(f"  Sites checked : {len(results)}")
        print(f"  \033[32m\033[1mFound         : {len(found)}\033[0m")
        print(f"  Not found     : {len(nf)}")
        print(f"  Errors        : {len(errors)}")
        print(f"{'─' * 50}\n")

        if found:
            print(f"\033[1m{username}\033[0m was found on {len(found)} site(s):")
            for r in found:
                print(f"  \033[32m{r['name']}\033[0m  →  {r['url_pretty']}")

        # ── Save outputs ──
        saved = []
        if not args.no_json:
            saved.append(("JSON log   ", save_json_log(username, results)))
        if not args.no_csv:
            saved.append(("CSV log    ", save_csv_log(username, results)))
        if not args.no_html:
            saved.append(("HTML report", save_html_report(username, results)))

        if saved:
            print("\n\033[1mOutput files:\033[0m")
            for label, path in saved:
                print(f"  {label} → {path}")


if __name__ == "__main__":
    main()
