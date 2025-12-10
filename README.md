# A股分时图实时显示

一个Python控制台应用，支持实时绘制A股分时图表。

## 功能特性

- 实时获取并显示A股分时图
- 支持深交所、上交所股票代码
- 可自定义更新频率（默认5秒）
- 显示前收盘价基准线
- 显示当前价格和涨跌幅
- 可选显示成交量

## 安装

```bash
pip install -r requirements.txt
```

## 使用方法

### 基本用法

```bash
python main.py 000001
```

### 自定义更新间隔

```bash
python main.py 600000 --interval 2
```

### 显示成交量

```bash
python main.py 000001 --volume
```

### 完整选项

```bash
python main.py 股票代码 [--interval 秒数] [--volume]
```

## 参数说明

- `symbol`: 股票代码（必需），例如 000001、600000
- `--interval`: 更新间隔（秒），默认为 5 秒
- `--volume`: 显示成交量图表（可选）

## 退出程序

按 `Ctrl+C` 退出程序

## 技术栈

- **数据源**: akshare - 获取实时A股数据
- **绘图**: plotext - 终端图表绘制
- **数据处理**: pandas - 数据处理和分析

## 项目结构

```
.
├── main.py       # CLI入口
├── app.py        # 主应用和实时更新逻辑
├── fetcher.py    # 数据获取模块
├── chart.py      # 图表绘制模块
├── config.py     # 配置管理
└── requirements.txt  # 依赖包
```

## 注意事项

- 股票代码格式：深交所以000、002、300开头，上交所以600、601、603、688开头
- 数据更新依赖网络连接和akshare数据源
- 建议更新间隔不低于2秒，避免过度请求
- 仅在交易时间段内有实时数据更新
