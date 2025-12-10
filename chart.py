import plotext as plt
import pandas as pd
from typing import Optional


class ChartRenderer:
    def __init__(self, show_volume: bool = False):
        self.show_volume = show_volume
    
    def render(self, df: pd.DataFrame, previous_close: float, 
               current_price: float, change_percent: float, symbol: str):
        plt.clear_figure()
        
        if df is None or df.empty:
            print("暂无数据")
            return
        
        today_dates = df['时间'].dt.date.unique()
        if len(today_dates) > 0:
            today = today_dates[-1]
            df_today = df[df['时间'].dt.date == today].copy()
        else:
            df_today = df.copy()
        
        if df_today.empty:
            print("今日暂无数据")
            return
        
        times = df_today['时间'].dt.strftime('%H:%M').tolist()
        prices = df_today['收盘'].tolist()
        
        if self.show_volume:
            plt.subplots(2, 1)
            plt.subplot(1, 1)
        
        plt.plot(times, prices, label="价格", color="cyan")
        
        if previous_close is not None:
            plt.hline(previous_close, label="前收盘价", color="yellow")
        
        change_symbol = "+" if change_percent >= 0 else ""
        color_indicator = "🔴" if change_percent >= 0 else "🟢"
        
        title = f"{symbol} 分时图 | 当前: {current_price:.2f} | {color_indicator} {change_symbol}{change_percent:.2f}%"
        plt.title(title)
        
        plt.xlabel("时间")
        plt.ylabel("价格")
        
        if len(times) > 20:
            tick_interval = len(times) // 10
            plt.xticks([times[i] for i in range(0, len(times), tick_interval)])
        
        if self.show_volume:
            plt.subplot(2, 1)
            volumes = df_today['成交量'].tolist()
            plt.bar(times, volumes, label="成交量", color="blue")
            plt.xlabel("时间")
            plt.ylabel("成交量")
            if len(times) > 20:
                tick_interval = len(times) // 10
                plt.xticks([times[i] for i in range(0, len(times), tick_interval)])
        
        plt.show()
    
    def clear(self):
        plt.clear_figure()
