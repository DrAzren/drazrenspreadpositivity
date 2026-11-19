#!/usr/bin/env python3
"""Ep002 v2 composer: writes src/index.src.html from a scene spec (DoodleVerse V2).

Rules baked in: every character is a FULL-BODY sprite standing on a drawn floor (feet visible),
or behind a fully drawn prop; Dr. Azren always uses a viseme rig (text-driven lip-sync + blinks);
props carry cyan/yellow offset marker shadows; every scene has a set, a doodle confetti layer and
draw-on accents. Run, then: python3 ../../tools/build_doodleverse.py .. --duration 85.3
"""
import json, math, os, random

HERE = os.path.dirname(os.path.abspath(__file__))
IMG = "assets/img/v2"
RIGS = json.load(open(os.path.join(HERE, IMG, "vis", "rigs.json")))
FLOOR = 1735
SIZES = {  # native sprite sizes (px)
    "drazren_think": (334, 1154), "drazren_point_marker": (366, 1144), "drazren_clipboard": (340, 1139),
    "drazren_welcome": (522, 1142), "drazren_wave": (350, 1145),
    "amir_low": (364, 1245), "amir_relieved": (448, 1301), "meiling_relieved": (407, 1254),
    "divya_relieved": (414, 1287), "pakrahman_relieved": (430, 1290), "danish_relieved": (418, 1285),
    "kakros_relieved": (370, 1241),
    "bed_messy": (653, 382), "desk_laptop": (632, 436), "guitar_dusty": (405, 484), "plant_wilted": (402, 417),
    "plant_bloom": (483, 455), "window_rain": (651, 420), "alarm_clock": (365, 466),
    "stepping_stones": (661, 431), "park_bench": (667, 401),
}
TWEENS = []


def tw(s):
    TWEENS.append(s)


# ---------------------------------------------------------------- sprites & rigs
def sprite(id_, name, cx, feet, s, cls="spr", style=""):
    """Full-body sprite, bottom-centre at (cx, feet)."""
    w, h = SIZES[name]
    W, H = w * s, h * s
    return (f'<img id="{id_}" class="{cls}" src="{IMG}/{name}.png" '
            f'style="left:{cx - W / 2:.0f}px;top:{feet - H:.0f}px;width:{W:.0f}px;{style}">')


def prop(id_, name, x, y, s, extra=""):
    w, h = SIZES[name]
    return f'<img id="{id_}" class="prop" src="{IMG}/{name}.png" style="left:{x}px;top:{y}px;width:{w * s:.0f}px;{extra}">'


def rig(id_, pose, cx, feet, s, mirror=False, extra_cls=""):
    """Dr. Azren viseme rig: pose + 6 mouth patches + eyelids. Lip-sync via data-v, blinks via data-b."""
    w, h = SIZES[pose]
    r = RIGS[pose]
    W, H = w * s, h * s
    m = r["mouth"]
    tf = f"translateX({W:.1f}px) scale({-s},{s})" if mirror else f"scale({s})"
    mouths = "".join(
        f'<img class="mo v{k}" src="{IMG}/vis/{pose}/mouth_{n}.png" style="left:{m["x"]}px;top:{m["y"]}px;width:{m["w"]}px">'
        for k, n in (("R", "rest"), ("A", "A"), ("E", "E"), ("O", "O"), ("M", "M"), ("N", "neutral")))
    er = r["eye_r"]; ang = r["angle"]
    lids = "".join(
        f'<g transform="rotate({ang} {e["x"]} {e["y"]})"><ellipse cx="{e["x"]}" cy="{e["y"]}" rx="{er * 1.05:.1f}" ry="{er * .95:.1f}" fill="{e["skin"]}"/>'
        f'<path d="M{e["x"] - er:.1f},{e["y"] + 2:.1f} q{er:.1f},{er * .55:.1f} {2 * er:.1f},0" stroke="#17161a" stroke-width="5" fill="none" stroke-linecap="round"/></g>'
        for e in r["eyes"])
    return (f'<div id="{id_}" class="rig {extra_cls}" data-talk="1" data-v="R" data-b="0" '
            f'style="left:{cx - W / 2:.0f}px;top:{feet - H:.0f}px;width:{W:.0f}px;height:{H:.0f}px">'
            f'<div class="rs" style="transform:{tf}"><img src="{IMG}/{pose}.png" style="left:0;top:0;width:{w}px">{mouths}'
            f'<svg class="lid" width="{w}" height="400" style="position:absolute;left:0;top:0;overflow:visible">{lids}</svg></div></div>')


# ---------------------------------------------------------------- doodles (marker style SVG)
def sparkle(x, y, s=50, c="#ffd43b"):
    return f'<use href="#sparkle" x="{x}" y="{y}" width="{s}" height="{s}" style="fill:{c}"/>'


def star(x, y, s=50, c="star"):
    return f'<use href="#{c}" x="{x}" y="{y}" width="{s}" height="{s}"/>'


def heart(x, y, s=60):
    return f'<use href="#heart" x="{x}" y="{y}" width="{s}" height="{s * .92:.0f}"/>'


def confetti(seed, n=26, y0=180, y1=1720, op=.55):
    rnd = random.Random(seed)
    cols = ["#ffd43b", "#3cc4e6", "#f08cb4", "#8f6cf0", "#ff9f2e", "#2fae9e"]
    out = []
    for i in range(n):
        x, y = rnd.uniform(30, 1050), rnd.uniform(y0, y1)
        k = rnd.random(); c = rnd.choice(cols)
        if k < .3:
            out.append(f'<circle cx="{x:.0f}" cy="{y:.0f}" r="{rnd.uniform(5, 10):.0f}" fill="{c}"/>')
        elif k < .5:
            out.append(sparkle(x - 18, y - 18, rnd.uniform(26, 44)))
        elif k < .7:
            a = rnd.uniform(0, 6.28)
            out.append(f'<path d="M{x:.0f},{y:.0f} q{18 * math.cos(a):.0f},{-14:.0f} {30 * math.cos(a):.0f},{10 * math.sin(a):.0f}" stroke="{c}" stroke-width="7" fill="none" stroke-linecap="round"/>')
        elif k < .85:
            out.append(f'<path d="M{x:.0f},{y:.0f} c10,-14 26,-4 16,8 c-8,10 -22,-2 -12,-12" stroke="{c}" stroke-width="5" fill="none" stroke-linecap="round"/>')
        else:
            out.append(f'<path d="M{x - 9:.0f},{y:.0f} l18,0 M{x:.0f},{y - 9:.0f} l0,18" stroke="{c}" stroke-width="6" stroke-linecap="round"/>')
    return f'<g opacity="{op}" filter="url(#wob)">{"".join(out)}</g>'


def floor_line(y=FLOOR, c="#17161a"):
    return (f'<path d="M30,{y + 8} C250,{y - 4} 520,{y + 12} 760,{y + 2} S1000,{y + 6} 1050,{y}" stroke="{c}" stroke-width="7" fill="none" stroke-linecap="round"/>'
            f'<path d="M60,{y + 30} l40,0 M180,{y + 26} l60,0 M420,{y + 34} l50,0 M700,{y + 28} l70,0 M900,{y + 32} l40,0" stroke="#b9bcc2" stroke-width="6" stroke-linecap="round"/>')


