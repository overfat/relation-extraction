# relation-extraction

蛋白质关系抽取

## 项目结构

```
1. data
2. util
3. model
4. run
5. conf.yaml
```

## 运行

1. 克隆项目

```bash
git clone https://github.com/overfat/relation-extraction.git
```

2. 安装依赖

```bash
pip install -r requirements.txt
```

3. 数据预处理

```bash
python -m run.pre_processing
```

4. 训练

```bash
python -m run.train
```

5. 测试

```bash
python -m run.test
```
