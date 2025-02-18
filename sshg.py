import os
import subprocess
import pyperclip

# 确定 SSH 密钥文件的路径
ssh_dir = os.path.expanduser('~/.ssh')
private_key_path = os.path.join(ssh_dir, 'id_rsa')
public_key_path = os.path.join(ssh_dir, 'id_rsa.pub')

def generate_ssh_key():
    """生成新的 SSH 密钥对"""
    print("生成新的 SSH 密钥对...")
    subprocess.run(['ssh-keygen', '-t', 'rsa', '-b', '4096', '-f', private_key_path, '-N', ''], check=True)
    print(f"SSH 密钥对已生成：{private_key_path} 和 {public_key_path}")

def print_and_copy_public_key():
    """打印公钥的内容并将其复制到剪贴板"""
    with open(public_key_path, 'r') as pub_key_file:
        public_key = pub_key_file.read()
    print("SSH 公钥是：")
    print(public_key)
    pyperclip.copy(public_key)
    print("公钥内容已复制到剪贴板。")

def main():
    # 检查 SSH 密钥文件是否存在
    if os.path.exists(private_key_path) and os.path.exists(public_key_path):
        print_and_copy_public_key()
    else:
        # 如果不存在，则生成新的 SSH 密钥对
        generate_ssh_key()
        print_and_copy_public_key()

if __name__ == "__main__":
    main()
