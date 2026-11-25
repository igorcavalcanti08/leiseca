import asyncio, shutil, glob
from playwright.async_api import async_playwright
U='http://localhost:8770/'
BAR="!document.querySelector('#abRate').hidden || !document.querySelector('#abNext').hidden"
async def main():
    async with async_playwright() as p:
        b = await p.chromium.launch(executable_path='/usr/bin/google-chrome', args=['--no-sandbox'])
        ctx = await b.new_context(viewport={'width':390,'height':844}, is_mobile=True, service_workers='block')
        pg = await ctx.new_page(); errs=[]
        pg.on('pageerror', lambda e: errs.append(str(e))); pg.on('console', lambda m: errs.append(m.text) if m.type=='error' else None)
        await pg.goto(U+'#home'); await pg.wait_for_timeout(1500)
        print('BASE', await pg.evaluate("[APP_VERSION, S.q.size]"))
        await pg.click('#btnAll'); await pg.wait_for_timeout(200)
        for i in range(3):
            g,t=await pg.evaluate("[S.current.gabarito,S.current.tipo]"); await pg.click(f'[data-alt="{g}"]' if t=='ME' else ('#btnC' if g=='C' else '#btnE')); await pg.wait_for_function(BAR)
            await pg.click('#abRate .g3' if await pg.evaluate("!document.querySelector('#abRate').hidden") else '#btnNext'); await pg.wait_for_function("!S.answered")
        for f in glob.glob('/home/claude/leiseca13/*'): shutil.copy(f, '/home/claude/serve/')
        await pg.goto(U+'#home'); await pg.reload(); await pg.wait_for_timeout(1500)
        print('NEW', await pg.evaluate("[APP_VERSION, S.q.size, S.p.size, S.meta.seedVersion]"))
        print('por materia', await pg.evaluate("(()=>{const c={};[...S.q.values()].forEach(q=>c[q.materia]=(c[q.materia]||0)+1);return c})()"))
        print('toast', await pg.evaluate("document.querySelector('#toast').textContent"))
        print('upd', await pg.evaluate("S.q.get('INF-O-03').textoLei.includes('desde 2024')"))
        print('validator EXTRA', await pg.evaluate("(()=>{let e=[],a=[];EXTRA.forEach((q,i)=>{const r=validarQuestao(q,i);e.push(...r.erros);a.push(...r.avisos)});return [e.slice(0,5),a.length,a.slice(0,3)]})()"))
        # Excel com tabela (ME)
        await pg.evaluate("estudar({nome:'t',itens:[{materia:'Matemática'}]})"); await pg.wait_for_timeout(200)
        await pg.evaluate("renderQuestao(S.q.get('INF-XT-03'),'new')"); await pg.wait_for_timeout(200)
        print('tabela', await pg.evaluate("document.querySelectorAll('#qTab td').length"), await pg.evaluate("!document.querySelector('#answerBar').classList.contains('show')"))
        await pg.screenshot(path='v13xl.png', full_page=True)
        await pg.click('[data-alt="A"]'); await pg.wait_for_function(BAR)
        print('fb', await pg.evaluate("[...document.querySelectorAll('#qFeedback .label')].map(x=>x.textContent)"))
        await pg.screenshot(path='v13xl2.png', full_page=True)
        await pg.click('#btnNext' if await pg.evaluate("!document.querySelector('#abNext').hidden") else '#abRate .g3'); await pg.wait_for_timeout(300)
        # Português CE
        await pg.evaluate("renderQuestao(S.q.get('INF-O-03'),'new')"); await pg.wait_for_timeout(100)
        await pg.click('#btnC'); await pg.wait_for_function(BAR)
        print('fb por', await pg.evaluate("[...document.querySelectorAll('#qFeedback .label')].map(x=>x.textContent)"), await pg.evaluate("document.querySelectorAll('.qrow').length"))
        await pg.screenshot(path='v13por.png', full_page=True)
        await pg.goto(U+'#home'); await pg.wait_for_timeout(400); await pg.screenshot(path='v13home.png', full_page=True)
        await pg.reload(); await pg.wait_for_timeout(1500); print('2nd load', await pg.evaluate("[S.meta.seedVersion, document.querySelector('#toast').classList.contains('show'), S.p.size]"))
        print('ERR', errs); await b.close()
asyncio.run(main())