def shadow(cx, w, y=FLOOR):
    return f'<ellipse cx="{cx}" cy="{y + 4}" rx="{w / 2:.0f}" ry="16" fill="rgba(23,22,26,.13)"/>'


def note(id_, x, y, w, h, color, text, size=40, rot=-3, tape="#3cc4e6"):
    return (f'<div id="{id_}" class="note" style="left:{x}px;top:{y}px;width:{w}px;height:{h}px;opacity:0">'
            f'<div class="note-in" style="background:{color};transform:rotate({rot}deg);font-size:{size}px">'
            f'<span class="tape" style="background:{tape}"></span>{text}</div></div>')


def bubble(id_, x, y, w, text, size=34, tail="left", color="#fff"):
    t = "left:34px" if tail == "left" else "right:34px"
    return (f'<div id="{id_}" class="bub" style="left:{x}px;top:{y}px;width:{w}px;opacity:0">'
            f'<div class="bub-in" style="font-size:{size}px;background:{color}">{text}<i style="{t}"></i></div></div>')


def tree(x, y, s=1.0, c="#7dc96b"):
    return (f'<g transform="translate({x},{y}) scale({s})"><path d="M-14,0 L-10,-170 L10,-170 L14,0Z" fill="#a8693a" class="ink5"/>'
            f'<path d="M0,-150 c-90,10 -120,-70 -70,-110 c-30,-70 60,-110 90,-70 c50,-50 130,0 100,60 c60,30 30,120 -40,110 c-20,20 -60,20 -80,10z" fill="{c}" class="ink"/>'
            f'<path d="M0,-150 c-90,10 -120,-70 -70,-110 c-30,-70 60,-110 90,-70 c50,-50 130,0 100,60 c60,30 30,120 -40,110 c-20,20 -60,20 -80,10z" fill="url(#hatch)"/></g>')


def flower(x, y, c="#f08cb4"):
    return (f'<g><path d="M{x},{y} l0,-46" class="ink5"/><circle cx="{x}" cy="{y - 52}" r="15" fill="{c}" class="ink5"/>'
            f'<circle cx="{x}" cy="{y - 52}" r="5" fill="#ffd43b"/><path d="M{x},{y - 20} q14,-10 22,-2" stroke="#2f9e57" stroke-width="5" fill="none"/></g>')


def bird(x, y, s=1):
    return f'<path d="M{x},{y} q{12 * s},{-12 * s} {24 * s},0 q{12 * s},{-12 * s} {24 * s},0" stroke="#17161a" stroke-width="5" fill="none" stroke-linecap="round"/>'


def sun(x, y, r=70):
    rays = "".join(f'<path d="M{x + (r + 14) * math.cos(a):.0f},{y + (r + 14) * math.sin(a):.0f} l{22 * math.cos(a):.0f},{22 * math.sin(a):.0f}" class="ink5"/>'
                   for a in [i * math.pi / 4 for i in range(8)])
    return f'<g><circle cx="{x}" cy="{y}" r="{r}" fill="#ffd43b" class="ink"/><circle cx="{x}" cy="{y}" r="{r}" fill="url(#hatch)" opacity=".5"/>{rays}</g>'


def cloud(x, y, w=300, c="#fff"):
    h = w * 0.5
    return f'<use href="#cloudw" x="{x}" y="{y}" width="{w}" height="{h:.0f}" style="fill:{c}"/>'


def grass(y=FLOOR - 40):
    return (f'<path d="M-20,{y} C200,{y - 30} 420,{y + 10} 620,{y - 14} S960,{y - 20} 1100,{y} L1100,1940 L-20,1940Z" fill="#9ad67a" class="ink"/>'
            f'<path d="M-20,{y} C200,{y - 30} 420,{y + 10} 620,{y - 14} S960,{y - 20} 1100,{y} L1100,1940 L-20,1940Z" fill="url(#hatch)" opacity=".6"/>'
            + "".join(f'<path d="M{x},{y + 40} l6,-22 l6,22 l6,-18" stroke="#2f9e57" stroke-width="5" fill="none" stroke-linecap="round"/>' for x in range(40, 1080, 110)))


def hl(id_, top, size, html, start_hidden=True):
    op = "opacity:0;" if start_hidden else ""
    return f'<div id="{id_}" class="hl" style="top:{top}px;font-size:{size}px;{op}">{html}</div>'


# ---------------------------------------------------------------- scenes
def scene(id_, start, dur, body, track):
    return f'<div id="{id_}" class="clip scene" data-start="{start}" data-duration="{dur}" data-track-index="{track}"><div id="{id_}-cam" class="cam">{body}</div></div>'


S = []

# S1 HOOK 0-4.2 : Amir + the guitar he loved, colour drains
S.append(scene("s1", 0, 4.2, f"""
<svg class="svgl" width="1080" height="1920">{confetti(1, 18)}<g filter="url(#wob)">
 <rect x="560" y="500" width="300" height="230" rx="10" fill="#fff" class="ink"/><rect x="580" y="520" width="260" height="190" fill="#dff3fb"/>
 <g id="s1-photo"><path d="M650,690 l0,-80 l60,-20 l0,80" class="ink5" fill="none"/><circle cx="640" cy="690" r="16" fill="#8f6cf0" class="ink5"/><circle cx="700" cy="670" r="16" fill="#8f6cf0" class="ink5"/>
 <circle cx="780" cy="600" r="30" fill="#ffd43b" class="ink5"/></g>
 <path d="M700,500 l10,-26 l10,26" class="ink5" fill="none"/>
 <rect x="60" y="610" width="300" height="18" rx="4" fill="#a8693a" class="ink5"/>
 <rect x="80" y="530" width="34" height="80" fill="#f25f5c" class="ink5"/><rect x="118" y="545" width="30" height="65" fill="#2d9cdb" class="ink5"/><rect x="152" y="520" width="38" height="90" fill="#ffd43b" class="ink5"/>
 <rect x="194" y="550" width="28" height="60" fill="#18a999" class="ink5"/><path d="M240,610 l44,-70 l20,10 l-40,62z" fill="#8f6cf0" class="ink5"/>
 {floor_line()}{shadow(320, 260)}{shadow(830, 360)}
</g></svg>
{hl("s1-h1", 190, 116, "DULU SUKA,", False)}{hl("s1-h2", 318, 116, 'KINI <span id="s1-kosong">KOSONG?</span>', False)}
{sprite("s1-amir", "amir_low", 320, FLOOR, .8)}
<div id="s1-gc" class="abs" style="left:600px;top:1251px">{prop("s1-guitar", "guitar_dusty", 0, 0, 1.0)}</div>
<div id="s1-gg" class="abs grey" style="left:600px;top:1251px;opacity:0">{prop("s1-guitar-g", "guitar_dusty", 0, 0, 1.0)}</div>
<svg class="svgl" width="1080" height="1920"><g id="s1-notes" filter="url(#wob)">
 <use href="#music" x="620" y="900" width="120" height="120"/><use href="#music" x="860" y="840" width="100" height="100"/><use href="#music" x="760" y="1020" width="80" height="80"/>
 {sparkle(940, 980, 50)}{sparkle(600, 1080, 40)}{star(980, 760, 48)}
</g>
<g id="s1-cloud" opacity="0" filter="url(#wob)"><use href="#cloud" x="150" y="560" width="340" height="180"/>
 <use href="#drop" x="210" y="740" width="34" height="52"/><use href="#drop" x="290" y="758" width="34" height="52"/><use href="#drop" x="380" y="744" width="34" height="52"/></g>
<path id="s1-arrow" class="draw" pathLength="1" d="M470,640 C560,560 640,560 700,600" stroke="#2d9cdb" stroke-width="7" fill="none" stroke-linecap="round" opacity="0"/>
</svg>
""", 1))
tw('cam("#s1-cam",0,4.2,1.0,1.045);')
tw('tl.fromTo("#s1-h1",{scale:.94},{scale:1,duration:.35,ease:"back.out(2)"},0);tl.fromTo("#s1-h2",{scale:.94},{scale:1,duration:.35,ease:"back.out(2)"},.08);')
tw('floaty("#s1-notes",0,2.7,12);tl.to("#s1-notes",{opacity:0,y:-40,duration:.5},2.7);')
tw('tl.to("#s1-gg",{opacity:1,duration:.7},2.75);tl.to("#s1-photo",{filter:"grayscale(1)",duration:.6},2.75);')
tw('tl.set("#s1-arrow",{opacity:1},1.0);draw("#s1-arrow",1.0,.7);')
tw('tl.fromTo("#s1-cloud",{opacity:0,y:-30},{opacity:1,y:0,duration:.5,ease:"power2.out"},2.9);')
tw('tl.to("#s1-kosong",{color:"#6d7076",textShadow:"-7px 6px 0 #c3c6cb, 7px 9px 0 #dfe1e4",duration:.5},3.5);')
tw('tl.fromTo("#s1-amir",{rotation:0},{rotation:-1.2,duration:2.4,ease:"sine.inOut",transformOrigin:"50% 100%"},1.6);')

