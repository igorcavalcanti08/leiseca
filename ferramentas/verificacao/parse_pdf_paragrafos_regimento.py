import re, json
raw = open('/tmp/ri/ri.txt', encoding='utf-8').read().replace('\f', '\n')
i0 = raw.find('Art. 1º Este Regimento')
raw = raw[i0:]
lines = [l.strip() for l in raw.split('\n')]
START = re.compile(r'^(Art\. \d|§ ?\d|Parágrafo único|[IVXL]+(-[A-Z])? ?[-–]|[a-z]\) |Título |TÍTULO|Capítulo |CAPÍTULO|Seção |Subseção |\* )')
out=[]; cur=None
for s in lines:
    if not s or re.fullmatch(r'\d{1,3}', s): continue
    if START.match(s):
        if cur: out.append(cur)
        cur = s
    else:
        if cur is None: continue
        cur = (cur[:-1]+s) if re.search(r'[a-zà-ú]-$', cur) else cur+' '+s
if cur: out.append(cur)
out=[re.sub(r'\s+',' ',p).strip() for p in out]
json.dump(out, open('/home/claude/interna/ri_paras.json','w'), ensure_ascii=False)
print(len(out))
