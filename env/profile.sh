#!/bin/bash
###################################################################################################
# file name : env/profile.sh                                                                      #
# purpose   : Load pyenv automatically while shell is initiating by .zprofile                     #
###################################################################################################

# Load pyenv
export PYENV_ROOT="${HOME}/.pyenv"
export PATH="${PYENV_ROOT}/bin:${PATH}"

if command -v pyenv 1> /dev/null 2>&1; then
    eval "$(pyenv init -)"
fi

# To enable auto-activation add to your profile:
if which pyenv-virtualenv-init > /dev/null; then
    eval "$(pyenv virtualenv-init -)"

    alias kata='cd ~/code/learning/python && pyenv activate kata'
fi

#######
# end #
#######