# S2 BEDROOM 4.2-13.7
bubbles = (bubble("s2-b1", 600, 900, 300, "Jom lunch? 🍜".replace(" 🍜", ""), 34) +
           bubble("s2-b2", 640, 1010, 300, "Okay tak, Amir?", 32) +
           bubble("s2-b3", 600, 1120, 260, "Amir??", 34))
S.append(scene("s2", 4.2, 9.5, f"""
<svg class="svgl" width="1080" height="1920">{confetti(2, 16)}<g filter="url(#wob)">
 <rect x="600" y="826" width="260" height="16" rx="4" fill="#a8693a" class="ink5"/>
 {floor_line()}{shadow(240, 240)}{shadow(640, 640)}
</g></svg>
<div id="s2-win" class="abs" style="left:40px;top:470px">{prop("s2-window", "window_rain", 0, 0, .85)}</div>
<svg id="s2-rain" class="svgl" width="1080" height="1920" style="clip-path:inset(500px 520px 1110px 120px)"><g stroke="#cfe7f7" stroke-width="5" stroke-linecap="round">
 {"".join(f'<path d="M{x},{y} l-10,34"/>' for x, y in [(160,520),(230,560),(300,530),(380,570),(450,540),(200,640),(330,660),(420,700),(260,740),(480,640)])}
</g></svg>
<svg class="svgl" width="1080" height="1920"><g id="s2-sky" opacity="0"><circle cx="250" cy="760" r="42" fill="#ffd43b" stroke="#17161a" stroke-width="6"/></g>
<g id="s2-moon" opacity="0"><path d="M300,620 a50,50 0 1,0 30,86 a40,40 0 1,1 -30,-86z" fill="#fff6c9" stroke="#17161a" stroke-width="6"/></g></svg>
{prop("s2-bed", "bed_messy", 270, 1277, 1.2)}
<div id="s2-clock" class="abs" style="left:640px;top:632px">{prop("s2-clock-i", "alarm_clock", 0, 0, .42)}</div>
{sprite("s2-amir", "amir_low", 180, FLOOR, .8)}
<svg class="svgl" width="1080" height="1920"><g filter="url(#wob)">
 <g id="s2-ugh" opacity="0"><use href="#cloud" x="40" y="610" width="280" height="150"/><text x="110" y="700" font-family="DV Hand" font-size="40" fill="#fff">letih...</text></g>
 <g id="s2-bowl" opacity="0"><circle cx="420" cy="740" r="78" fill="#fff" stroke="#ff6b5e" stroke-width="7" stroke-dasharray="14 12"/>
  <path d="M362,734 q58,70 116,0z" fill="#f7e9cc" class="ink5"/><path d="M362,734 l116,0" class="ink5"/><path d="M372,722 q48,-30 96,0" fill="#fff" class="ink5"/>
  <path d="M470,690 l40,-40 M480,700 l40,-38" class="ink5"/><text x="458" y="690" font-family="DV Marker" font-size="50" fill="#8f6cf0" stroke="#17161a" stroke-width="2">?</text></g>
 <g id="s2-phone" opacity="0"><rect x="560" y="1330" width="150" height="80" rx="12" fill="#3e4962" class="ink5" transform="rotate(-8 635 1370)"/>
  <rect x="574" y="1342" width="122" height="56" rx="6" fill="#dff3fb" transform="rotate(-8 635 1370)"/></g>
</g></svg>
{bubbles}
{hl("s2-hl", 190, 104, "HARI DEMI HARI...")}
<div id="s2-3am" class="hand" style="left:612px;top:860px;font-size:46px;opacity:0"><span class="u-y">3:00 pagi</span></div>
""", 2))
tw('cam("#s2-cam",4.2,9.5,1.0,1.05);')
tw('tl.fromTo("#s2-amir",{opacity:0,x:-40},{opacity:1,x:0,duration:.35,ease:"power3.out"},4.2);')
tw('floaty("#s2-rain",4.2,9.4,30);')
tw('tl.fromTo("#s2-sky",{opacity:0,y:60},{opacity:1,y:0,duration:.8},4.36);pop("#s2-ugh",4.8,.35);')
tw('tl.to("#s2-ugh",{opacity:0,duration:.25},6.0);pop("#s2-bowl",6.23,.35);tl.to("#s2-bowl",{opacity:0,duration:.25},7.6);')
tw('tl.fromTo("#s2-clock",{rotation:-5},{rotation:5,duration:.06,yoyo:true,repeat:11,transformOrigin:"50% 100%"},7.78);rise("#s2-3am",7.8,.3);fade("#s2-3am",8.95,.2);')
tw('pop("#s2-phone",9.05,.3);')
for i, t in enumerate([9.1, 9.5, 9.9]):
    tw(f'tl.fromTo("#s2-b{i + 1}",{{opacity:0,y:40}},{{opacity:1,y:0,duration:.3,ease:"back.out(1.7)"}},{t});')
