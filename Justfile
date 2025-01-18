TOPIC := "Available Recipes for Python Learning:\n"

_default:
    @just --list --unsorted --list-prefix "✨ " --list-heading '{{TOPIC}}'

install-python-requirements:
    pip install -r requirements.txt --upgrade

commit:
    #!/usr/bin/env bash
    git status
    echo -n "Enter commit message: "
    read commit_message
    git commit -m "${commit_message}"
    git push

lazy-commit:
    #!/usr/bin/env bash
    git add homebrew/Brewfile
    # Check for unstaged changes
    if ! git diff --quiet; then
        echo "Error: There are unstaged changes. Please stage all changes before running this command."
        echo "Unstaged changes:"
        git --no-pager diff --name-status
        exit 1
    fi
    git commit --amend --no-edit
    git push --force

update-pre-commithooks:
    #!/usr/bin/env bash
    set -euo pipefail
    pre-commit autoupdate
    pre-commit install
    git add .pre-commit-config.yaml
    if git diff --cached --quiet .pre-commit-config.yaml; then
        echo "No changes to pre-commit config"
    else
        echo "Pre-commit config updated and staged"
    fi
