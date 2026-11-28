#!/usr/bin/env python3
"""Builds mock.html for the newsroom dashboard from the real files.
usage: mock-build.py questions.json briefing.json out.html [admin|public]
admin mode (behind sign-in, later): the full dashboard. public mode (the open page, cl-6.security 28 Nov 02:30Z): only items with public:true, each as title, public_summary and if_you_wait (cl-6.decisions' rule allows title, public_summary, why, if_you_wait, unblocks and the agent name in where) and never an answer line, option, where, link, id, Copy box or checked time; no briefing times or changes; no counts of non-public items.
Reads only: cl-6.decisions' questions.json (title, why, if_you_wait, unblocks, tier, kind, answer_line, options,
where, where_url, recommended, checked_at, since, question, asked_by, id) and cl-6.maestro's briefing.json (brief, changes)."""
import json,html,sys,re,datetime as dt
esc=html.escape
Q=json.load(open(sys.argv[1])); B=json.load(open(sys.argv[2])); out=sys.argv[3]; MODE=sys.argv[4] if len(sys.argv)>4 else 'admin'
qs=sorted(Q['questions'],key=lambda x:x.get('rank',999)); tier=lambda t:[x for x in qs if x['tier']==t]
now,week,later,ans=tier('now'),tier('week'),tier('later'),tier('answered')
KIND={'decision':'Decision','approval':'Approval','information':'For information'}
def dl(s):
    x=dt.date.fromisoformat(s[:10]); return f"{x.day} {x.strftime('%b')}"
def hm(s): return f"{int(s[8:10])} {dt.date.fromisoformat(s[:10]).strftime('%b')} {s[11:16]} UTC"
BTN='<button type="button" aria-label="Copy this answer" onclick="navigator.clipboard&&navigator.clipboard.writeText(this.previousElementSibling.textContent)">Copy</button>'
def oneway(x):
    if not x.get('one_way'): return ''
    if x.get('one_way_line'):
        return f'<p class="ow">{esc(x["one_way_line"])}</p>'
    w=(x.get('where') or '').split(';')[0].split(' (')[0]
    reason=esc(x.get('one_way_reason') or '')
    return f'<p class="ow"><b>One-way door{(": "+reason) if reason else ""}.</b></p>'
def grant(x):
    g=x.get('grant_text')
    if not g: return ''
    return f'<div class="gt"><div class="al">What you are approving</div><div class="gtext">{esc(g)}</div></div>'
def answer(x):
    a=x['answer_line'].strip(); rec=x.get('recommended')
    if x['kind']=='information' or a.startswith('('):
        txt=a.strip('()'); return f'<div class="ans do"><div class="al">{"Pass this on" if x["kind"]=="information" else "Do this yourself"}</div><div class="line">{esc(txt[:1].upper()+txt[1:])}</div></div>'
    if '<' in a and '>' in a:
        return f'<div class="ans do"><div class="al">Write your own</div><div class="line">{esc(a)}</div></div>'
    alts=[o['label'] for o in x['options']] if x.get('options') else [s.strip() for s in re.split(r'\s+\|\s+',a) if s.strip()]
    def one(s):
        mark='<div class="rec">Recommended by '+esc(rec['by'])+'</div>' if rec and rec['answer'].strip().lower()==s.strip().lower() else ''
        return f'<div class="alt"><span class="line">{esc(s)}</span>{BTN}</div>{mark}'
    lab='Say one of these' if len(alts)>1 else 'Say'
    return f'<div class="ans"><div class="al">{lab}</div>{"".join(one(s) for s in alts)}</div>'
def where(x):
    w=x['where'].split(';')[0]
    if not w: return ''
    return f'<p class="wh">Where: {"<a href=%s>"%chr(34)+esc(x["where_url"])+chr(34)+">" if False else ""}{("<a href=\""+esc(x["where_url"])+"\">"+esc(w)+"</a>") if x.get("where_url") else esc(w)}</p>'
