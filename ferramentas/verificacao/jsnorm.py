import re,unicodedata,hashlib,json
def norm(s):
    s=unicodedata.normalize('NFC',s)
    s=re.sub(r'\s*\((Reda[çc][ãa]o dada|Inclu[íi]d[oa]|Vide|Vig[êe]ncia|Renumerad|Revogad)[^)]*\)+','',s,flags=re.I)
    s=re.sub(r'\s+Vig[êe]ncia\s*$','',s,flags=re.I); s=re.sub(r'[–—‑]','-',s).replace('“','"').replace('”','"')
    s=re.sub(r'\s+',' ',s); s=re.sub(r'\s+([:;.,])',r'\1',s); s=re.sub(r'([.:;])\.+',r'\1',s); return s.strip()
h=lambda s: hashlib.sha256(norm(s).encode()).hexdigest()[:12]
