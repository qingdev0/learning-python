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


if __name__ == "__main__":
    pytk_banner()
