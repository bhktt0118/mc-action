#!/usr/bin/env python3
import time
import os
import subprocess

def send_server_command(command):
    """向Minecraft服务器发送命令"""
    try:
        # 使用rcon-cli发送命令
        result = subprocess.run([
            "docker", "exec", "mc-server",
            "rcon-cli", command
        ], capture_output=True, text=True, timeout=10)
        print(f"命令 '{command}' 执行结果: {result.returncode}")
        return True
    except Exception as e:
        print(f"发送命令失败: {e}")
        return False

def graceful_shutdown():
    """安全关闭服务器"""
    print("开始安全关闭流程...")
    
    # 发送警告消息
    send_server_command("say 服务器将在3分钟后自动保存并关闭！")
    time.sleep(120)
    
    send_server_command("say 服务器将在1分钟后关闭，请做好准备！")
    time.sleep(30)
    
    send_server_command("say 正在保存世界数据...")
    send_server_command("save-all")
    time.sleep(25)
    
    send_server_command("say 服务器关闭中...")
    send_server_command("stop")
    print("关闭命令已发送")

def main():
    """主函数 - 5小时后触发关闭"""
    # 5小时 = 18000秒
    wait_time = 18000
    
    print(f"自动关闭守护进程已启动，将在{wait_time/3600}小时后执行关闭")
    print(f"等待时间: {wait_time}秒")
    
    time.sleep(wait_time)
    graceful_shutdown()

if __name__ == "__main__":
    main()