tw('tl.to(["#s2-b1","#s2-b2","#s2-b3"],{filter:"grayscale(1)",opacity:.55,duration:.5},10.6);')
tw('slam("#s2-hl",10.96,-1);tl.to("#s2-sky",{opacity:0,duration:.25},11.3);tl.to("#s2-moon",{opacity:1,duration:.25},11.4);'
   'tl.to("#s2-moon",{opacity:0,duration:.25},12.0);tl.to("#s2-sky",{opacity:1,duration:.25},12.1);'
   'tl.to("#s2-sky",{opacity:0,duration:.25},12.7);tl.to("#s2-moon",{opacity:1,duration:.25},12.8);')
tw('tl.fromTo("#s2-cam",{filter:"grayscale(0)"},{filter:"grayscale(0.75)",duration:2.0},11.4);')

# S3 DOCTOR 13.7-27.6 : sun/moon timeline, life notes, think -> clipboard
nodes = []
for i in range(14):
    r, c = divmod(i, 7)
    x, y = 100 + c * 88, 560 + r * 150
    nodes.append(f'<g id="n{i + 1}"><circle cx="{x}" cy="{y}" r="36" fill="#fff" class="ink5"/>'
                 f'<circle id="n{i + 1}f" cx="{x}" cy="{y}" r="26" fill="#ffd43b"/></g>')
S.append(scene("s3", 13.7, 13.9, f"""
<svg class="svgl" width="1080" height="1920">{confetti(3, 18)}<g filter="url(#wob)">{floor_line()}{shadow(905, 300)}</g></svg>
{hl("s3-hl1", 190, 96, 'SEDIH ITU <span class="t">NORMAL</span>...')}
{hl("s3-hl2", 180, 100, 'KEMURUNGAN<br><span class="t">MAJOR?</span>')}
<div id="s3-norm" class="abs" style="left:70px;top:470px;width:560px;opacity:0">
 <svg width="560" height="300" style="overflow:visible"><g filter="url(#wob)">{sun(330, 110, 64)}<use href="#cloudw" x="60" y="110" width="320" height="160" style="fill:#fff"/></g></svg>
 <div class="hand" style="left:40px;top:280px;font-size:52px;color:#11897b"><span class="u-y">sekali-sekala ✓</span></div></div>
<svg id="s3-tl" class="svgl" width="1080" height="1920" style="opacity:0"><g filter="url(#wob)">
 <path d="M100,560 L628,560 M100,710 L628,710" stroke="#2d9cdb" stroke-width="6" stroke-dasharray="14 12" fill="none"/>
 {"".join(nodes)}
 <text x="100" y="500" font-family="DV Hand" font-size="40" fill="#17161a">hari 1</text><text x="560" y="500" font-family="DV Hand" font-size="40" fill="#17161a">hari 7</text>
</g></svg>
{hl("s3-2w", 790, 92, "2 MINGGU+").replace('class="hl"', 'class="hl" data-w="1"').replace('style="top', 'style="left:40px;width:640px;top')}
<div id="s3-hampir" class="hand" style="left:80px;top:900px;font-size:44px;opacity:0"><span class="u-y">hampir setiap hari</span></div>
{note("s3-k1", 60, 990, 190, 120, "#ffd43b", "KERJA", 36, -5)}{note("s3-k2", 262, 980, 210, 130, "#f08cb4", "KELUARGA", 32, 3, "#ffd43b")}{note("s3-k3", 484, 992, 180, 118, "#9ad67a", "KAWAN", 36, -2, "#f08cb4")}
<svg class="svgl" width="1080" height="1920"><g id="s3-cracks" opacity="0" stroke="#e2382f" stroke-width="6" fill="none" stroke-linecap="round" filter="url(#wob)">
 <path d="M150,1000 l-14,40 l22,20 l-12,40"/><path d="M370,990 l14,36 l-20,24 l10,44"/><path d="M570,1004 l-10,40 l20,22"/></g></svg>
{rig("s3-doc", "drazren_think", 905, FLOOR, .87, mirror=True)}
{rig("s3-doc2", "drazren_clipboard", 905, FLOOR, .87, extra_cls="hide")}
{bubble("s3-sah", 300, 1105, 470, "Hanya doktor boleh sahkan ✓", 38, "right", "#e9faf6")}
<svg class="svgl" width="1080" height="1920"><g id="s3-burst" opacity="0" filter="url(#wob)">{sparkle(780, 760, 70)}{star(1010, 820, 50)}{sparkle(990, 650, 46, "#3cc4e6")}{heart(760, 900, 50)}</g></svg>
""", 3))
tw('tl.fromTo("#s3-doc",{x:-60,opacity:0},{x:0,opacity:1,duration:.45,ease:"power2.out"},13.72);bob("#s3-doc",14.3,11.5,1.4);')
tw('slam("#s3-hl1",13.87,-1);rise("#s3-norm",13.95,.45);fade(["#s3-norm","#s3-hl1"],16.0,.3);')
tw('rise("#s3-tl",16.1,.4);')
for i in range(14):
    t = 17.0 + 4.9 * (i / 13) ** 0.8
    tw(f'tl.to("#n{i + 1}f",{{fill:"#9aa0a8",duration:.12}},{t:.2f});')
tw('rise("#s3-hampir",19.65,.35);slam("#s3-2w",21.9,-3);')
tw('rise("#s3-k1",22.85,.3);rise("#s3-k2",23.05,.3);rise("#s3-k3",23.25,.3);tl.to("#s3-cracks",{opacity:1,duration:.2},23.5);')
tw('slam("#s3-hl2",24.86,-1);cam("#s3-cam",24.8,2.8,1.0,1.03);')
tw('pop("#s3-burst",25.85,.35);tl.to("#s3-burst",{opacity:0,duration:.3},26.6);tl.set("#s3-doc",{opacity:0},25.98);tl.set("#s3-doc2",{opacity:1},25.98);')
tw('tl.fromTo("#s3-sah",{opacity:0,scale:.8},{opacity:1,scale:1,duration:.3,ease:"back.out(2)"},26.12);')


# S4 PARK METAPHOR 27.6-37.0 (colour world + grey copy wiped in; plant wilts)
def park_world(grey):
    plant = "plant_wilted" if grey else "plant_bloom"
    return f"""<svg class="svgl" width="1080" height="1920"><g filter="url(#wob)">
 {sun(900, 560, 76)}{cloud(120, 470, 300)}{cloud(560, 600, 220)}{bird(400, 520)}{bird(470, 560, .8)}{bird(700, 500, .9)}
 {tree(150, 1300, 1.2)}{tree(960, 1250, 1.0, "#5fbf6a")}
 {grass()}{flower(80, 1700)}{flower(1000, 1690, "#8f6cf0")}{flower(560, 1720, "#ffd43b")}{shadow(855, 280)}
</g></svg>
{prop("s4-bench" + ("g" if grey else ""), "park_bench", 40, 1314, 1.05)}
{prop("s4-plant" + ("g" if grey else ""), plant, 30, 1458 if not grey else 1450, .6)}
{sprite("s4-amir" + ("g" if grey else ""), "amir_low", 855, FLOOR, .8)}"""


