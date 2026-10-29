// Checks (default) or applies (--fix) polytypo typography on the Markdown files.
// Exits 1 if any file is not already normalized.
import { transform } from "polytypo/markdown";
import { readFileSync, writeFileSync } from "node:fs";

const FILES = ["README.md", "CONTRIBUTING.md", ".github/PULL_REQUEST_TEMPLATE.md"];
const OPTS = { locale: "en-GB", dialect: "commonmark" };
// awesome-lint requires a plain hyphen between an entry's link and its description,
// while polytypo turns " - " into an en dash. Only that separator is exempt.
const ENTRY_SEPARATOR = /^(- \[[^\]]+\]\([^)\s]+\)) – /gm;
const normalize = (text) => transform(text, OPTS).replace(ENTRY_SEPARATOR, "$1 - ");
const fix = process.argv.includes("--fix");
let dirty = 0;

for (const file of FILES) {
  const original = readFileSync(file, "utf8");
  const normalized = normalize(original);
  if (normalize(normalized) !== normalized) {
    console.error(`${file}: polytypo is not idempotent on this file`);
    process.exit(1);
  }
  if (normalized === original) continue;
  if (fix) {
    writeFileSync(file, normalized);
    console.log(`fixed: ${file}`);
    continue;
  }
  dirty++;
  const a = original.split("\n");
  const b = normalized.split("\n");
  for (let i = 0; i < Math.max(a.length, b.length); i++) {
    if (a[i] !== b[i]) console.error(`${file}:${i + 1}\n  - ${a[i]}\n  + ${b[i]}`);
  }
}

if (dirty) {
  console.error(`\n${dirty} file(s) need typography. Run: pnpm typography:fix`);
  process.exit(1);
}
console.log("typography ok");
