#!/usr/bin/env python3
"""Builds a source-page mock from cl-6.data's health.json, and nothing else.
usage: source-page-build.py health.json out.html
Every figure comes from the file; nothing is explained that the file does not explain."""
import json,html,sys,datetime as dt
esc=html.escape
H=json.load(open(sys.argv[1])); out=sys.argv[2]
def fmt_b(n):
    return f"{n/1_000_000:.1f} MB" if n>=1_000_000 else (f"{n/1000:.0f} KB" if n>=1000 else f"{n} B")
def when(s):
    t=dt.datetime.fromisoformat(s.replace('Z','+00:00')); return f"{t.day} {t.strftime('%b')} {t:%H:%M} UTC"
def lisbon(s): return when(s)
lr=H['last_run']; runs=H['runs']; cp=H['copies']; sch=H['schedule']; pr=H['problems']
nreq=len(lr['requests']); failed_names=[r for r in runs[0].get('failed_requests',[])]
nfail=len(pr)
verdict=('Healthy','●') if not pr else ('Partly failing','▲')
if pr and lr['ok']==0: verdict=('Failing','■')
chg=sum(1 for r in runs if r['changed_requests'])
def runstrip():
    cells=''.join(f'<span class="c {"bad" if r["failed_requests"] else "ok"}" title="{esc(when(r["at"]))}">{"▲" if r["failed_requests"] else "●"}</span>' for r in reversed(runs))
    return f'<div class="strip" aria-label="Last {len(runs)} runs, oldest first">{cells}</div><p class="mono">Oldest to newest, last {len(runs)} runs kept. ● all requests read · ▲ at least one request failed</p>'
def req_rows():
    rows=''
    for r in lr['requests']:
        st=r['status']; word='changed' if r.get('changed') else 'same as before'
        bad=r['name'] in failed_names
        rows+=f'<li class="{"bad" if bad else ""}"><div class="rn">{esc(r["name"])}</div><div class="rs"><b>{esc(str(st))}</b> · {fmt_b(r.get("bytes",0))} · {word}</div><div class="rm">{esc(r.get("meaning",""))}</div></li>'
    return rows
def cmp_link(r):
    u=r.get('compare_with_previous_run_url')
    return f' · <a href="{esc(u)}">what changed since the run before</a>' if u else ' · oldest run kept, nothing to compare with'
def run_rows():
    rows=''
    for r in runs:
        rows+=f'<li><div><b>{esc(when(r["at"]))}</b> · {r["ok"]} read, {r["failed"]} failed · {len(r["changed_requests"])} changed</div><div class="mono"><a href="{esc(r["commit_url"])}">commit {esc(r["commit"])}</a>{cmp_link(r)}</div></li>'
    return rows
if pr:
    wrong=''.join(f'<li><div class="rn">{esc(p["request"])}</div><div class="rs"><b>{esc(",".join(str(s) for s in p["status"]))}</b> · {esc(p["plain"])} · failed in {esc(p["failed_in"])}</div><div class="mono"><a href="{esc(p["url"])}">{esc(p["url"][:80])}{"…" if len(p["url"])>80 else ""}</a></div></li>' for p in pr)
    wrongblock=f'<h2>What is wrong</h2><p>{len(pr)} of {nreq} requests are refused or failing, in every run kept. The rest are read normally.</p><ul class="req">{wrong}</ul>'
else:
    notes=[r for r in lr['requests'] if r['status']>=400]
    extra=(' '+'; '.join(f'{esc(r["name"])}: {esc(r["meaning"])}' for r in notes)) if notes else ''
    wrongblock=f'<h2>What is wrong</h2><p>Nothing is wrong. {lr["ok"]} of {nreq} requests were read normally.{extra}</p>'
