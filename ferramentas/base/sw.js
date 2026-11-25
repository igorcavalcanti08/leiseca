/* Service Worker — Lei Seca C/E
   IMPORTANTE: a cada alteração em index.html (ou em qualquer arquivo listado),
   aumente a versão abaixo. É isso que faz o app baixar a nova versão. */
const CACHE = 'leiseca-v2.1.0';
const ASSETS = ['./', './index.html', './manifest.json', './icon-192.png', './icon-512.png'];

self.addEventListener('install', event => {
  event.waitUntil(caches.open(CACHE).then(c => c.addAll(ASSETS)));
  // Na 1ª instalação não há versão antiga: ativa direto.
  // Nas atualizações, espera o usuário tocar em "Atualizar" (mensagem SKIP_WAITING).
});

self.addEventListener('activate', event => {
  event.waitUntil((async () => {
    const keys = await caches.keys();
    await Promise.all(keys.filter(k => k !== CACHE && k.startsWith('leiseca-')).map(k => caches.delete(k)));
    await self.clients.claim();
  })());
});

self.addEventListener('message', event => {
  if (event.data === 'SKIP_WAITING') self.skipWaiting();
});

// Cache-first: funciona 100% offline; a rede só é usada para o que não estiver em cache.
self.addEventListener('fetch', event => {
  const req = event.request;
  if (req.method !== 'GET' || new URL(req.url).origin !== self.location.origin) return;
  event.respondWith((async () => {
    const cache = await caches.open(CACHE);
    if (req.mode === 'navigate') {
      return (await cache.match('./index.html')) || (await cache.match('./')) || fetch(req);
    }
    const hit = await cache.match(req, {ignoreSearch: true});
    if (hit) return hit;
    try {
      const res = await fetch(req);
      if (res.ok && res.type === 'basic') cache.put(req, res.clone());
      return res;
    } catch (e) {
      return new Response('Offline', {status: 503, statusText: 'Offline'});
    }
  })());
});
