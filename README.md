# agileWave

An agile description for drawing digital waveform or timing diagram, based wavedrom and qt
agileWave旨在提供一种更加便捷的信号时序描述格式，在wavedrom和Qt基础上二次开发，由于部分描述格式和wavedrom语法一致，因此建议读者先初步了解下wavedrom：<https://wavedrom.com/>

## 信号描述格式说明

1. 每行代表1个clock tick
   格式= "[clock周期]->[信号1=信号值],[信号2=信号值-标签];"
   例如：00-> A=1,B=0-b,C=Data0
2. NULL=0代表在前后信号之间添加空白分隔;
3. 某个时钟信号描述为'...'，则表示所有的信号和前一个周期取值相同
4. 如果某个tick没有指定信号的取值，则表示该信号重复前一周期值
5. 画线固定使用：EDGE: [a-b 连线标签],[c-d];
6. HEAD和FOOT表示添加标题和脚注，格式=HEAD/FOOT:[标题]
7. 支持保存波形描述(.txt)和时序图(.svg)

### 示例

HEAD:tick_base_wave test<br>
FOOT:tick_cnt 12<br>
00-> clk=P,A=0,NULL=0,B=1,C=1<br>
01-> A=1-a<br>
02->...<br>
03->D=data0<br>
04->...<br>
05->B=0-b<br>
06->C=1-c<br>
07->C=0-d,D=data1<br>
08->...<br>
EDGE: a-b note,c-d<br>

![示例](https://gitee.com/cc-hook/picture/raw/master/wechat/eg.jpg)
