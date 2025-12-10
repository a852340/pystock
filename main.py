import argparse
from app import RealtimeStockApp
from config import DEFAULT_INTERVAL, DEFAULT_SHOW_VOLUME


def main():
    parser = argparse.ArgumentParser(
        description='实时显示A股分时图',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
示例:
  python main.py 000001              # 显示000001的分时图，默认5秒更新
  python main.py 600000 --interval 2 # 显示600000的分时图，2秒更新
  python main.py 000001 --volume     # 显示000001的分时图并显示成交量
        """
    )
    
    parser.add_argument(
        'symbol',
        type=str,
        help='股票代码 (例如: 000001, 600000)'
    )
    
    parser.add_argument(
        '--interval',
        type=int,
        default=DEFAULT_INTERVAL,
        help=f'更新间隔（秒），默认为 {DEFAULT_INTERVAL} 秒'
    )
    
    parser.add_argument(
        '--volume',
        action='store_true',
        default=DEFAULT_SHOW_VOLUME,
        help='显示成交量'
    )
    
    args = parser.parse_args()
    
    if args.interval < 1:
        print("错误: 更新间隔必须大于等于1秒")
        return
    
    app = RealtimeStockApp(
        symbol=args.symbol,
        interval=args.interval,
        show_volume=args.volume
    )
    
    app.start()


if __name__ == '__main__':
    main()
