import { resolve } from 'node:path';
import { fileURLToPath } from 'node:url';
import { defineConfig } from 'vite';

const root = fileURLToPath(new URL('.', import.meta.url));

// Native multipage build: each primary page is its own HTML document.
export default defineConfig({
  build: {
    rollupOptions: {
      input: {
        home: resolve(root, 'index.html'),
        menu: resolve(root, 'menu/index.html'),
        catering: resolve(root, 'catering/index.html'),
        visit: resolve(root, 'visit/index.html'),
      },
    },
  },
});
