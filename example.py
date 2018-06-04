from pegga import main
from turtle_recorder import Recorder

with Recorder(main, fps=30) as peg:
    peg.to_video('./media/pegga.mp4')
    peg.to_gif('./media/pegga.gif')