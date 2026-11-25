import asyncio
from playwright.async_api import async_playwright
async def main():
    async with async_playwright() as p:
        b = await p.chromium.launch(executable_path='/usr/bin/google-chrome', args=['--no-sandbox'])
        pg = await (await b.new_context(viewport={'width':390,'height':844})).new_page(); errs=[]
        pg.on('pageerror', lambda e: errs.append(str(e)))
        await pg.goto('http://localhost:8771/#home'); await pg.wait_for_timeout(2500)
        print(await pg.evaluate("[APP_VERSION, S.q.size, MATERIAS_EDITAL, (()=>{const c={};[...S.q.values()].forEach(q=>c[q.materia]=(c[q.materia]||0)+1);return c})()]"))
        await pg.screenshot(path='tg.png'); print('ERR', errs); await b.close()
asyncio.run(main())
