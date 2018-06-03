from pegga import main
from turtle_recorder import Recorder

peg = Recorder(main, fps=30)
peg.record()
peg.to_video('./media/pegga.mp4')
peg.to_gif('./media/pegga.gif')
peg.remove_temp()
