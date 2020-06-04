click_wait_time = 1
video_load_wait_time = 5
video_check_time = 3
mainloop_wait_time = 5

resFolderViewList_wait_time = 0
colUrlStuView_wait_time = 0
thread_wait_time = 0
test_wait_time = 0
unknown_wait_time = 0

savedDataExist = False
savedData = {}
savedDataFileName = "saved-data.json"
import os
import json
if os.path.exists(savedDataFileName):
    try:
        f = open(savedDataFileName, "r")
        t = f.read()
        f.close()
        savedData = json.loads(t)
        savedDataExist = True
    except:
        print("读取配置文件失败...忽略错误")

if savedDataExist:
    x = input("已读取到保存的账号信息\n链接: {}\n账号: {}\n密码: {}\n是否使用? (Y/n): "
              .format(savedData["umooc_link"],
                      savedData["umooc_username"],
                      savedData["umooc_password"]))
    if x.lower() == "n":
        savedDataExist = False

if savedDataExist:
    umooc_link = savedData["umooc_link"]
    umooc_username = savedData["umooc_username"]
    umooc_password = savedData["umooc_password"]
else:
    # umooc_link = "http://jpkc.bcu.edu.cn/meol/index.do"
    umooc_link = "http://jpkc.bcu.edu.cn/meol/"
    input_umooc = input("请输入学校优慕课链接\n"
                        "（如：http://jpkc.bcu.edu.cn/meol/\n"
                        "输入不正确会导致后续程序运行出现问题，留空默认为北京城市学院在线教育综合平台）：\n")
    if (input_umooc == ""):
        print("已默认选择：北京城市学院在线教育综合平台")
    else:
        umooc_link = input_umooc
    umooc_username = input("优慕课用户名:\n")
    umooc_password = input("优慕课密码:\n")
    savedData["umooc_link"] = umooc_link
    savedData["umooc_username"] = umooc_username
    savedData["umooc_password"] = umooc_password
    try:
        t = json.dumps(savedData)
        f = open(savedDataFileName, "w")
        f.write(t)
        f.close()
    except:
        print("保存配置文件失败...忽略错误")
