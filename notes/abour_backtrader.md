# Backtrader
> link: https://www.backtrader.com/docu/

运行流程:
- 制定策略
  - 确定潜在的可调参数
  - 实例化您在策略中需要的指标
  - 写下进入/退出市场的逻辑
- 创建Cerebro引擎（西班牙语大脑的意思） 
  - 注入策略
  - 使用cerebro.adddata加载回测数据
  - 执行cerebro.run 
  - 使用cerebro.plot绘制可视化图表