S.append(scene("s4", 27.6, 9.4, f"""
<div id="s4-col" class="abs" style="left:0;top:0;width:1080px;height:1920px">{park_world(False)}</div>
<div id="s4-grey" class="abs rv grey" style="left:0;top:0;width:1080px;height:1920px;--rv:100%">{park_world(True)}</div>
{hl("s4-hl", 190, 104, 'DUNIA JADI<br><span id="s4-kelabu">KELABU...</span>')}
<svg id="s4-wave" class="svgl" width="1080" height="1920" style="opacity:0"><g filter="url(#wob)">
 <path d="M60,300 C20,700 100,1100 40,1760" stroke="#8d9096" stroke-width="26" fill="none" stroke-linecap="round" opacity=".7"/>
 <path d="M110,260 C70,700 150,1100 90,1800" stroke="#b9bcc2" stroke-width="16" fill="none" stroke-linecap="round" opacity=".7"/></g></svg>
<svg id="s4-swirl" class="svgl" width="1080" height="1920" style="opacity:0"><g filter="url(#wob)">
 <path d="M855,640 c40,0 40,-50 0,-50 c-60,0 -60,80 0,80 c80,0 80,-110 0,-110 c-100,0 -100,140 0,140" stroke="#8d9096" stroke-width="7" fill="none" stroke-linecap="round"/></g></svg>
<div id="s4-fokus" class="hand" style="left:600px;top:560px;font-size:52px;color:#6d7076;opacity:0">fo... kus?</div>
{bubble("s4-t1", 60, 520, 420, '"Aku tak berguna..."', 42, "right", "#eef0f2")}
{bubble("s4-t2", 140, 700, 420, '"Semua salah aku..."', 42, "right", "#eef0f2")}
""", 4))
tw('tl.fromTo("#s4-col",{opacity:0},{opacity:1,duration:.3},27.6);cam("#s4-cam",27.6,9.4,1.05,1.0);slam("#s4-hl",27.8,-1);')
tw('tl.fromTo("#s4-grey",{"--rv":"100%"},{"--rv":"0%",duration:1.8,ease:"power1.inOut"},29.9);')
tw('tl.fromTo("#s4-wave",{opacity:0,x:-200},{opacity:1,x:1100,duration:1.8,ease:"power1.inOut"},29.9);tl.to("#s4-wave",{opacity:0,duration:.2},31.6);')
tw('tl.to("#s4-kelabu",{color:"#6d7076",textShadow:"-7px 6px 0 #c3c6cb, 7px 9px 0 #dfe1e4",duration:.5},31.1);')
tw('tl.fromTo("#s4-swirl",{opacity:0,rotation:0},{opacity:1,rotation:200,duration:1.4,ease:"sine.inOut",transformOrigin:"855px 610px"},31.95);'
   'tl.fromTo("#s4-fokus",{opacity:0,filter:"blur(0px)"},{opacity:1,filter:"blur(3px)",duration:.9},32.3);fade(["#s4-swirl","#s4-fokus"],33.2,.25);')
tw('tl.fromTo("#s4-t1",{opacity:0,scale:.7},{opacity:1,scale:1,duration:.35,ease:"back.out(2)"},33.33);'
   'tl.fromTo("#s4-t2",{opacity:0,scale:.7},{opacity:1,scale:1,duration:.35,ease:"back.out(2)"},35.14);floaty("#s4-t1",33.8,3.0,8);')

# S5 NOT WEAKNESS 37.0-46.3 : tags on Amir torn off, three gears
def gear(id_, cx, cy, r, color, label, teeth=10):
    pts = []
    for i in range(teeth * 2):
        a = i * math.pi / teeth
        rr = r if i % 2 == 0 else r * .82
        for da in (-.12, .12):
            pts.append(f"{cx + rr * math.cos(a + da):.0f},{cy + rr * math.sin(a + da):.0f}")
    return (f'<g id="{id_}" opacity="0"><g class="gearrot" id="{id_}r"><polygon points="{" ".join(pts)}" fill="{color}" class="ink"/>'
            f'<polygon points="{" ".join(pts)}" fill="url(#hatch)" opacity=".5"/><circle cx="{cx}" cy="{cy}" r="{r * .6:.0f}" fill="#fff" class="ink5"/></g>'
            f'<text x="{cx}" y="{cy + 9}" text-anchor="middle" font-family="DV Sans" font-weight="900" font-size="{22 if len(label) > 7 else 28}" fill="#17161a">{label}</text></g>')


S.append(scene("s5", 37.0, 9.3, f"""
<svg class="svgl" width="1080" height="1920">{confetti(5, 18)}<g filter="url(#wob)">{floor_line()}{shadow(200, 300)}{shadow(855, 280)}</g></svg>
{hl("s5-hl", 190, 80, 'MASALAH KESIHATAN<br><span class="t">SEBENAR</span>')}
{sprite("s5-amir", "amir_low", 855, FLOOR, .8)}
<div id="s5-tag1" class="tag" style="left:720px;top:1000px;opacity:0"><div class="tag-in" style="background:#f08cb4">MALAS</div></div>
<div id="s5-tag2" class="tag" style="left:770px;top:1120px;opacity:0"><div class="tag-in" style="background:#b9a4f5">LEMAH</div></div>
<svg class="svgl" width="1080" height="1920"><g stroke="#e2382f" stroke-width="14" stroke-linecap="round" fill="none" filter="url(#wob)">
 <path id="s5-x1a" class="draw" pathLength="1" d="M712,996 L960,1086" opacity="0"/><path id="s5-x1b" class="draw" pathLength="1" d="M960,996 L712,1086" opacity="0"/>
 <path id="s5-x2a" class="draw" pathLength="1" d="M762,1116 L1010,1206" opacity="0"/><path id="s5-x2b" class="draw" pathLength="1" d="M1010,1116 L762,1206" opacity="0"/></g>
 <g filter="url(#wob)">{gear("s5-g1", 690, 600, 130, "#f08cb4", "BIOLOGI")}{gear("s5-g2", 900, 760, 112, "#b9a4f5", "PSIKOLOGI")}{gear("s5-g3", 660, 880, 112, "#ffd43b", "SOSIAL")}</g></svg>
<div id="s5-foot" class="hand" style="left:420px;top:1050px;width:600px;font-size:31px;line-height:1.15;white-space:normal;color:#3b3d42;opacity:0">* Doktor juga akan periksa punca fizikal lain (cth. tiroid).</div>
{rig("s5-doc", "drazren_point_marker", 210, FLOOR, .87)}
""", 5))
tw('tl.fromTo("#s5-doc",{x:-300,opacity:0},{x:0,opacity:1,duration:.45,ease:"power3.out"},37.0);bob("#s5-doc",37.4,8.8,1.4);')
tw('slam("#s5-tag1",37.2,-8);tl.set(["#s5-x1a","#s5-x1b"],{opacity:1},37.9);draw("#s5-x1a",37.9,.18);draw("#s5-x1b",38.06,.18);')
tw('slam("#s5-tag2",38.45,6);tl.set(["#s5-x2a","#s5-x2b"],{opacity:1},39.55);draw("#s5-x2a",39.55,.18);draw("#s5-x2b",39.71,.18);')
tw('tl.to(["#s5-tag1","#s5-x1a","#s5-x1b"],{y:620,rotation:-40,opacity:0,duration:.6,ease:"power2.in"},40.0);'
   'tl.to(["#s5-tag2","#s5-x2a","#s5-x2b"],{y:560,rotation:35,opacity:0,duration:.6,ease:"power2.in"},40.12);')
