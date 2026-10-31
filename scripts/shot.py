import asyncio, sys
from playwright.async_api import async_playwright
async def main():
    async with async_playwright() as p:
        b=await p.chromium.launch()
        for name,w,h,scheme in [("desktop-light",1360,900,"light"),("phone-dark",400,860,"dark")]:
            ctx=await b.new_context(viewport={"width":w,"height":h},color_scheme=scheme)
            pg=await ctx.new_page(); errs=[]
            pg.on("console",lambda m: errs.append(m.text) if m.type in ("error","warning") else None); pg.on("pageerror",lambda e: errs.append(str(e)))
            await pg.goto("file:///home/user/embodied-ai-governance-v4/dashboard/index.html"); await pg.wait_for_timeout(1500)
            await pg.screenshot(path=f"/home/user/embodied-ai-governance-v4/dashboard/shot-{name}.png",full_page=False)
            sw=await pg.evaluate("document.documentElement.scrollWidth"); cw=await pg.evaluate("document.documentElement.clientWidth")
            print(name,"scrollWidth",sw,"clientWidth",cw,"errors:",errs[:5])
            if name=="desktop-light":
                await pg.click("tr[data-id]"); await pg.wait_for_timeout(400); await pg.screenshot(path="/home/user/embodied-ai-governance-v4/dashboard/shot-drawer.png")
        await b.close()
asyncio.run(main())
