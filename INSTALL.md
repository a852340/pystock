# 安装指南

## 系统要求

- Python 3.7 或更高版本
- pip (Python 包管理器)
- 稳定的网络连接

## 快速安装

### 1. 克隆仓库

```bash
git clone <repository-url>
cd <project-directory>
```

### 2. 安装依赖

使用 pip 安装所需的 Python 包：

```bash
pip install -r requirements.txt
```

或者手动安装：

```bash
pip install akshare>=1.11.0 plotext>=5.2.8 pandas>=2.0.0
```

### 3. 验证安装

运行帮助命令验证安装是否成功：

```bash
python main.py --help
```

如果看到帮助信息，说明安装成功。

## 使用虚拟环境（推荐）

为了避免依赖冲突，建议使用 Python 虚拟环境：

### 使用 venv

```bash
# 创建虚拟环境
python3 -m venv venv

# 激活虚拟环境
# Linux/Mac:
source venv/bin/activate
# Windows:
venv\Scripts\activate

# 安装依赖
pip install -r requirements.txt

# 运行程序
python main.py 000001
```

### 使用 conda

```bash
# 创建虚拟环境
conda create -n stock-chart python=3.9

# 激活环境
conda activate stock-chart

# 安装依赖
pip install -r requirements.txt

# 运行程序
python main.py 000001
```

## 依赖说明

本项目依赖以下 Python 包：

1. **akshare** (>= 1.11.0)
   - 用途: 获取中国股市数据
   - 官网: https://akshare.akfamily.xyz/

2. **plotext** (>= 5.2.8)
   - 用途: 在终端中绘制图表
   - GitHub: https://github.com/piccolomo/plotext

3. **pandas** (>= 2.0.0)
   - 用途: 数据处理和分析
   - 官网: https://pandas.pydata.org/

## 常见问题

### 问题1: 安装 akshare 失败

**解决方案**: 尝试更新 pip 后重新安装

```bash
pip install --upgrade pip
pip install akshare
```

### 问题2: 在 Windows 上中文显示乱码

**解决方案**: 设置终端编码为 UTF-8

```bash
# 在 PowerShell 中
[Console]::OutputEncoding = [System.Text.Encoding]::UTF8
```

或使用支持 UTF-8 的终端（如 Windows Terminal）。

### 问题3: ModuleNotFoundError

**解决方案**: 确保在正确的虚拟环境中，并已安装所有依赖

```bash
pip list  # 查看已安装的包
pip install -r requirements.txt  # 重新安装依赖
```

### 问题4: 无法获取数据

**可能原因**:
- 网络连接问题
- 股票代码错误
- 非交易时间

**解决方案**:
- 检查网络连接
- 确认股票代码格式正确（如 000001, 600000）
- 在交易时间内运行程序

## 首次运行

安装完成后，尝试运行一个简单的命令：

```bash
python main.py 000001 --interval 5
```

这将显示平安银行（000001）的实时分时图，每5秒更新一次。

按 `Ctrl+C` 可以退出程序。

## 下一步

- 阅读 [README.md](README.md) 了解项目功能
- 查看 [example.md](example.md) 学习更多使用示例
- 参考 [PROJECT_SUMMARY.md](PROJECT_SUMMARY.md) 了解项目架构

## 获取帮助

如果遇到问题，请：

1. 查看本文档的"常见问题"部分
2. 检查 Python 和依赖版本是否符合要求
3. 在项目仓库提交 Issue
