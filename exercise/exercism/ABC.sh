#!/usr/bin/env bash

repo_root=$(git rev-parse --show-toplevel)

#################################
# install exercism via Homebrew #
#################################
# Check if exercism is installed and update or install accordingly
if brew list exercism &> /dev/null; then
    echo "Exercism is already installed, upgrading if needed..."
    brew upgrade exercism
else
    echo "Installing exercism..."
    brew install exercism
fi

exercism version
# exercism version 3.0.13

###################
# Working Locally #
###################
# URL: https://exercism.org/docs/using/solving-exercises/working-locally

# Ask for Exercism token interactively
echo "Please enter your Exercism token (from https://exercism.org/settings/api_cli):"
read -r EXERCISM_TOKEN

# Configure exercism with the provided token
exercism configure --token="${EXERCISM_TOKEN}" --workspace="/Users/ewanli/code/pytk/exercise/exercism"

# command output:
#    You have configured the Exercism command-line client:
#    Config dir:                       /Users/ewanli/.config/exercism
#    Token:         (-t, --token)      e3ce1eee-786a-41b7-be9d-68d8752f6605
#    Workspace:     (-w, --workspace)  /Users/ewanli/Exercism
#    API Base URL:  (-a, --api)        https://api.exercism.io/v1

# exercism download --exercise=<exercise-slug> --track=<track-slug>
exercism download --exercise=hello-world --track=python

# exercism submit <implementation_file_paths>
exercism submit "${repo_root}/exercise/exercism/python/hello-world/hello_world.py"

# exercism troubleshoot
# exercism help
