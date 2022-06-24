from moviepy.editor import *
import moviepy.video.tools.segmenting as seg
import moviepy.video.fx.mirror_x as mir

name = input("Enter videos name: ")

clipName = VideoFileClip(name)

def frames4(clip):
    top_clip = mir.mirror_x(clip.subclip())
    right_clip = top_clip.rotate(90)
    left_clip = top_clip.rotate(-90)
    bot_clip = top_clip.rotate(180)

    clips = [left_clip, bot_clip, top_clip, right_clip]

    bckgr = ImageClip("canv4.png")

    reg = seg.findObjects(bckgr)
    #for i in reg:
    #   print(i.screenpos)

    comp_clips = [c.resize(r.size).set_mask(r.mask).set_pos(r.screenpos) for c, r in zip(clips, reg)]
    cc = CompositeVideoClip(comp_clips, bckgr.size)
    return cc

def frames3(clip):
    subClip = mir.mirror_x(clipName.subclip())
    bot_clip = subClip
    right_clip = subClip.rotate(90)
    left_clip = subClip.rotate(-90)

    clips = [left_clip, bot_clip, right_clip]

    bckgr = ImageClip("canv3.png")

    reg = seg.findObjects(bckgr)

    comp_clips = [c.resize(r.size).set_mask(r.mask).set_pos(r.screenpos) for c, r in zip(clips, reg)]
    cc = CompositeVideoClip(comp_clips, bckgr.size)
    return cc

framesNum = input("Enter frames number(3 or 4): ")
res = 0
if framesNum == "4":
    res = frames4(clipName)
if framesNum == "3":
    res = frames3(clipName)
res.write_videofile("out_" + name)