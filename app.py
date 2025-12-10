import time
import os
from typing import Optional
from fetcher import StockDataFetcher
from chart import ChartRenderer


class RealtimeStockApp:
    def __init__(self, symbol: str, interval: int = 5, show_volume: bool = False):
        self.symbol = symbol
        self.interval = interval
        self.show_volume = show_volume
        self.fetcher = StockDataFetcher(symbol)
        self.renderer = ChartRenderer(show_volume)
        self.running = False
    
    def start(self):
        self.running = True
        print(f"正在启动股票 {self.symbol} 的实时分时图...")
        print(f"更新间隔: {self.interval}秒")
        print("按 Ctrl+C 退出\n")
        
        previous_close = self.fetcher.get_previous_close()
        if previous_close is None:
            print("警告: 无法获取前收盘价，将使用当日首个价格作为基准")
        
        try:
            while self.running:
                self._update()
                time.sleep(self.interval)
        except KeyboardInterrupt:
            self.stop()
    
    def _update(self):
        df = self.fetcher.fetch_minute_data()
        
        if df is None or df.empty:
            print("获取数据失败，将在下次更新重试...")
            return
        
        previous_close = self.fetcher.get_previous_close()
        if previous_close is None:
            if not df.empty:
                previous_close = float(df.iloc[0]['开盘'])
                self.fetcher.previous_close = previous_close
        
        current_price = self.fetcher.get_current_price(df)
        if current_price is None:
            print("无法获取当前价格")
            return
        
        change_percent = self.fetcher.calculate_change_percent(current_price, previous_close)
        
        self._clear_screen()
        self.renderer.render(df, previous_close, current_price, change_percent, self.symbol)
        
        print(f"\n最后更新: {time.strftime('%Y-%m-%d %H:%M:%S')}")
        print(f"下次更新: {self.interval}秒后")
    
    def _clear_screen(self):
        os.system('clear' if os.name == 'posix' else 'cls')
    
    def stop(self):
        self.running = False
        print("\n\n程序已停止")