mism= sch['card_says']!=sch['really']
css='''*{box-sizing:border-box}:root{--bg:#f6f3ec;--ink:#121317;--ink3:#595c64;--rule:#9d9580;--hair:#d9d2c1;--panel:#fffdf8;--g:#006600;--warn:#8a5200}body{margin:0;background:var(--bg);color:var(--ink);font:16px/1.45 Newsreader,Georgia,serif}.w{max-width:760px;margin:0 auto;padding:16px}.back{font:12px "IBM Plex Mono",monospace}h1{font-size:26px;line-height:1.2;margin:8px 0}h2{font:700 12px/1 "IBM Plex Mono",monospace;letter-spacing:.08em;text-transform:uppercase;margin:28px 0 10px;border-top:2px solid var(--ink);padding-top:10px}.mono{font:12px/1.5 "IBM Plex Mono",monospace;color:var(--ink3)}.top{display:flex;justify-content:space-between;gap:10px;align-items:flex-start}.badge{font:700 12px "IBM Plex Mono",monospace;border:2px solid var(--ink);padding:6px 10px;white-space:nowrap;background:var(--panel)}.badge.bad{border-color:var(--warn)}.figs{display:grid;grid-template-columns:repeat(auto-fit,minmax(130px,1fr));gap:8px}.fig{border:1px solid var(--rule);background:var(--panel);padding:10px}.fig b{display:block;font:600 22px/1.1 "IBM Plex Mono",monospace}.bar{height:14px;background:var(--hair);margin:6px 0}.bar i{display:block;height:100%;background:var(--g)}.sch{border:1px solid var(--rule);background:var(--panel);padding:10px}.sch .row{display:flex;gap:10px;padding:4px 0}.sch .lb{font:600 11px "IBM Plex Mono",monospace;text-transform:uppercase;color:var(--ink3);width:110px;flex:none}.mis{border:2px solid var(--warn);padding:8px 10px;margin-top:8px;background:#fff}ul.req,ul.runs{list-style:none;margin:0;padding:0}ul.req li,ul.runs li{border-top:1px solid var(--hair);padding:8px 0}ul.req li.bad{border-left:4px solid var(--warn);padding-left:8px}.rn{font:600 13px "IBM Plex Mono",monospace;overflow-wrap:anywhere}.rs{font:13px "IBM Plex Mono",monospace}.rm{font-size:14px;color:var(--ink3)}.strip{display:flex;flex-wrap:wrap;gap:3px}.c{font-size:16px;width:20px;text-align:center}.c.bad{color:var(--warn)}a{color:var(--ink);overflow-wrap:anywhere}.mono{overflow-wrap:anywhere}summary{cursor:pointer;font:600 12px "IBM Plex Mono",monospace}.json{border:1px dashed var(--rule);padding:10px;background:#fff;font:12px "IBM Plex Mono",monospace;color:var(--ink3)}'''
sc=max(cp['bytes_in_git_data'],cp['bytes_in_vault_working_copy'],1)
body=f'''<div class="w"><p class="back"><a href="#">← All sources (status)</a></p>
<div class="top"><h1>{esc(H["title"])}</h1><span class="badge {'bad' if pr else ''}">{verdict[1]} {verdict[0]}</span></div>
<p class="mono">Source: <a href="{esc(H["source_home"])}">{esc(H["source_home"].split("//")[1].split("/")[0])}</a> · health read {esc(when(H["generated_utc"]))}</p>
<h2>What we hold</h2><div class="figs"><div class="fig"><b>{cp["files_in_git_data"]}</b>files in git ({fmt_b(cp["bytes_in_git_data"])})<div class="bar"><i style="width:{max(2,cp['bytes_in_git_data']/sc*100):.0f}%"></i></div></div>
<div class="fig"><b>{cp["files_in_vault_working_copy"]}</b>files in the vault working copy ({fmt_b(cp["bytes_in_vault_working_copy"])})<div class="bar"><i style="width:{max(2 if cp['bytes_in_vault_working_copy'] else 0,cp['bytes_in_vault_working_copy']/sc*100):.0f}%"></i></div></div>
<div class="fig"><b>{cp["dated_copies_in_vault"]}</b>dated copies in the vault</div></div><p class="mono">Bars share one scale. The vault holds the full history.</p>
<h2>When it is collected</h2><div class="sch"><div class="row"><span class="lb">The card says</span><span>{esc(sch["card_says"])}</span></div><div class="row"><span class="lb">It really runs</span><span>{esc(sch["really"])}</span></div><div class="row"><span class="lb">Last run</span><span>{esc(when(lr["at"]))}</span></div></div>{'<div class="mis"><b>These disagree.</b> The card says "'+esc(sch["card_says"])+'"; the collector runs '+esc(sch["really"])+'.</div>' if mism else ''}
{wrongblock}
<h2>The last run, request by request</h2><ul class="req">{req_rows()}</ul>
<h2>Run history</h2>{runstrip()}<p>{chg} of the last {len(runs)} runs found something new.</p><ul class="runs">{run_rows()}</ul>
<h2>Where it is kept</h2><ul class="runs"><li><a href="{esc(cp["where"]["git"])}">The files in git</a></li><li><a href="{esc(cp["where"]["api_latest"])}">API: latest</a></li><li><a href="{esc(cp["where"]["api_reads"])}">API: the request log</a></li><li><a href="{esc(H["source_home"])}">The source's own page</a> (it is not embedded here)</li></ul><p class="mono">{esc(cp["note"])}</p>
<h2>The data, as JSON</h2><div class="json">Embedded viewer of latest.json goes here (built by cl-6.dev from the API file; a tree you can open, no third-party script).</div></div>'''
open(out,'w').write('<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>Source</title><style>'+css+'</style></head><body>'+body+'</body></html>')
print(H['source'],verdict[0],len(pr),chg,len(runs))
