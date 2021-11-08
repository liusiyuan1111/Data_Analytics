# 03Pandas文件索引

`Pandas` 数据的索引就像一本书的目录，让我们很快地找到想要看的章节，作为大量数据，创建合理的具有业务意义的索引对我们分析数据至关重要。

## 一、认识索引

下图是一个简单的 `DataFrame` 中索引的示例：

![pandas index](https://www.gairuo.com/file/pic/2020/04/pandas_index_01.jpg)

其中：

- 行索引是数据的索引，列索引指向的是一个 `Series`
- `DataFrame` 的索引也是系列形成的 `Series` 的索引
- 建立索引让数据更加直观明确
- 建立索引方便数据处理
- 索引允许重复，但业务上一般不会让它重复

有时一个行和列层级较多的数据会出现多层索引的情况。

## 二、设置索引

之前我们学习了加载数据生成 `DataFrame` 时可以指定索引

```python
data = 'res/team.xlsx'
df = pd.read_excel(data, index_col='name') # 设置索引为 name
df
'''
      team  Q1  Q2  Q3  Q4
name
Liver    E  89  21  24  64
Arry     C  36  37  37  57
Ack      A  57  60  18  84
Eorge    C  93  96  71  78
Oah      D  65  49  61  86
'''
```

如果加载时没有指定索引，我们可以使用 `df.set_index()` 指定：

## 三、数据查询

1. Series数据查询

   类似Python的字典dict

   ```python
   s1 = pd.Series([1, 'a', 5.2, 7], index=['a','b','c','d'])
   s1
   s1['a']
   type(s1['a'])
   s1[['b','a']]
   type(s1[['b','a']])
   ```

   

2. 从DataFrame中查询Series
- 如果只查询一行、一列，返回的是pd.Series

- 如果查询多行、多列，返回的是pd.DataFrame

  ```python
  data = 'res/team.xlsx'
  df = pd.read_excel(data) 
  df
  #查询一列，得到一个Series
  df['Q1']
  type(df['Q1'])
  #查询多列，得到的是DataFrame
  df['Q1','Q2']
  type(df['Q1','Q2'])
  #查询一行，得到的是Series
  df.loc[1]
  type(df.loc[1])
  df.loc['Arry']
  #查询多行，得到的是DataFrame
  df.loc[1:3]
  type(df.loc[1:3])
  ```



## 三、查询方法

Pandas查询数据的几种方法

1. df.loc( )方法，根据标签值查询
2. df.iloc( )方法，根据数字位置查询
3. df.where( )方法
4. df.query( )方法

> 注意:
>
> - 以上查询方法，既适用于行，也适用于列
> - 注意观察降维dataFrame>Series>值
> - df.loc( )既能查询，又能覆盖写入，强烈推荐！

### 0.读取数据