def body(x):
    unb=f'<p><span class="lb">Unblocks</span> {esc(x["unblocks"])}</p>' if x.get('unblocks') else ''
    return (f'<p><span class="lb">Why</span> {esc(x["why"])}</p><p><span class="lb">If you wait</span> {esc(x["if_you_wait"])}</p>{grant(x)}{answer(x)}{where(x)}'
      f'{("<p class=\"chk\">Facts checked "+esc(hm(x["checked_at"]) if len(x["checked_at"])>10 else dl(x["checked_at"]))+"</p>") if x.get("checked_at") else ""}{oneway(x)}<details><summary>Details</summary>{unb.replace('<p>','<p class="dt">')}<p class="dt">Asked by {esc(x["asked_by"])} · waiting since {esc(dl(x["since"]))} · id {esc(x["id"])}</p><p class="dt">{esc(x["question"])}</p></details>')
def card(x): return f'<article class="card now"><header><span>● Now · {KIND[x["kind"]]}{(" · One-way door" if x.get("one_way") else "")}</span><span>since {esc(dl(x["since"]))}</span></header><h3>{esc(x["title"])}</h3>{body(x)}</article>'
def row(x,m,n): return f'<li><details><summary><span class="t"><span class="mk">{n}</span> {esc(x["title"])}{(" <span class=\"mk\">· one-way door</span>" if x.get("one_way") else "")}</span><span class="sn">{KIND[x["kind"]]} · {esc(dl(x["since"]))}</span></summary>{body(x)}</details></li>'
css='''*{box-sizing:border-box}:root{--bg:#f6f3ec;--ink:#121317;--ink3:#595c64;--rule:#9d9580;--hair:#d9d2c1;--panel:#fffdf8;--warn:#8a5200}body{margin:0;background:var(--bg);color:var(--ink);font:16px/1.45 Newsreader,Georgia,serif}.w{max-width:760px;margin:0 auto;padding:16px}h1{font-size:28px;margin:8px 0 4px}h2{font:700 12px/1 "IBM Plex Mono",monospace;letter-spacing:.08em;text-transform:uppercase;margin:28px 0 10px;border-top:2px solid var(--ink);padding-top:10px}.mono{font:12px/1.4 "IBM Plex Mono",monospace;color:var(--ink3)}.card{background:var(--panel);border:1px solid var(--rule);padding:14px;margin:0 0 12px}.card.now{border:2px solid var(--ink)}.card header{display:flex;justify-content:space-between;font:600 11px/1 "IBM Plex Mono",monospace;margin-bottom:8px}.card h3{font-size:20px;line-height:1.25;margin:0 0 8px}.card p,li p{margin:0 0 6px}.dt,.chk{font:12px/1.5 "IBM Plex Mono",monospace;color:var(--ink3);overflow-wrap:anywhere}.lb{font:600 10.5px "IBM Plex Mono",monospace;text-transform:uppercase;letter-spacing:.06em;color:var(--ink3);margin-right:6px}.ans{border:1px solid var(--ink);padding:8px 10px;margin:8px 0;background:#fff}.ans.do{background:var(--panel);border-style:dashed}.al{font:600 10.5px "IBM Plex Mono",monospace;text-transform:uppercase;letter-spacing:.06em;color:var(--ink3);margin-bottom:6px}.line{font:13px/1.45 "IBM Plex Mono",monospace;overflow-wrap:anywhere}.alt{display:flex;gap:8px;align-items:flex-start;justify-content:space-between;padding:4px 0}.alt+.alt{border-top:1px solid var(--hair)}.alt .line{flex:1}.gt{border:2px solid var(--ink);padding:8px 10px;margin:8px 0;background:#fff}.rule{border:2px solid var(--warn);padding:8px 10px;background:#fff;font-size:15px;margin:14px 0 0}.ow{border:2px solid var(--warn);padding:6px 10px;background:#fff;font-size:15px}.gtext{font:15px/1.45 Newsreader,Georgia,serif}button{font:600 12px "IBM Plex Mono",monospace;border:1px solid var(--ink);background:var(--bg);padding:6px 12px;border-radius:999px;min-height:36px;min-width:60px;flex:none}.rec{display:block;font:600 10.5px "IBM Plex Mono",monospace;color:var(--ink3);margin-top:2px}.card p.wh,li p.wh{font:12px "IBM Plex Mono",monospace;color:var(--ink3);margin:2px 0 4px}summary{cursor:pointer;font:600 12px "IBM Plex Mono",monospace}ul.rows,ul.chg{list-style:none;margin:0;padding:0}ul.rows li{border-top:1px solid var(--hair)}ul.rows summary{display:flex;justify-content:space-between;gap:10px;padding:10px 0;font:500 15px/1.3 Newsreader,Georgia,serif}ul.rows summary .t{flex:1}.sn,.mk{font:11px "IBM Plex Mono",monospace;color:var(--ink3);white-space:nowrap}.heart{font:13px/1.5 "IBM Plex Mono",monospace;margin:6px 0}.counts{font:600 14px/1.5 "IBM Plex Mono",monospace;margin:8px 0}.chg li{padding:6px 0;border-top:1px solid var(--hair);font-size:15px}.chg .at{font:11px "IBM Plex Mono",monospace;color:var(--ink3);display:block}.flag{border:1px solid var(--warn);padding:8px 10px;margin-top:8px;background:#fff}'''

