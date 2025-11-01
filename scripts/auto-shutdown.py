#!/usr/bin/env python3
import time
import os
import requests
import threading

# 计算时间点（5小时 = 18000秒）
MAX_RUNTIME = 18000
SHUTDOWN_MARGIN = 1800  # 希望留出30分钟（1800秒）用于数据保存和上传
SHUTDOWN_AT = MAX_RUNTIME - SHUTDOWN_MARGIN

def send_server_command(command):
    """通过 RCON 或直接向服务器标准输入发送命令（此处为简化示例）"""
    # 实际实现可能需要使用 RCON 协议或直接写入容器的标准输入
    print(f"[INFO] 执行命令: {command}")

def graceful_shutdown():
    """安全关闭服务器"""
    print("[INFO] 准备关闭服务器...")
    send_server_command("say 服务器将在5分钟后自动保存并关闭，感谢大家的游玩！")
    time.sleep(60)
    send_server_command("say 服务器将在1分钟后关闭，请做好准备。")
    time.sleep(30)
    send_server_command("say 最后30秒！正在保存世界...")
    send_server_command("save-all")  # 强制保存所有数据
    time.sleep(25)
    send_server_command("say 服务器关闭中...")
    send_server_command("stop")      # 停止服务器
    print("[INFO] 服务器关闭指令已发送。")

def main():
    print(f"[INFO] 守护脚本已启动。将在 {SHUTDOWN_AT/3600} 小时后触发关闭流程。")
    time.sleep(SHUTDOWN_AT)
    graceful_shutdown()

if __name__ == "__main__":
    main()
