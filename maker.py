from moviepy.editor import *
import moviepy.video.tools.segmenting as seg
import moviepy.video.fx.mirror_x as mir

canvNum = input("Enter frames num (3 or 4): ")
mode = input("Enter 1 for different videos or 0 for one video: ")
canvas = {"3": "canv3.png", "4": "canv4.png"}

backgr = ImageClip(canvas[canvNum])

