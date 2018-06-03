# turtle_recorder: turtle动画生成器

`turtle`是python中的一个简单的绘图工具，可以用来画很多有趣的东西（具体用法见[官方文档](https://docs.python.org/3/library/turtle.html)）。

但是，现在`turtle`绘图的动画展示都是基于窗口的，至于录制和转换为视频的过程，仍然是一个空白。

`turtle_recorder`则是对这一空白的弥补。在python和一些工具的帮助下，只需几行代码，就可以把绘图的过程和结果录制进来，转换为`mp4`视频或者`gif`动图。

## 适用Python版本

- Python 3.6
- Python 2.7 （不太确定，如果出现问题请提issue）

## 安装

1. `git clone`或者下载为`zip`
2. 安装依赖的python库：`numpy`, `matplotlib`, `PIL`
  
   ```
   pip install -r requirements.txt
   ```
3. 安装[Ghostscript](https://www.ghostscript.com/download/gsdnld.html)并添加到PATH环境变量中（Windows操作，Linux及Mac OS应该有类似操作，欢迎补充）
4. 转换为视频：安装[ffmpeg](http://ffmpeg.org/download.html)并添加到PATH环境变量
5. 转换为gif：安装[ImageMagick](http://www.imagemagick.org/script/download.php)并添加到PATH环境变量

## 使用

代码样例见`example.py`，核心代码如下：

```
from pegga import main # 导入原来画图的函数，注意要删去末尾的done()或turtle.done()
from turtle_recorder import Recorder

peg = Recorder(main, fps=30) # 参数fps为每秒帧数
peg.record() # 捕获并保存动画
peg.to_video('./media/pegga.mp4') # 生成mp4视频
peg.to_gif('./media/pegga.gif') # 生成gif动图
peg.remove_temp() # 清除缓存
```

执行完成后，在对应目录（此例中是`./media`文件夹）查看结果。


## 效果

![Pegga Pig](./demo/pegga.gif)

## 可能的问题

视频或动图的生成时间可能较长，如果没有报错，请耐心等待。

如果使用过程有问题或报错，请先检查是否安装好对应的工具，然后在issue中提出。

## 致谢

在此感谢StackOverflow社区中[该问题](https://stackoverflow.com/questions/41319971/is-there-a-way-to-save-turtles-drawing-as-an-animated-gif/41353016#41353016)下的答案，这给予了我绘图捕获过程中的部分启发。

展示动画（小猪佩奇）代码`pegga.py`来自[Monster12138/-](https://github.com/Monster12138/-)，在此表示感谢。

本项目基于MIT License开源。（查看`LICENSE`文件获取更多信息）