tw('slam("#s5-hl",40.14,-1);tl.to("#s5-amir",{opacity:0,scale:.96,duration:.4,transformOrigin:"50% 100%"},40.5);')
tw('tl.to("#s5-foot",{opacity:1,duration:.4},42.4);')
tw('pop("#s5-g1",44.25,.4);pop("#s5-g2",44.78,.4);pop("#s5-g3",45.7,.4);'
   'tl.fromTo("#s5-g1r",{rotation:0},{rotation:90,duration:2.0,ease:"none",svgOrigin:"690 600"},44.3);'
   'tl.fromTo("#s5-g2r",{rotation:0},{rotation:-100,duration:1.5,ease:"none",svgOrigin:"900 760"},44.8);'
   'tl.fromTo("#s5-g3r",{rotation:0},{rotation:-60,duration:.6,ease:"none",svgOrigin:"660 880"},45.7);')

# S6 SMALL STEPS 46.3-53.4 : stepping stones, Amir walks to Mei Ling
S.append(scene("s6", 46.3, 7.1, f"""
<svg class="svgl" width="1080" height="1920">{confetti(6, 16)}<g filter="url(#wob)">
 {sun(940, 470, 60)}{cloud(60, 430, 240)}{tree(980, 1150, .8)}{tree(120, 1120, .7, "#5fbf6a")}{grass(1180)}
</g></svg>
{hl("s6-hl", 180, 100, "LANGKAH KECIL")}
{prop("s6-stones", "stepping_stones", 45, 1089, 1.5)}
{note("s6-n1", 40, 560, 330, 110, "#ffd43b", "👟 GERAK SIKIT".replace("👟 ", ""), 40, -4)}
{note("s6-n2", 60, 700, 440, 150, "#9ad67a", "TIDUR &amp; MAKAN<br>IKUT WAKTU", 36, 3, "#f08cb4")}
{note("s6-n3", 470, 470, 300, 110, "#f08cb4", "LUAHKAN", 42, -3, "#ffd43b")}
<svg class="svgl" width="1080" height="1920"><g stroke="#2d9cdb" stroke-width="6" stroke-dasharray="12 10" fill="none" stroke-linecap="round" filter="url(#wob)">
 <path id="s6-a1" class="draw" pathLength="1" d="M200,680 C230,760 260,800 300,840" opacity="0"/>
 <path id="s6-a2" class="draw" pathLength="1" d="M420,860 C470,980 520,1080 560,1200" opacity="0"/>
 <path id="s6-a3" class="draw" pathLength="1" d="M700,590 C740,630 780,660 820,690" opacity="0"/></g>
 <g filter="url(#wob)"><g id="s6-sp1" opacity="0">{sparkle(420, 1450, 50)}<circle cx="300" cy="1480" r="10" fill="#ffd43b"/><circle cx="460" cy="1520" r="9" fill="#3cc4e6"/></g>
 <g id="s6-sp2" opacity="0">{sparkle(640, 1290, 46)}<circle cx="520" cy="1320" r="9" fill="#f08cb4"/><circle cx="680" cy="1350" r="8" fill="#ffd43b"/></g>
 <g id="s6-sp3" opacity="0">{sparkle(860, 1050, 50, "#ffd43b")}{heart(700, 1080, 46)}<circle cx="920" cy="1120" r="9" fill="#8f6cf0"/></g></g></svg>
{sprite("s6-mei", "meiling_relieved", 880, 1190, .38)}
{sprite("s6-amir", "amir_low", 360, 1580, .61)}
{sprite("s6-amir2", "amir_relieved", 715, 1262, .415, style="opacity:0")}
""", 6))
tw('slam("#s6-hl",46.44,-1);tl.fromTo("#s6-stones",{opacity:0,y:40},{opacity:1,y:0,duration:.4},46.3);')
tw('tl.fromTo("#s6-amir",{opacity:0,x:-60},{opacity:1,x:0,duration:.4,ease:"power3.out"},46.5);tl.fromTo("#s6-mei",{opacity:0},{opacity:1,duration:.4},46.8);')
tw('rise("#s6-n1",47.88,.3);tl.set("#s6-a1",{opacity:1},48.0);draw("#s6-a1",48.0,.4);pop("#s6-sp1",48.0,.4);')
tw('tl.to("#s6-amir",{x:210,y:-185,scale:.82,duration:.6,ease:"power2.inOut",transformOrigin:"50% 100%"},49.35);')
tw('rise("#s6-n2",49.56,.3);tl.set("#s6-a2",{opacity:1},49.7);draw("#s6-a2",49.7,.4);pop("#s6-sp2",49.8,.4);')
tw('tl.to("#s6-amir",{x:345,y:-325,scale:.69,duration:.6,ease:"power2.inOut",transformOrigin:"50% 100%"},51.15);')
tw('rise("#s6-n3",51.38,.3);tl.set("#s6-a3",{opacity:1},51.5);draw("#s6-a3",51.5,.4);pop("#s6-sp3",51.6,.4);')
tw('tl.to("#s6-amir",{opacity:0,duration:.25},52.75);tl.to("#s6-amir2",{opacity:1,duration:.25},52.75);bob("#s6-mei",51.6,1.6,4);')
tw('tl.fromTo("#s6-amir",{rotation:-1.5},{rotation:1.5,duration:.3,yoyo:true,repeat:11,transformOrigin:"50% 100%"},46.6);')

