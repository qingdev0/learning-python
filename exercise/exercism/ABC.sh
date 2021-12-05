# 2021-10-16

#################################
# install exercism via Homebrew #
#################################
brew update
brew install exercism

exercism version
# exercism version 3.0.13

###################
# Working Locally #
###################
# URL: https://exercism.org/docs/using/solving-exercises/working-locally

# exercism configure --token=<your-api-token>
exercism configure --token="e3ce1eee-786a-41b7-be9d-68d8752f6605" --workspace="/Users/ewanli/code/pytk/exeecise/exercism"

# command output:
#    You have configured the Exercism command-line client:
#    Config dir:                       /Users/ewanli/.config/exercism
#    Token:         (-t, --token)      e3ce1eee-786a-41b7-be9d-68d8752f6605
#    Workspace:     (-w, --workspace)  /Users/ewanli/Exercism
#    API Base URL:  (-a, --api)        https://api.exercism.io/v1


# exercism download --exercise=<exercise-slug> --track=<track-slug>
exercism download --exercise=hello-world --track=python



# exercism submit <implementation_file_paths>
exercism submit ${pytk_home}/exeecise/exercism/python/hello-world/hello_world.py


# exercism troubleshoot
# exercism help