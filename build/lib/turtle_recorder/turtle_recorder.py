from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

from turtle import *
import os
import shutil

class Recorder(object):
    def __init__(self, func, fps=30):
        self.func = func
        self.fps = fps
    def __enter__(self):
        self.record()
        return self
    def __exit__(self, type, value, traceback):
        self.remove_temp()
    def draw(self):
        self.func()
        ontimer(self.stop, 500)
    def stop(self):
        self.running = False
    def save_eps(self, counter=[1]):
        if not os.path.exists('tmp'):
            os.mkdir('tmp')
        getcanvas().postscript(file='./tmp/{0:03d}.eps'.format(counter[0]))
        counter[0] += 1
        if self.running:
            ontimer(self.save_eps, int(1000 / self.fps))
    def save_animation(self):
        print('Capturing animation: Please close the window when the animation ends.')
        self.running = True
        self.save_eps()
        ontimer(self.draw, 500)
        done()
        self.frames = len(os.listdir('./tmp'))
        print('Captured frames: {}'.format(self.frames))
    def load_animation(self):
        import matplotlib.pyplot as plt
        from matplotlib import animation

        fig = plt.figure()
        plt.axis('off')
        plt.subplots_adjust(left=0, bottom=0, right=1, top=1)
        img = plt.imread('./tmp/001.eps')
        plt.imshow(img)

        # plt.show()

        def init():
            img = plt.imread('./tmp/001.eps')
            return img

        def animate(i):
            filename = './tmp/{0:03d}.eps'.format(i + 1)
            plt.clf()
            plt.axis('off')
            plt.subplots_adjust(left=0, bottom=0, right=1, top=1)
            img = plt.imread(filename)
            plt.imshow(img)
            return img
        
        self.animation = animation.FuncAnimation(fig, animate, init_func=init, frames=self.frames, interval=1000 / self.fps)
        print('Animation loaded. Prepare to generate video/gif...')
    def remove_temp(self):
        shutil.rmtree('./tmp')
    def record(self):
        self.save_animation()
        self.load_animation()
        # self.remove_temp()
    def to_video(self, output):
        print('Generating video...')
        self.animation.save(output, fps=self.fps, extra_args=['-vcodec', 'libx264'])
        print('Video generated successfully.')
    def to_gif(self, output):
        print('Generating gif...')
        self.animation.save(output, writer='imagemagick')
        print('Gif generated successfully.')


        
    