# S7 CLINIC 53.4-61.95
S.append(scene("s7", 53.4, 8.55, f"""
<svg class="svgl" width="1080" height="1920">{confetti(7, 14)}<g filter="url(#wob)">
 <rect x="680" y="660" width="330" height="230" rx="10" fill="#fff" class="ink"/><rect x="700" y="680" width="290" height="190" fill="#dff3fb"/>
 <path d="M845,680 l0,190 M700,775 l290,0" class="ink5"/>{sun(930, 730, 30)}
 <rect x="560" y="700" width="90" height="120" rx="6" fill="#fffdf2" class="ink5"/><path d="M580,730 l50,0 M580,755 l50,0 M580,780 l36,0" class="ink5"/><circle cx="605" cy="805" r="10" fill="#ffd43b" class="ink5"/>
 <path d="M990,1735 l-10,-150 q30,-60 60,0 l-10,150z" fill="#a8693a" class="ink5"/><path d="M1010,1590 c-60,-60 -40,-160 0,-200 c40,40 60,140 0,200z" fill="#5fbf6a" class="ink5"/>
 {floor_line()}{shadow(865, 300)}
</g></svg>
<div id="s7-ban" class="abs" style="left:110px;top:190px;width:860px;opacity:0"><div class="banner">BUKAN PENGGANTI RAWATAN</div></div>
<div id="s7-c1" class="card" style="left:70px;top:330px;width:450px;height:260px;opacity:0">
 <svg width="450" height="260" style="position:absolute;left:0;top:0"><g filter="url(#wob)">
  <path d="M40,40 l120,0 q14,0 14,14 l0,52 q0,14 -14,14 l-70,0 l-26,22 l4,-22 l-28,0 q-14,0 -14,-14 l0,-52 q0,-14 14,-14z" fill="#8f6cf0" class="ink5"/>
  <path d="M60,66 l80,0 M60,90 l56,0" stroke="#fff" stroke-width="7" stroke-linecap="round"/>
  <path d="M300,40 l100,0 q14,0 14,14 l0,52 q0,14 -14,14 l-20,0 l-4,22 l-24,-22 l-52,0 q-14,0 -14,-14 l0,-52 q0,-14 14,-14z" fill="#f08cb4" class="ink5"/>{heart(325, 52, 50)}</g></svg>
 <div class="abs" style="left:0;top:150px;width:450px;text-align:center;font-weight:900;font-size:38px;line-height:1.05">TERAPI PSIKOLOGI<br><span style="color:#11897b">(CBT)</span></div></div>
<div id="s7-c2" class="card" style="left:560px;top:330px;width:450px;height:260px;opacity:0">
 <svg width="450" height="260" style="position:absolute;left:0;top:0"><g filter="url(#wob)" transform="rotate(-25 225 80)">
  <rect x="140" y="50" width="170" height="64" rx="32" fill="#fff" class="ink5"/><path d="M225,52 l52,0 a30,30 0 0,1 0,60 l-52,0z" fill="#ff6b5e" class="ink5"/></g></svg>
 <div class="abs" style="left:0;top:150px;width:450px;text-align:center;font-weight:900;font-size:38px;line-height:1.05">UBAT<br><span style="color:#11897b">bila perlu</span></div></div>
<div id="s7-ok" class="sticker" style="left:250px;top:620px;width:580px;font-size:42px;background:#ffd43b;color:#17161a;-webkit-text-stroke:0;padding:6px 0;opacity:0">✔ TERBUKTI BERKESAN</div>
{rig("s7-doc", "drazren_clipboard", 330, 1700, .87)}
{prop("s7-desk", "desk_laptop", 20, 1299, 1.0)}
{sprite("s7-amir", "amir_low", 865, FLOOR, .8)}
""", 7))
tw('tl.fromTo("#s7-doc",{opacity:0},{opacity:1,duration:.3},53.4);cam("#s7-cam",53.4,8.55,1.0,1.03);slam("#s7-ban",53.49,0);bob("#s7-doc",53.8,8.0,1.2);')
tw('rise("#s7-c1",57.3,.4);rise("#s7-c2",59.65,.4);slam("#s7-ok",60.76,-3);')
tw('tl.fromTo("#s7-amir",{rotation:0},{rotation:1.4,duration:1.2,yoyo:true,repeat:5,ease:"sine.inOut",transformOrigin:"50% 100%"},54.0);')

# S8 HELP 61.95-73.5 : notice board + Dr. Azren full body
S.append(scene("s8", 61.95, 11.55, f"""
<svg class="svgl" width="1080" height="1920">{confetti(8, 10, op=.4)}<g filter="url(#wob)">
 <rect x="40" y="370" width="640" height="860" rx="20" fill="#d9a46b" class="ink"/><rect x="40" y="370" width="640" height="860" rx="20" fill="url(#hatch)" opacity=".5"/>
 <rect x="62" y="392" width="596" height="816" rx="12" fill="#e8bd88" class="ink5"/>
 {floor_line()}{shadow(845, 400)}
</g></svg>
{hl("s8-hl", 190, 90, "JANGAN TUNGGU.")}
<div id="s8-card" class="card" style="left:80px;top:420px;width:560px;height:760px;opacity:0;border-radius:14px">
 <span class="pin" style="left:30px;top:-14px"></span><span class="pin" style="right:30px;top:-14px;background:#3cc4e6"></span>
 <div id="s8-hi1" class="hi" style="top:30px"></div><div id="s8-hi2" class="hi" style="top:250px"></div><div id="s8-hi3" class="hi" style="top:470px"></div>
 <svg width="560" height="760" style="position:absolute;left:0;top:0"><use href="#phoneI" x="22" y="44" width="60" height="60"/><use href="#phoneI" x="22" y="264" width="60" height="60"/><use href="#phoneI" x="22" y="484" width="60" height="60"/></svg>
 <div class="abs" style="left:96px;top:40px;font-weight:900;font-size:44px;line-height:1.05">Talian HEAL<br>15555</div>
 <div class="abs" style="left:98px;top:150px;font-weight:700;font-size:28px;color:#3b3d42">8 pagi – 12 malam, setiap hari</div>
 <div class="abs" style="left:96px;top:260px;font-weight:900;font-size:44px;line-height:1.05">Befrienders<br>03-7627 2929</div>
 <div class="abs" style="left:98px;top:370px;font-weight:700;font-size:28px;color:#3b3d42">24 jam, percuma &amp; sulit</div>
 <div class="abs" style="left:96px;top:480px;font-weight:900;font-size:44px;line-height:1.05">Kecemasan<br><span style="color:#c8323a">999</span></div>
 <div class="abs" style="left:98px;top:590px;font-weight:700;font-size:28px;color:#3b3d42">jika dalam bahaya segera</div>
 <div class="hand" style="left:30px;top:650px;width:500px;white-space:normal;font-size:32px;line-height:1.1;color:#11897b">Rasa tak boleh berfungsi langsung? Jumpa doktor segera.</div></div>
{rig("s8-doc", "drazren_welcome", 860, FLOOR, .8)}
<svg class="svgl" width="1080" height="1920"><g filter="url(#wob)">{heart(930, 560, 70)}{sparkle(760, 600, 46)}</g></svg>
""", 8))
tw('tl.fromTo("#s8-doc",{opacity:0,y:40},{opacity:1,y:0,duration:.5,ease:"power3.out"},61.95);bob("#s8-doc",62.5,10.8,1.0);')
tw('tl.fromTo("#s8-card",{opacity:0,y:30},{opacity:1,y:0,duration:.5,ease:"power3.out"},62.3);slam("#s8-hl",65.06,-1);')
tw('tl.to("#s8-hi1",{opacity:.55,duration:.3},65.95);tl.to("#s8-hi1",{opacity:0,duration:.3},69.0);tl.to("#s8-hi2",{opacity:.55,duration:.3},69.09);'
   'tl.to("#s8-hi2",{opacity:0,duration:.3},70.15);tl.to("#s8-hi3",{opacity:.55,duration:.3},70.22);')


