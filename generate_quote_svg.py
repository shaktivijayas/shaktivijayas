import random
import textwrap
import sys

QUOTES = [
    ("If you don't like your destiny, don't accept it. Instead, have the courage to change it the way you want it to be.", "Naruto Uzumaki"),
    ("I'll leave tomorrow's problems to tomorrow's me.", "Saitama"),
    ("A dropout will beat a genius through hard work.", "Rock Lee"),
    ("It's more important to master the cards you're holding than to complain about the ones your opponent was dealt.", "Grimsley"),
    ("Not giving up on yourself is what's truly important. That way you don't end up pathetic.", "Reiko Mikami"),
    ("Reject common sense to make the impossible possible.", "Simon"),
    ("How can you move forward if you keep regretting the past?", "Edward Elric"),
    ("Don't live your life making up excuses. The one making your choices is yourself!", "Mugen"),
    ("If you don't take risks, you can't create a future!", "Monkey D. Luffy"),
    ("If your life can change once, your life can change again.", "Sanae Furukawa"),
    ("Being weak is nothing to be ashamed of... Staying weak is!!!", "Fuegoleon Vermillion"),
]

WRAP_WIDTH = 58
LINE_HEIGHT = 26
FONT_SIZE = 18
AUTHOR_FONT_SIZE = 15
PADDING_TOP = 40
PADDING_BOTTOM = 34
SVG_WIDTH = 760

def build_svg(text_color, filename, seed_index):
    quote, author = QUOTES[seed_index]
    lines = textwrap.wrap(f'“{quote}”', width=WRAP_WIDTH)
    height = PADDING_TOP + len(lines) * LINE_HEIGHT + PADDING_BOTTOM

    tspans = "\n".join(
        f'    <tspan x="50%" dy="{0 if i == 0 else LINE_HEIGHT}">{line}</tspan>'
        for i, line in enumerate(lines)
    )

    svg = f'''<svg xmlns="http://www.w3.org/2000/svg" width="{SVG_WIDTH}" height="{height}" viewBox="0 0 {SVG_WIDTH} {height}">
  <style>
    .quote {{ font: italic 400 {FONT_SIZE}px 'Segoe UI', ui-sans-serif, sans-serif; fill: {text_color}; }}
    .author {{ font: 600 {AUTHOR_FONT_SIZE}px 'Segoe UI', ui-sans-serif, sans-serif; fill: {text_color}; opacity: 0.75; }}
  </style>
  <text text-anchor="middle" class="quote" x="50%" y="{PADDING_TOP}">
{tspans}
  </text>
  <text text-anchor="middle" class="author" x="50%" y="{PADDING_TOP + len(lines) * LINE_HEIGHT + 24}">— {author}</text>
</svg>
'''
    with open(filename, "w", encoding="utf-8") as f:
        f.write(svg)

if __name__ == "__main__":
    idx = random.randrange(len(QUOTES))
    build_svg("#e6e6e6", "quote-dark.svg", idx)
    build_svg("#1a1a1a", "quote-light.svg", idx)
    print(f"Generated quote {idx}: {QUOTES[idx][1]}")
