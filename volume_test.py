#!/usr/bin/env python3
# hackintosh, alcid layout auto test

# 黑苹果，自动测试 alcid layout
# 1 修改下面四个参数为你电脑的参数
# 2 打开mac的免密码登录
# 3 修改本文件为 volume_test.command 添加到用户启动项中
# 4 双击打开 volume_test.command 开启运行
# 注意：config.plist 需要预先写入 <string>-v keepsyms=1 debug=0x100 alcid=1</string>
# 注意：layout 中第一项需要与上一个注意中的alcid相同，作为起始点。例子中为：1
# 注意：本脚本不会测试 layout 中第一项的值

# 本脚本自动更换要测试的layout id，并检测当前声音是否正常，如不正常则自动挂载efi磁盘，
# 并修改plist文件中的alcid

import os
import re
import subprocess

# 修改下面四个参数
layout = [1, 12, 15, 16, 17, 18, 20, 22, 31, 97, 99]  # 要测试的layout值
password = "0000"  # 电脑的密码
efi = "disk4s1"  # efi磁盘名 使用 $ diskutil list 可查看
plist = "/Volumes/EFI/EFI/OC/config.plist"  # plist文件位置


def systemShell(shell):
    result = subprocess.run(shell, stdout=subprocess.PIPE)
    return (result.returncode, result.stdout.decode('UTF-8').strip())


def volumeFail():
    res = systemShell(['osascript', '-e', 'get volume settings'])
    return 'miss' in res[1]


def mount():
    os.system('echo "{}" | sudo -S diskutil mount {}'.format(password, efi))


def edit():
    p = ""
    with open(plist) as f:
        p = f.read()
    find = re.findall("alcid=(\d+)<", p)
    cur = -1
    if len(find) != 0:
        cur = int(find[0])
    if cur not in layout:
        print("current id not in layout list")
        return False
    for index, id in enumerate(layout):
        if id == cur:
            if index == len(layout) - 1:
                print("last layout")
                return False
            else:
                p = re.sub("alcid=(\d+)<",
                           "alcid={}<".format(layout[index + 1]), p)
                print("try layout: ", layout[index + 1])
                with open(plist, "w") as f:
                    f.write(p)
    return True


def restart():
    os.system('echo "{}" | sudo -S reboot'.format(password))


def main():
    if volumeFail():
        print("current volume failed")
        mount()
        print("mount efi")
        if edit():
            print("restrt")
            restart()
        else:
            print("edit failed")
    else:
        print("success")


if __name__ == '__main__':
    main()