# S9a HOPE 73.5-77.4 : park in colour, plant blooms, Amir + Mei Ling + Dr. Azren
def hope_world(grey):
    plant = "plant_wilted" if grey else "plant_bloom"
    return f"""<svg class="svgl" width="1080" height="1920"><g filter="url(#wob)">
 {sun(900, 520, 80)}{cloud(100, 430, 280)}{bird(420, 480)}{bird(500, 520, .8)}{tree(140, 1280, 1.1)}{tree(990, 1260, .95, "#5fbf6a")}
 {grass()}{flower(60, 1720)}{flower(1020, 1700, "#8f6cf0")}{shadow(185, 300)}{shadow(510, 260)}{shadow(860, 380)}
</g></svg>
{prop("s9-bench" + ("g" if grey else ""), "park_bench", 200, 1330, 1.0)}
{prop("s9-plant" + ("g" if grey else ""), plant, 405, 1500, .5)}"""


S.append(scene("s9a", 73.5, 3.9, f"""
<div class="abs" style="left:0;top:0;width:1080px;height:1920px">{hope_world(False)}</div>
<div id="s9-grey" class="abs rvr grey" style="left:0;top:0;width:1080px;height:1920px;--rv:100%">{hope_world(True)}</div>
{hl("s9-h1", 180, 100, 'WARNA BOLEH<br><span class="t">KEMBALI</span>', False)}
{hl("s9-h2", 180, 100, 'ANDA TAK<br><span class="t">KESEORANGAN</span>')}
{sprite("s9-amir", "amir_relieved", 205, FLOOR, .74, cls="spr grey")}
{sprite("s9-mei", "meiling_relieved", 510, FLOOR, .7, cls="spr grey")}
{rig("s9-doc", "drazren_welcome", 848, FLOOR, .8, extra_cls="grey")}
<svg class="svgl" width="1080" height="1920"><g id="s9-conf" opacity="0" filter="url(#wob)">{sparkle(360, 1380, 60)}{sparkle(660, 1300, 50, "#3cc4e6")}{star(80, 760, 56)}{star(990, 820, 50, "starP")}{heart(330, 980, 60)}{heart(650, 900, 50)}</g></svg>
""", 9))
tw('tl.fromTo("#s9-grey",{"--rv":"100%"},{"--rv":"0%",duration:1.8,ease:"power1.inOut"},73.6);')
tw('tl.fromTo(["#s9-amir","#s9-mei","#s9-doc"],{filter:"grayscale(1) contrast(0.92) brightness(1.06)"},{filter:"grayscale(0) contrast(1) brightness(1)",duration:1.2},74.2);')
tw('pop("#s9-conf",75.0,.45);cam("#s9a-cam",73.5,3.9,1.02,1.0);fade("#s9-h1",75.8,.2);slam("#s9-h2",75.98,-1);')
tw('bob("#s9-mei",74.6,2.6,3);bob("#s9-amir",74.8,2.4,3);')

# S9b OUTRO 77.4-85.3 : Dr. Azren waves, the avatar family
S.append(scene("s9b", 77.4, 7.9, f"""
<svg class="svgl" width="1080" height="1920">{confetti(9, 30, op=.7)}<g filter="url(#wob)">{floor_line()}
 {shadow(110, 150)}{shadow(275, 150)}{shadow(540, 300)}{shadow(805, 150)}{shadow(970, 150)}</g></svg>
<div id="s9b-cta" class="abs" style="left:110px;top:190px;width:860px;opacity:0"><div class="banner" style="background:#f25f5c;font-size:52px;line-height:1.08;padding:12px 0 16px">SHARE DENGAN<br>ORANG TERSAYANG ♥</div></div>
{hl("s9b-l1", 430, 128, "Dr. Azren")}
<div id="s9b-l2" class="abs" style="left:0;top:580px;width:1080px;text-align:center;font-weight:900;font-size:60px;color:#11897b;opacity:0">| Spread Positivity |</div>
<div id="s9b-disc" class="abs" style="left:110px;top:662px;width:860px;text-align:center;font-weight:700;font-size:28px;color:#3b3d42;opacity:0">Pendidikan kesihatan umum, bukan diagnosis.</div>
{sprite("s9b-pr", "pakrahman_relieved", 110, FLOOR, .4)}{sprite("s9b-dn", "danish_relieved", 275, FLOOR, .4)}
{sprite("s9b-kr", "kakros_relieved", 805, FLOOR, .4)}{sprite("s9b-dv", "divya_relieved", 970, FLOOR, .4)}
{rig("s9b-doc", "drazren_wave", 540, FLOOR, .85)}
<svg class="svgl" width="1080" height="1920"><g id="s9b-conf" opacity="0" filter="url(#wob)">{sparkle(80, 820, 70)}{sparkle(930, 800, 80)}{star(60, 1000, 60)}{star(970, 1010, 56, "starP")}{heart(860, 900, 80)}{sparkle(200, 950, 50, "#3cc4e6")}</g></svg>
""", 11))
tw('tl.fromTo("#s9b-doc",{y:200,opacity:0},{y:0,opacity:1,duration:.5,ease:"back.out(1.3)"},77.4);bob("#s9b-doc",77.9,7.3,1.6);')
for i, (k, t) in enumerate([("s9b-pr", 77.7), ("s9b-dn", 77.85), ("s9b-kr", 78.0), ("s9b-dv", 78.15)]):
    tw(f'tl.fromTo("#{k}",{{y:160,opacity:0}},{{y:0,opacity:1,duration:.45,ease:"back.out(1.4)"}},{t});bob("#{k}",{t + .5},{84.9 - t:.1f},{2 + i % 2});')
tw('slam("#s9b-cta",77.46,0);slam("#s9b-l1",79.94,-2);rise("#s9b-l2",80.6,.4);pop("#s9b-conf",80.88,.5);floaty("#s9b-conf",81.4,3.9,10);tl.to("#s9b-disc",{opacity:1,duration:.4},82.2);')

# global scene-change marker swipes
SWIPES = [4.2, 13.7, 27.6, 37.0, 46.3, 53.4, 61.95, 73.5, 77.4]
swipe_svg = "".join(
    f'<path id="sw{i}" class="draw" pathLength="1" d="M-60,{700 + (i % 3) * 260} C200,{560 + (i % 3) * 260} 520,{900 + (i % 3) * 200} 1140,{640 + (i % 3) * 260}" '
    f'stroke="{["#ffd43b", "#3cc4e6", "#f08cb4", "#8f6cf0"][i % 4]}" stroke-width="150" fill="none" stroke-linecap="round" opacity="0"/>'
    for i in range(len(SWIPES)))
for i, t in enumerate(SWIPES):
    tw(f'tl.set("#sw{i}",{{opacity:.9}},{t - .22:.2f});draw("#sw{i}",{t - .22:.2f},.22);tl.to("#sw{i}",{{opacity:0,duration:.25}},{t + .02:.2f});')

# ---------------------------------------------------------------- page
tpl = open(os.path.join(HERE, "src", "page_v2.tpl.html")).read()
html = tpl.replace("<!--@SCENES-->", "\n".join(S)).replace("<!--@SWIPES-->", swipe_svg).replace("/*@SCENE_TWEENS*/", "\n".join(TWEENS))
open(os.path.join(HERE, "src", "index.src.html"), "w").write(html)
print("scenes", len(S), "tweens", len(TWEENS))
