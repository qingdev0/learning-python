#!/usr/local/bin/python
#!/usr/bin/env python
# set -x
####################################################################################################
# shell name : ${pytk_home}/exercism/python/hello-world/hello_world.py                             #
# source     :                                                                                     #
# purpose    :                                                                                     #
# parameter  : NONE                                                                                #
# dependency :                                                                                     #
# tested     : Python 2.7.5 @ RHEL 7.6                                                             #
# created    : v1.1 (2021-10-17)                                                                   #
# revised    : V1.2 (2021-10-17)                                                                   #
# location   : DBA\                                                                                #
# c#20211017 : v1.2 change:                                                                        #
####################################################################################################

###########
# modules #
###########
import platform


###############
# pytk banner #
###############
def pytk_banner():
    py_info = platform.python_version()
    os_info = platform.system() + "(" + platform.platform() + ")"

    banner_message_1 = f"* Python Information: {py_info}"
    banner_message_2 = f"* System Information: {os_info}"

    v_letter = "*"
    v_repeat = 66
    banner_message_x = "".join([char * v_repeat for char in v_letter])

    print(banner_message_x)
    print(banner_message_1)
    print(banner_message_2)
    print(banner_message_x)


pytk_banner()


########
# main #
########
# def hello():
#     return 'Goodbye, Mars!'


def hello():
    message = "Hello, World!"
    return message


print(hello())

#######
# eof #
#######
