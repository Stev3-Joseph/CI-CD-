ruff check .
if ($LASTEXITCODE -ne 0) { exit 1 }

ruff format --check .
if ($LASTEXITCODE -ne 0) { exit 1 }

python -m pytest
if ($LASTEXITCODE -ne 0) { exit 1 }