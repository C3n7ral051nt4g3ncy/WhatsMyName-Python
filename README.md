[![security: bandit](https://img.shields.io/badge/security-bandit-yellow.svg)](https://github.com/PyCQA/bandit)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

# [WhatsMyName](https://github.com/WebBreacher/WhatsMyName) Python Script V1.3 🔍

As a regular contributor to Project [WhatsMyName](https://whatsmyname.app), this is a Python script I made for myself.

The script is **unofficial** and is not part of Project WhatsMyName.

Feel free to use it! 

<img width="333" src="https://user-images.githubusercontent.com/104733166/189120786-f854c5f8-57df-408c-bf33-b8eda521572c.png">

---

# Support ♡

There is no support button on this repository. This is because WhatsMyName is not my project — `this is my own personal script`. All support should go to Project [WhatsMyName](https://github.com/WebBreacher/WhatsMyName) and to [@WebBreacher](https://ko-fi.com/WebBreacher). **DO NOT DONATE TO ME.**

---

# License ©

I am a regular contributor to Project WhatsMyName, but I am not officially part of its creation. WMN is licensed under the Creative Commons Attribution-ShareAlike 4.0 International License. **Copyright (C) Micah Hoffman**

---

# Installation ⚙️

## Option 1 — pipx (recommended)

Install once, and the `whatsmyname` command becomes available globally in your terminal — no virtual environment management, no path hassle.

```bash
pipx install git+https://github.com/C3n7ral051nt4g3ncy/WhatsMyName-Python.git
```

To update to the latest version at any time:

```bash
pipx upgrade WhatsMyName-Python
```

To uninstall:

```bash
pipx uninstall WhatsMyName-Python
```

## Option 2 — Classic git clone

```bash
git clone https://github.com/C3n7ral051nt4g3ncy/WhatsMyName-Python
cd WhatsMyName-Python
pip install -r requirements.txt
```

---

# Usage 📖

## pipx install users

Once installed via pipx, just run `whatsmyname` from anywhere:

```bash
whatsmyname -u <username>
```

## git clone users

```bash
python3 whatsmyname.py -u <username>
```

---

## Commands

- **Help:**
```bash
whatsmyname -h
```

- **Count** the number of sites currently supported on Project WhatsMyName:
```bash
whatsmyname -c
```

- **Full sites list** supported on Project WhatsMyName:
```bash
whatsmyname -f
```

- **Scan** the full sites list for a target username:
```bash
whatsmyname -u johndoe
```

- **Single site search** — check if a username exists on a specific site:
```bash
whatsmyname -u johndoe -s "Bluesky 2"
```

- **Control output files** — skip formats you don't need:
```bash
whatsmyname -u johndoe --no-csv --no-json   # HTML report only
whatsmyname -u johndoe --no-html            # JSON + CSV only
```

- **Tune concurrency** — adjust the number of parallel workers (default: 20):
```bash
whatsmyname -u johndoe --workers 40
```

---

# Screenshot 📸

<img width="633" src="https://github.com/user-attachments/assets/6ec11b0c-183d-48f1-be57-92ad5e5bd7e5">
</p>

---

# Output & Reports 📊

Every scan automatically generates **three output files**, all timestamped so repeated scans never overwrite each other:

| File | Format | Contents |
|---|---|---|
| `wmn_<user>_<timestamp>.html` | HTML | Colour-coded report with a **found-accounts summary at the top**, then the full results table with a live filter |
| `wmn_<user>_<timestamp>.json` | JSON | Full structured log — every site checked, with status, HTTP code, response time, and any error message |
| `wmn_<user>_<timestamp>.csv` | CSV | Spreadsheet-friendly log of all results, easy to import into other tools |

All three files are saved in whichever directory you run the command from.

<img width="933" src="https://github.com/user-attachments/assets/27a783f0-f6ce-4755-83ee-c61e2032a81c">

---

# Latest Improvements 🚀

### Version 1.3
- **`uri_pretty` support**: when a site defines a `uri_pretty` field in the WMN dataset, the clean human-facing profile URL is shown in all output — terminal, HTML, JSON, and CSV — instead of the internal check URL which may point to an API endpoint. Sites without `uri_pretty` fall back to `uri_check` automatically.
- **Full response logging**: all sites are now logged, not just hits. Every result — found, not found, or error — is recorded with its HTTP status code, response time in milliseconds, and error message if applicable.
- **Three output formats**: JSON, CSV, and HTML are all generated automatically at the end of each scan. Individual formats can be skipped with `--no-html`, `--no-csv`, or `--no-json`.
- **Timestamped output files**: repeated scans no longer overwrite previous reports.
- **pipx support**: the script can now be installed globally via pipx without cloning the repo.
- **`--workers` flag**: concurrency is now configurable from the command line.
- **Proper error handling**: each site failure is caught and recorded with the actual exception message instead of being silently discarded.
- **HTML report improvements**: found accounts appear in a dedicated green summary table at the top of the report, followed by the full colour-coded results table with a live search filter.

### Version 1.2
- Improved code structure and separation of concerns.
- Fixed progress bar bug where `pbar` was referenced outside its `with` block.

### Version 1.1
- Links made clickable in the HTML report. Special thanks to [boringthegod](https://github.com/boringthegod) for the request and idea.
- Scan speed significantly improved while maintaining accuracy.
- **HTML Report Generation**: a `.html` report is generated at the end of each scan with all found links in one place.

---

# Contributors 🎉

Huge thanks to the following contributors for their valuable contributions to this project:

<table>
    <tr>
        <td align="center">
            <a href="https://github.com/hippiiee">
                <img src="https://avatars.githubusercontent.com/u/41185722?v=4" width="99;" alt="@hippiiee"/>
                <br />
                <sub><b>@hippiiee</b></sub>
            </a>
        </td>
        <td align="center">
            <a href="https://github.com/ljrk0">
                <img src="https://avatars.githubusercontent.com/u/7831843?v=4" width="99;" alt="@ljrk0"/>
                <br />
                <sub><b>@ljrk0</b></sub>
            </a>
        </td>
        <td align="center">
            <a href="https://github.com/webbreacher">
                <img src="https://avatars.githubusercontent.com/u/2359093?v=4" width="99;" alt="@webbreacher"/>
                <br />
                <sub><b>@Webbreacher</b></sub>
            </a>
        </td>
    </tr>
</table>

<br>

To add yourself to this list, please make a pull request with your GitHub username.





