// Minifica os arquivos únicos da pasta dist/ (HTML, CSS e JS), para o código publicado
// ficar compacto e difícil de ler. Uso: node tools/minificar.mjs dist/lp-completa.html [...]
// Requer: cd tools && npm install
import { minify } from 'html-minifier-terser';
import { readFileSync, writeFileSync } from 'node:fs';

for (const arquivo of process.argv.slice(2)) {
  const antes = readFileSync(arquivo, 'utf8');
  const depois = await minify(antes, {
    collapseWhitespace: true,
    conservativeCollapse: false,
    removeComments: true,
    minifyCSS: true,
    minifyJS: { compress: { passes: 2 }, mangle: { toplevel: true }, format: { comments: false } },
    removeRedundantAttributes: true,
    useShortDoctype: true,
    keepClosingSlash: false,
  });
  writeFileSync(arquivo, depois);
  console.log(`${arquivo}: minificado ${(antes.length / 1024).toFixed(0)} KB -> ${(depois.length / 1024).toFixed(0)} KB`);
}
