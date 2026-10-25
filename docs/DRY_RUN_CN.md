# Freqtrade Dry-Run 门控验证 (新手傻瓜版)

### 目标
验证 `regime.json` 的方向锁在实盘环境真的生效，不是只在回测里。

### 1. 安装 freqtrade (Docker 最稳)
```bash
git clone https://github.com/freqtrade/freqtrade.git
cd freqtrade
docker-compose build
```

### 2. 把 RegimeGate 放进去
```bash
cp -r ~/Desktop/regime-gate-skill/execution/RegimeGateStrategy.py ./user_data/strategies/
cp ~/Desktop/regime-gate-skill/configs/dry_run_config.json ./user_data/
```

### 3. 生成 regime.json
```bash
cd ~/Desktop/regime-gate-skill
python3 gate/runner.py
cat regime.json
# 应该有 bias: long, allowed: long_only, ttl_hours: 26
```

### 4. 启动 dry-run
```bash
cd freqtrade
docker-compose run --rm freqtrade trade --config user_data/dry_run_config.json --strategy RegimeGateStrategy --dry-run
```

### 5. 验证点
- 日志里 `allowed: long_only` 时，只有多单，没有空单
- 删除 `regime.json` 后，策略应该不进新单 (expired -> HARD_CLOSE)
- 26小时后 `regime.json` 过期，应该 SOFT_CLOSE

### 6. 常见问题
- 没数据: `docker-compose run --rm freqtrade download-data --config user_data/dry_run_config.json --days 30`
- 权限: `chmod +x gate/runner.py`
