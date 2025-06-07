# WAV File Cutter

一个简单的 Python 脚本，用于在 Windows 11 环境下，根据 `CutTime.txt` 文件中提供的时间戳，使用 FFmpeg 将一个 `.wav` 音频文件分割成多个片段。
![ScreenShot1](https://github.com/user-attachments/assets/b9fc6267-6a9e-4cf1-a198-1a82cfa15d6b)

## 🚀 功能

* 将单个 `.wav` 文件分割成多个部分。
* 从外部文本文件读取切割时间点。
* 易于使用和配置。

## 📋 环境准备

在开始之前，请确保您已安装并配置好以下软件：

1.  **Python 3:** 确保您的系统已安装 Python。您可以从 [python.org](https://www.python.org/downloads/) 下载。
2.  **FFmpeg:** 您必须安装 FFmpeg，并将其可执行文件路径添加到 Windows 的环境变量 `Path` 中，以便在命令提示符中可以直接调用。您可以从 [ffmpeg.org](https://ffmpeg.org/download.html) 下载 FFmpeg。

## 🛠️ 如何使用

1.  **下载或克隆项目**：
    将项目文件下载到您的本地计算机。

2.  **准备文件**：
    * 将您要切割的源 `.wav` 文件（例如 `input.wav`）放在项目文件夹中。
    * 在同一文件夹中创建一个名为 `CutTime.txt` 的文件。

3.  **编辑 `CutTime.txt`**：
    * 在此文件中添加您要切割音频的时间点。每个时间戳应为 `HH:MM:SS,ms` 格式，每行一个。
    * 脚本将根据这些时间戳创建分段。第一个分段是从音频开始到第一个时间戳，第二个分段是从第一个时间戳到第二个时间戳，以此类推，直到音频文件结束。

    **`CutTime.txt` 示例内容：**
    ```
    00:00:17,640
    00:00:30,560
    00:00:44,120
    00:01:00,280
    00:01:12,640
    00:01:29,120
    00:01:46,400
    ```

4.  **运行脚本**：
    * 在项目文件夹中打开命令提示符 (CMD) 或 PowerShell。
    * 使用以下命令执行脚本，请将 `input.wav` 替换为您自己的音频文件名：

    ```bash
    python split_audio.py input.wav
    ```

5.  **查看输出**：
    * 脚本将创建一个名为 `output` 的新文件夹。
    * 在 `output` 文件夹中，您会找到切割好的 `.wav` 文件，它们会按顺序命名（例如 `output_1.wav`, `output_2.wav`, 等等）。

## 🤝 贡献

欢迎任何形式的贡献！如果您有改进建议，请随时提交 Pull Request 或开启一个 Issue。
