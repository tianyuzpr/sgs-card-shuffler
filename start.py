import os, sys, time
from utils import Utils as utils
import env
import subprocess

utils.log("start", 2)
try:
    subprocess.run(["chcp", "65001"], check=True, shell=True)
except subprocess.CalledProcessError as e:
    utils.log(f"Failed to set code page: {e}", 4)

# 启动逻辑
def start():
    global env_content
    utils.log("checking ENV File", 2)
    utils.log("change dir to " + os.path.dirname(os.path.abspath(__file__)), 2)
    os.system("cd " + os.path.dirname(os.path.abspath(__file__)))
    utils.log("current dir is " + os.getcwd(), 2)
    # 确认是否切换成功，保险起见，在使用一次os.chdir
    os.chdir(os.path.dirname(os.path.abspath(__file__)))
    utils.log("current dir is " + os.getcwd(), 2)


    env_file = ".env"  # 确保文件名正确
    if not os.path.exists(env_file):
        utils.log("ENV File not found", 3)
        utils.log("creating ENV File", 2)
        with open(env_file, "w") as f:
            f.write("")
        utils.log("ENV File created", 2)
        utils.log("please set the ENV File", 2)
        sys.exit(1)
    utils.log("loading ENV File", 2)
    with open(env_file, "r") as f:
        env_content = f.readlines()  # 读取所有行
    utils.log("ENV File loaded", 2)
    utils.log("checking ENV Variables", 2)
    print(env_content)

    # 解析 env.env 文件内容
    env_variables = {}
    for line in env_content:
        line = line.strip()
        if line and "=" in line:
            key, value = line.split("=", 1)
            env_variables[key.strip()] = value.strip()

    # 检查 default_kazu 是否存在
    if "default_kazu" not in env_variables:
        utils.log("default_kazu not found in ENV File", 4)
        utils.log("please set the default_kazu", 4)
        sys.exit(1)
    
    utils.log("checking ENV Variables done", 2)
    utils.log(env_variables, 2)
    utils.log("loading ENV Variables", 2)
    env.load_env()
    utils.log("loading ENV Variables done", 2)

    # 检测是否启用HTML模式
    html_mode = env.getenv('html_mode', 'false').lower() == 'true'
    if html_mode:
        utils.log("Starting Flask server", 2)
        os.system("python webapp.py")
    else:
        utils.log("Starting Tkinter GUI", 2)
        os.system("python main.py")

def check_system():
    '''检查系统'''
    # 检查Python版本
    utils.log("checking python version", 2)
    if sys.version_info < (3, 6):
        utils.log("python version is less than 3.6, please upgrade", 4)
        sys.exit(1)
    utils.log("checking python version done", 2)
    
    # 检查操作系统类型
    utils.log("checking system", 2)
    if sys.platform == "win32":
        utils.log("system is windows", 2)
        # 设置窗口标题
        os.system("title SGS Card Shuffler")
    elif sys.platform == "linux":
        utils.log("system is linux", 2)
    elif sys.platform == "darwin":
        utils.log("system is macos", 2)
    else:
        # 不支持的操作系统
        utils.log("system is unknown", 4)
        utils.log("please use windows/mac/linux", 4)
        utils.log("or set env:\"system\" to windows/mac/linux", 4)
        sys.exit(1)
    utils.log("checking system done", 2)

if __name__ == "__main__":
    check_system()
    start()