if MODE=='public':
    P=[x for x in qs if x.get('public') is True]
    pcards=''.join(f'<article class="card now"><h3>{esc(x["title"])}</h3><p>{esc(x["public_summary"])}</p><p><span class="lb">If you wait</span> {esc(x["if_you_wait"])}</p></article>' for x in P)
    pbody=f'''<div class="w"><h1>The newsroom today</h1>
<p class="mono">How the newsroom is doing, in public: who does what, what is waiting, and how fresh the data is. Run by AI agents, operated by Dinis Cruz.</p>
<p class="heart">Last article published 26 Nov · 117 articles live · build v0.1.2412, checks passed at the build</p>
<p class="mono">Built 28 Nov 02:00 UTC</p>
<h2>Waiting on Dinis</h2>{pcards}
<h2>Agents</h2><p>43 agents, each with its role and state. <a href="#">Every agent by desk</a></p>
<h2>Data</h2><p>30 datasets: 23 fresh, 1 archive, 6 with a source problem. <a href="#">Every dataset, with its source and date</a></p></div>'''
    open(out,'w').write('<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>Status</title><style>'+css+'</style></head><body>'+pbody+'</body></html>')
    print('public',len(P)); sys.exit(0)
ch=''.join(f'<li><span class="at">{esc(hm(c["at"].replace("1xZ","00Z")))} · {esc(c["kind"])}</span>{esc(c["text"])}</li>' for c in B['changes'][:5])
br=B['brief']
body_=f'''<div class="w"><h1>What needs you</h1>
<p class="heart">Last article published 26 Nov · 117 articles live · build v0.1.2412, checks passed at the build</p>
<p class="counts">{len(now)} need you now · {len(week)} this week · {len(later)} can wait · {len(ans)} answered</p>
<p class="mono">Built 28 Nov 02:00 UTC · list updated {esc(hm(Q['updated']+'Z' if len(Q['updated'])==16 else Q['updated']))} · last briefed {esc(hm(br['last_brief_at']))} · next briefing {esc(hm(br['next_brief_at']))}</p>
<p class="rule"><b>One-way doors</b> cannot be undone. Only words you give yourself count, typed or pasted by you in the session the card names. Words relayed by an agent, or a button on this page, do not.</p><h2>Decide now ({len(now)})</h2>{"".join(card(x) for x in now)}
<p class="mono">Answered somewhere else? This page catches up at its next build.</p>
<h2>This week ({len(week)})</h2><ul class="rows">{"".join(row(x,'◐',i+1) for i,x in enumerate(week))}</ul>
<h2>Can wait ({len(later)})</h2><details><summary>Show the {len(later)} that can wait</summary><ul class="rows">{"".join(row(x,'○',i+1) for i,x in enumerate(later))}</ul></details>
<h2>What changed since you last looked</h2><ul class="chg">{ch}</ul>
<h2>Running fine</h2><div class="flag"><b>Needs a look</b><br>17 agents are blocked. <a href="#">See each one and what it waits on</a><br>6 data sources have a problem. <a href="#">See which</a></div><p style="margin-top:10px">Running fine: 26 agents idle, 23 datasets fresh, 1 archive. <a href="#">Every agent by desk</a> · <a href="#">Every dataset</a></p>
<h2>Answered ({len(ans)})</h2><p class="mono">{esc(ans[0]["title"]) if ans else "none"}{(": "+chr(8220)+esc(ans[0].get("answer_given",""))+chr(8221)) if ans and ans[0].get("answer_given") else ""}</p></div>'''
open(out,'w').write('<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>Status</title><style>'+css+'</style></head><body>'+body_+'</body></html>')
print(len(now),len(week),len(later),len(ans))
