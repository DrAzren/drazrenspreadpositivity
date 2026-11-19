// Flags any visible character/prop sprite that leaves the 1080x1920 canvas (= would look cut off).
// Usage: NODE_PATH=$(npm root -g) node sprite_edge_check.js <path/to/index.html> [step=0.25]
const { chromium } = require("playwright");
(async () => {
  const [, , file, stepArg] = process.argv;
  const step = Number(stepArg || 0.25);
  const b = await chromium.launch();
  const p = await b.newPage({ viewport: { width: 1080, height: 1920 } });
  // serve GSAP from a local copy (the CDN may be unreachable from a bare browser)
  const glob = require("child_process").execSync("find / -name gsap.min.js -path '*gsap@3*' -not -path '/proc/*' 2>/dev/null | head -1").toString().trim();
  if (glob) await p.route(/gsap.*\.js$/, (r) => r.fulfill({ path: glob, contentType: "application/javascript" }));
  p.on("pageerror", (e) => console.log("pageerror:", e.message));
  await p.goto("file://" + require("path").resolve(file), { waitUntil: "domcontentloaded" });
  await p.waitForTimeout(2500);
  await p.waitForFunction(() => !!(window.__timelines && window.__timelines.main), null, { polling: 250, timeout: 60000 });
  await p.evaluate(() => document.fonts.ready);
  const dur = await p.evaluate(() => Number(document.getElementById("root").dataset.duration));
  const issues = {};
  for (let t = 0; t <= dur; t += step) {
    const found = await p.evaluate((t) => {
      const tl = window.__timelines.main; tl.seek(t, false);
      const out = [];
      for (const sc of document.querySelectorAll(".scene")) {
        const s = Number(sc.dataset.start), d = Number(sc.dataset.duration);
        if (!(t >= s && t < s + d)) continue;
        for (const el of sc.querySelectorAll("img.spr, img.prop, .rig")) {
          let op = 1, n = el;
          while (n && n !== sc) { const cs = getComputedStyle(n); op *= Number(cs.opacity); if (cs.display === "none") op = 0; n = n.parentElement; }
          if (op < 0.05) continue;
          const r = el.getBoundingClientRect();
          const tol = 2;
          if (r.left < -tol || r.top < -tol || r.right > 1080 + tol || r.bottom > 1920 + tol)
            out.push(`${el.id || el.getAttribute("src")}: [${r.left.toFixed(0)},${r.top.toFixed(0)},${r.right.toFixed(0)},${r.bottom.toFixed(0)}]`);
        }
      }
      return out;
    }, t);
    for (const f of found) { const k = f.split(":")[0]; (issues[k] = issues[k] || []).push(`${t.toFixed(2)}s ${f.split(": ")[1]}`); }
  }
  await b.close();
  const keys = Object.keys(issues);
  if (!keys.length) { console.log("PASS: no sprite leaves the canvas"); process.exit(0); }
  for (const k of keys) console.log(`FAIL ${k}: ${issues[k].length} samples, first ${issues[k][0]}, last ${issues[k][issues[k].length - 1]}`);
  process.exit(1);
})();
