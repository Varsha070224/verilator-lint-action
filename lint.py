import os
import json
import subprocess

files = os.environ["SV_FILES"].split()

results = {}

for file in files:
    try:
        subprocess.run(
            ["verilator", "--lint-only", file],
            check=True,
            capture_output=True
        )

        results[file] = "PASS"

    except subprocess.CalledProcessError:
        results[file] = "FAIL"

json_result = json.dumps(results)

with open(os.environ["GITHUB_OUTPUT"], "a") as f:
    f.write(f"results={json_result}\n")

