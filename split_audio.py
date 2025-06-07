import os
import subprocess
import sys


def split_wav_file(input_file, timestamps_file):
    """
    根据给定的时间戳文件，使用 FFmpeg 切割 WAV 文件。

    参数:
    input_file (str): 输入的 .wav 文件名。
    timestamps_file (str): 包含切割时间点（HH:MM:SS,ms）的文本文件名。
    """
    # 检查输入文件是否存在
    if not os.path.isfile(input_file):
        print(f"错误：找不到输入文件 '{input_file}'")
        return

    # 检查时间戳文件是否存在
    if not os.path.isfile(timestamps_file):
        print(f"错误：找不到时间戳文件 '{timestamps_file}'")
        return

    # 读取并解析时间戳
    with open(timestamps_file, 'r') as f:
        timestamps = [line.strip() for line in f if line.strip()]

    if not timestamps:
        print("错误：时间戳文件为空。")
        return

    # 创建输出目录
    output_dir = "output"
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
        print(f"已创建输出目录：'{output_dir}'")

    # FFmpeg 命令的基本部分
    base_cmd = ['ffmpeg', '-i', input_file]

    # 第一个片段：从头到第一个时间戳
    start_time = "00:00:00.000"
    end_time = timestamps[0].replace(',', '.')
    output_filename = os.path.join(output_dir, f"output_1.wav")

    print(f"正在处理第 1 段：从 {start_time} 到 {end_time}")
    command = base_cmd + ['-ss', start_time, '-to', end_time, '-c', 'copy', output_filename]

    try:
        # 使用 CREATE_NO_WINDOW 标志来防止在 Windows 上打开新的命令行窗口
        subprocess.run(command, check=True, capture_output=True, text=True, creationflags=subprocess.CREATE_NO_WINDOW)
    except FileNotFoundError:
        print("\n错误：找不到 'ffmpeg' 命令。")
        print("请确保 FFmpeg 已安装，并已将其路径添加到系统的 PATH 环境变量中。")
        return
    except subprocess.CalledProcessError as e:
        print(f"FFmpeg 在处理第 1 段时出错:\n{e.stderr}")
        return

    # 中间的片段
    for i in range(len(timestamps) - 1):
        start_time = timestamps[i].replace(',', '.')
        end_time = timestamps[i + 1].replace(',', '.')
        segment_number = i + 2
        output_filename = os.path.join(output_dir, f"output_{segment_number}.wav")

        print(f"正在处理第 {segment_number} 段：从 {start_time} 到 {end_time}")
        command = base_cmd + ['-ss', start_time, '-to', end_time, '-c', 'copy', output_filename]

        try:
            subprocess.run(command, check=True, capture_output=True, text=True,
                           creationflags=subprocess.CREATE_NO_WINDOW)
        except subprocess.CalledProcessError as e:
            print(f"FFmpeg 在处理第 {segment_number} 段时出错:\n{e.stderr}")
            continue

    # 最后一个片段：从最后一个时间戳到文件结尾
    start_time = timestamps[-1].replace(',', '.')
    segment_number = len(timestamps) + 1
    output_filename = os.path.join(output_dir, f"output_{segment_number}.wav")

    print(f"正在处理第 {segment_number} 段：从 {start_time} 到文件结尾")
    command = base_cmd + ['-ss', start_time, '-c', 'copy', output_filename]

    try:
        subprocess.run(command, check=True, capture_output=True, text=True, creationflags=subprocess.CREATE_NO_WINDOW)
    except subprocess.CalledProcessError as e:
        print(f"FFmpeg 在处理第 {segment_number} 段时出错:\n{e.stderr}")

    print("\n✅ 文件切割完成！所有片段已保存在 'output' 文件夹中。")


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("使用方法: python split_audio.py <your_audio_file.wav>")
        sys.exit(1)

    input_audio_file = sys.argv[1]
    timestamps_definition_file = "CutTime.txt"
    split_wav_file(input_audio_file, timestamps_definition_file)