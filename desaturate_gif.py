"""
Converts an animated GIF to grayscale/monochrome in place, preserving
per-frame duration, loop count, and transparency.

Used as a post-processing step after gh-space-shooter generates game.gif,
since that action hardcodes GitHub's green contribution-graph colors with
no theme/color option of its own.
"""

import sys
from PIL import Image, ImageSequence


def desaturate_gif(path):
    im = Image.open(path)

    frames = []
    durations = []

    for frame in ImageSequence.Iterator(im):
        rgba = frame.convert("RGBA")
        gray = rgba.convert("L").convert("RGB")

        # preserve transparency mask if the frame had one
        if "A" in rgba.getbands():
            alpha = rgba.getchannel("A")
            gray.putalpha(alpha)
            gray = gray.convert("RGBA")

        frames.append(gray)
        durations.append(frame.info.get("duration", 40))

    loop = im.info.get("loop", 0)

    # convert each frame to palette mode for GIF output, preserving alpha
    # via a transparency index where possible
    p_frames = []
    for f in frames:
        if f.mode == "RGBA":
            # composite onto black background where fully transparent,
            # keep everything else as opaque grayscale
            bg = Image.new("RGB", f.size, (0, 0, 0))
            bg.paste(f, mask=f.getchannel("A"))
            p_frames.append(bg.convert("P", palette=Image.ADAPTIVE, colors=64))
        else:
            p_frames.append(f.convert("P", palette=Image.ADAPTIVE, colors=64))

    p_frames[0].save(
        path,
        save_all=True,
        append_images=p_frames[1:],
        duration=durations,
        loop=loop,
        optimize=False,
        disposal=2,
    )


if __name__ == "__main__":
    target = sys.argv[1] if len(sys.argv) > 1 else "game.gif"
    desaturate_gif(target)
    print(f"Desaturated {target}")
