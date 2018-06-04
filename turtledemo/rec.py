from yinyang import main
from turtle_recorder import Recorder

with Recorder(main, fps=30) as rec:
    rec.to_video('./media/yinyang.mp4')