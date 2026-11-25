(async()=>{
const norm=s=>{s=s.normalize('NFC');
s=s.replace(/\s*\((Reda[çc][ãa]o dada|Inclu[íi]d[oa]|Vide|Vig[êe]ncia|Renumerad|Revogad)[^)]*\)+/gi,'');
s=s.replace(/\s+Vig[êe]ncia\s*$/i,'');s=s.replace(/[–—‑]/g,'-').replace(/“/g,'"').replace(/”/g,'"');
s=s.replace(/\s+/g,' ');s=s.replace(/\s+([:;.,])/g,'$1');s=s.replace(/([.:;])\.+/g,'$1');return s.trim();};
const b=document.body.cloneNode(true);b.querySelectorAll('strike,s,del,[style*="line-through"]').forEach(e=>e.remove());
const ps=[...b.querySelectorAll('p')].map(p=>p.innerText);
const H=new Set();for(const t of ps){const n=norm(t);if(!n)continue;const d=await crypto.subtle.digest('SHA-256',new TextEncoder().encode(n));H.add([...new Uint8Array(d)].map(x=>x.toString(16).padStart(2,'0')).join('').slice(0,12));}
window.__H=H;window.__nps=ps.map(norm);return H.size;})()
