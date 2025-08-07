#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import json
import time
from typing import Dict, List, Any, Optional

class DataProcessor:
    """数据处理器"""
    
    def __init__(self, name: str):
        self.name = name
        self.created_at = time.time()
        self.process_count = 0
        
    def process(self, data: Dict[str, Any]) -> Dict[str, Any]:
        """处理数据"""
        self.process_count += 1
        
        # 模拟处理逻辑
        processed_data = {
            "original": data,
            "processed_by": self.name,
            "timestamp": time.time(),
            "metrics": {
                "fields": len(data),
                "complexity": self._calculate_complexity(data)
            }
        }
        
        return processed_data
    
    def _calculate_complexity(self, data: Dict[str, Any]) -> float:
        """计算数据复杂度"""
        # 简单示例：基于数据结构深度和字段数量
        complexity = len(data)
        
        for key, value in data.items():
            if isinstance(value, dict):
                complexity += self._calculate_complexity(value) * 0.5
            elif isinstance(value, list):
                complexity += len(value) * 0.3
                
        return complexity
    
    def get_stats(self) -> Dict[str, Any]:
        """获取处理器统计信息"""
        return {
            "name": self.name,
            "uptime": time.time() - self.created_at,
            "process_count": self.process_count
        }
    
    def to_json(self) -> str:
        """转换为JSON字符串"""
        return json.dumps(self.get_stats())

# 测试代码
if __name__ == "__main__":
    processor = DataProcessor("测试处理器")
    
    test_data = {
        "user": {
            "id": 123,
            "name": "张三",
            "tags": ["vip", "active"]
        },
        "order": {
            "id": "ORD-2023-001",
            "items": [
                {"product": "手机", "price": 5999},
                {"product": "耳机", "price": 999}
            ]
        }
    }
    
    result = processor.process(test_data)
    print(f"处理结果: {result}")
    print(f"处理器统计: {processor.to_json()}")
