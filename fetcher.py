import akshare as ak
from typing import Optional
import pandas as pd
from datetime import datetime


class StockDataFetcher:
    def __init__(self, symbol: str):
        self.symbol = symbol
        self.previous_close = None
        
    def fetch_minute_data(self) -> Optional[pd.DataFrame]:
        try:
            df = ak.stock_zh_a_hist_min_em(
                symbol=self.symbol,
                period='1',
                adjust=''
            )
            
            if df is None or df.empty:
                return None
            
            return df
            
        except Exception as e:
            print(f"获取数据失败: {e}")
            return None
    
    def get_previous_close(self) -> Optional[float]:
        if self.previous_close is not None:
            return self.previous_close
            
        try:
            df = ak.stock_zh_a_hist(
                symbol=self.symbol,
                period='daily',
                start_date=(datetime.now().strftime('%Y%m%d')),
                end_date=(datetime.now().strftime('%Y%m%d')),
                adjust=''
            )
            
            if df is not None and not df.empty and '昨收' in df.columns:
                self.previous_close = float(df['昨收'].iloc[-1])
                return self.previous_close
            
            df_minute = self.fetch_minute_data()
            if df_minute is not None and not df_minute.empty:
                today_dates = df_minute['时间'].dt.date.unique()
                if len(today_dates) > 0:
                    today = today_dates[-1]
                    today_data = df_minute[df_minute['时间'].dt.date == today]
                    if not today_data.empty:
                        first_price = float(today_data.iloc[0]['开盘'])
                        self.previous_close = first_price
                        return self.previous_close
            
            return None
            
        except Exception as e:
            print(f"获取前收盘价失败: {e}")
            return None
    
    def get_current_price(self, df: pd.DataFrame) -> Optional[float]:
        if df is None or df.empty:
            return None
        return float(df.iloc[-1]['收盘'])
    
    def calculate_change_percent(self, current_price: float, previous_close: float) -> float:
        if previous_close == 0:
            return 0.0
        return ((current_price - previous_close) / previous_close) * 100
