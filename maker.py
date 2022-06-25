from moviepy.editor import *
from moviepy.video.tools.segmenting import findObjects
from moviepy.video.fx.mirror_x import mirror_x

mode_choose = input("Enter mode(0 - photo; 1 - similar videos; 2 - different videos):")

back = ImageClip("canv3.png")


def choose(mode):
    if mode == "0":
        return photo(back)
    if mode == "1":
        return sim_videos(back)
    if mode == "2":
        return dif_videos(back)


def photo(background_clip):
    img_name = input("Enter image` name:")

    dur = int(input("Enter video` duration(seconds):"))

    image = ImageClip(img_name, duration=dur).subclip()
    left_clip = mirror_x(image.rotate(90))
    right_clip = mirror_x(image.rotate(-90))
    front_clip = mirror_x(image)

    clips = [left_clip, front_clip, right_clip]

    regions = findObjects(background_clip)

    comp_clips = [c.resize(r.size).set_mask(r.mask).set_pos(r.screenpos) for c, r in zip(clips, regions)]

    return CompositeVideoClip(comp_clips, background_clip.size)


def sim_videos(background_clip):
    clip_name = input("Enter video` name:")

    clip = mirror_x(VideoFileClip(clip_name).subclip())
    front = clip
    right = clip.rotate(90)
    left = clip.rotate(-90)

    clips = [left, front, right]

    regions = findObjects(background_clip)

    comp_clips = [c.resize(r.size).set_mask(r.mask).set_pos(r.screenpos) for c, r in zip(clips, regions)]
    cc = CompositeVideoClip(comp_clips, background_clip.size)
    return cc


def dif_videos(background_clip):
    right_side_name = input("Enter right side video` name:")
    left_side_name = input("Enter left side video` name:")
    front_side_name = input("Enter front side video` name:")

    right_clip = mirror_x(VideoFileClip(right_side_name).subclip().rotate(90))
    left_clip = mirror_x(VideoFileClip(left_side_name).subclip().rotate(-90))
    front_clip = mirror_x(VideoFileClip(front_side_name).subclip())

    clips = [right_clip, front_clip, left_clip]

    regions = findObjects(background_clip)

    comp_clips = [c.resize(r.size).set_mask(r.mask).set_pos(r.screenpos) for c, r in zip(clips, regions)]
    cc = CompositeVideoClip(comp_clips, background_clip.size)
    return cc

out_name = input("Enter output file` name:")

choose(mode_choose).write_videofile(out_name, fps=30)
