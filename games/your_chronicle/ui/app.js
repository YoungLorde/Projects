"use strict";
/* Your Chronicle — data-driven UI framework prototype.
   - Loads game_data.json (exported from your_chronicle.db).
   - Renders condition-gated, collapsible panels & buttons.
   - Implements a small, safe evaluator for the condition grammar in
     ui_framework.yaml (phase_index, population, currency.<id>,
     building.<id>.tier, dungeon_rank_cleared, has_item.<id>, quest_done.<id>,
     achievement.<id>, rebirth_count, stat.<id>, plus AND/OR/NOT and comparisons).
   - Demonstrates additive-from-inventory equipment stats and a collapsible
     inventory with category dropdowns. */

let GAME = null;

/* ----------------------------- game state ------------------------------ */
const state = {
  phase_index: 1,
  level: 1,
  population: 0,
  rebirth_count: 0,
  dungeon_rank_cleared: -1,
  currency: { bronze: 0, silver: 0, gold: 0, zenu_coin: 0, mythril_coin: 0 },
  buildings: {},            // id -> tier
  items: {},                // id -> {item, qty, equipped}
  quests_done: {},          // id -> true
  achievements: {},         // id -> true
  baseStats: { hp: 50, atk: 10, def: 8, spd: 8, vit: 10, int: 8, lck: 5, cha: 8, ldr: 6 },
  seenUnlocked: {},         // key -> true (for the "new" highlight)
};

/* ----------------------- condition grammar parser ---------------------- */
/* Recursive-descent parser -> numeric/boolean result. No eval(). */
function tokenize(expr) {
  const re = /\s*(>=|<=|==|!=|>|<|\(|\)|\*|\+|-|AND|OR|NOT|&&|\|\||!|[A-Za-z_][A-Za-z0-9_.]*|\d+(?:\.\d+)?)/g;
  const toks = []; let m;
  while ((m = re.exec(expr)) !== null) { if (m[1] !== undefined) toks.push(m[1]); }
  return toks;
}
function parseCondition(expr) {
  if (!expr) return () => true;
  const toks = tokenize(expr);
  let i = 0;
  const peek = () => toks[i];
  const next = () => toks[i++];

  function resolve(name) {
    if (/^\d/.test(name)) return parseFloat(name);
    if (name === "true") return 1; if (name === "false") return 0;
    if (name === "phase_index") return state.phase_index;
    if (name === "player_level") return state.level;
    if (name === "population") return state.population;
    if (name === "rebirth_count") return state.rebirth_count;
    if (name === "dungeon_rank_cleared") return state.dungeon_rank_cleared;
    if (name === "max_phase") return state.phase_index;
    if (name === "deaths") return 0;
    const dot = name.split(".");
    if (dot[0] === "currency") return state.currency[dot[1]] || 0;
    if (dot[0] === "building") return (state.buildings[dot[1]] || 0); // building.<id>.tier
    if (dot[0] === "has_item") return state.items[dot[1]] ? 1 : 0;
    if (dot[0] === "quest_done") return state.quests_done[dot[1]] ? 1 : 0;
    if (dot[0] === "achievement") return state.achievements[dot[1]] ? 1 : 0;
    if (dot[0] === "stat") return totalStats()[dot[1]] || 0;
    return 0; // unknown variable -> 0 (keeps secrets locked)
  }
  // grammar: or := and (OR and)* ; and := cmp (AND cmp)* ;
  // cmp := add (op add)? ; add := mul (+|- mul)* ; mul := unary (* unary)* ;
  // unary := (NOT|!) unary | '(' or ')' | name|number
  function unary() {
    const t = peek();
    if (t === "NOT" || t === "!") { next(); return unary() ? 0 : 1; }
    if (t === "(") { next(); const v = orExpr(); if (peek() === ")") next(); return v; }
    return resolve(next());
  }
  function mul() { let v = unary(); while (peek() === "*") { next(); v *= unary(); } return v; }
  function add() { let v = mul(); while (peek() === "+" || peek() === "-") { const o = next(); const r = mul(); v = o === "+" ? v + r : v - r; } return v; }
  function cmp() {
    let v = add(); const o = peek();
    if ([">=", "<=", ">", "<", "==", "!="].includes(o)) {
      next(); const r = add();
      switch (o) { case ">=": return v >= r ? 1 : 0; case "<=": return v <= r ? 1 : 0;
        case ">": return v > r ? 1 : 0; case "<": return v < r ? 1 : 0;
        case "==": return v === r ? 1 : 0; case "!=": return v !== r ? 1 : 0; }
    }
    return v;
  }
  function andExpr() { let v = cmp(); while (peek() === "AND" || peek() === "&&") { next(); const r = cmp(); v = (v && r) ? 1 : 0; } return v; }
  function orExpr() { let v = andExpr(); while (peek() === "OR" || peek() === "||") { next(); const r = andExpr(); v = (v || r) ? 1 : 0; } return v; }

  return () => { i = 0; try { return !!orExpr(); } catch (e) { return false; } };
}
function check(expr) { return parseCondition(expr)(); }

/* ------------------------------- stats --------------------------------- */
/* Additive-from-inventory: every held item grants full stats; equipping adds
   a +15% attunement bonus (see data/systems/stats.yaml). */
function totalStats() {
  const t = { ...state.baseStats };
  for (const id in state.items) {
    const e = state.items[id];
    const s = e.item.stats || {};
    const mult = e.equipped ? 1.15 : 1.0;
    for (const k in s) t[k] = (t[k] || 0) + Math.round(s[k] * e.qty * mult);
  }
  return t;
}

/* ------------------------------ helpers -------------------------------- */
function human(n) {
  const u = ["", "K", "M", "B", "T", "Qa", "Qi"]; let i = 0; n = Number(n);
  while (n >= 1000 && i < u.length - 1) { n /= 1000; i++; }
  return (n % 1 === 0 ? n : n.toFixed(1)) + u[i];
}
function rarityColor(id) {
  const r = (GAME.rarity || []).find(x => x.id === id);
  return r ? r.color : "#cdd6ff";
}
function el(tag, cls, html) { const e = document.createElement(tag); if (cls) e.className = cls; if (html != null) e.innerHTML = html; return e; }

/* ------------------------- currency auto-convert ----------------------- */
function autoConvert() {
  const chain = [["bronze", 1000, "silver"], ["silver", 1000, "gold"]];
  for (const [from, per, to] of chain) {
    if (state.currency[from] >= per) {
      const c = Math.floor(state.currency[from] / per);
      state.currency[from] -= c * per; state.currency[to] = (state.currency[to] || 0) + c;
    }
  }
}

/* ------------------------------ rendering ------------------------------ */
function renderHeader() {
  const p = GAME.phases.find(x => x.idx === state.phase_index) || {};
  document.getElementById("phaseline").textContent =
    `Phase ${state.phase_index}/45 — ${p.name || "?"} (${p.band || ""})`;
  const order = ["bronze", "silver", "gold", "zenu_coin", "mythril_coin"];
  const names = { bronze: "Bronze", silver: "Silver", gold: "Gold", zenu_coin: "Zenu", mythril_coin: "Mythril" };
  document.getElementById("currencies").innerHTML = order
    .map(k => `<span class="coin">${names[k]} <b>${human(state.currency[k] || 0)}</b></span>`).join("");
}

const PANEL_BODY = {};   // panel id -> render function

function renderPanels() {
  const showLocked = document.getElementById("c_show_locked").checked;
  const host = document.getElementById("panels");
  host.innerHTML = "";
  for (const p of GAME.ui_framework.panels) {
    if (["header", "main_click"].includes(p.id)) continue; // rendered elsewhere
    const unlocked = p.always_visible || !p.unlock || check(p.unlock);
    if (!unlocked && !showLocked) continue;              // hidden entirely
    const panel = el("div", "panel" + (unlocked ? "" : " locked"));
    panel.dataset.panel = p.id;

    // "new" highlight the first time a panel unlocks
    const key = "panel:" + p.id;
    if (unlocked && !state.seenUnlocked[key]) panel.classList.add("isnew");

    const collapsed = (p.default === "closed");
    if (collapsed && unlocked) panel.classList.add("collapsed");

    const head = el("div", "panel-head" + (unlocked ? " collapsible" : ""));
    head.innerHTML = `<span>${unlocked ? "▾ " : "🔒 "}${p.title}</span>` +
      (unlocked ? "" : `<span class="lockmsg">${p.unlock}</span>`);
    if (unlocked) head.onclick = () => {
      panel.classList.toggle("collapsed");
      panel.classList.remove("isnew"); state.seenUnlocked[key] = true;
    };
    panel.appendChild(head);

    const body = el("div", "panel-body");
    if (unlocked && PANEL_BODY[p.id]) PANEL_BODY[p.id](body);
    else if (unlocked) body.innerHTML = `<p class="hint">Panel "${p.id}" — content driven by game data.</p>`;
    panel.appendChild(body);
    host.appendChild(panel);
  }
  renderButtonsBar();
}

/* ---- individual panel bodies ---- */
PANEL_BODY.base = (b) => {
  b.innerHTML = `<p class="hint">Dwelling upgrade path (cap grows ${human(1)}→${human(1e12)}).</p>`;
  const ul = el("ul", "list");
  GAME.buildings.forEach(bd => {
    ul.appendChild(el("li", "row",
      `<span>${bd.name} <small>tier ${bd.tier}</small></span><small>cap ${human(bd.pop_capacity)}</small>`));
  });
  b.appendChild(ul);
};
PANEL_BODY.dungeons = (b) => {
  const ul = el("ul", "list");
  GAME.dungeons.forEach(d => {
    const open = state.phase_index >= d.unlock_phase;
    ul.appendChild(el("li", "row",
      `<span style="color:${rarityColor(d.max_rarity)}">${d.name}</span>` +
      `<small>${open ? "lv " + d.level_band : "unlock phase " + d.unlock_phase} · boss: ${d.boss}</small>`));
  });
  b.appendChild(ul);
};
PANEL_BODY.quests = (b) => {
  const ul = el("ul", "list");
  GAME.quests_sample.slice(0, 30).forEach(q => {
    const ok = check(q.unlock_condition);
    ul.appendChild(el("li", "row",
      `<span>${q.name} <span class="tag">${q.type}</span></span>` +
      `<small>${ok ? "available" : "🔒 " + q.unlock_condition}</small>`));
  });
  b.appendChild(el("p", "hint", `Showing 30 of ${GAME.counts.quests} quests (full set in DB).`));
  b.appendChild(ul);
};
PANEL_BODY.achievements = (b) => {
  const ul = el("ul", "list");
  GAME.achievements_sample.slice(0, 30).forEach(a => {
    const got = check(a.condition);
    ul.appendChild(el("li", "row",
      `<span>${got ? "🏆" : "▫️"} ${a.name}</span><small>${a.points}pt</small>`));
  });
  b.appendChild(el("p", "hint", `Showing 30 of ${GAME.counts.achievements} (hidden ones stay invisible until met).`));
  b.appendChild(ul);
};
PANEL_BODY.inventory = (b) => {
  const t = totalStats();
  const summary = el("div", "statline");
  ["hp", "atk", "def", "spd", "int"].forEach(k =>
    summary.appendChild(el("div", "stat", `${k.toUpperCase()}<b>${human(t[k] || 0)}</b>`)));
  b.appendChild(el("p", "hint", "Additive stats: items grant their full stats just by being held."));
  b.appendChild(summary);

  const groups = {};
  for (const id in state.items) {
    const e = state.items[id]; const g = e.item.group || "Misc";
    (groups[g] = groups[g] || []).push(e);
  }
  if (Object.keys(groups).length === 0) { b.appendChild(el("p", "hint", "Inventory empty — use “Grant sample equipment”.")); return; }
  for (const g in groups) {
    const d = el("details", "group"); d.open = true;
    d.appendChild(el("summary", null, `${g} (${groups[g].length})`));
    const ul = el("ul", "list");
    groups[g].forEach(e => {
      const statTxt = Object.entries(e.item.stats || {}).map(([k, v]) => `+${v} ${k}`).join(", ");
      const li = el("li", "row",
        `<span style="color:${rarityColor(e.item.rarity)}">${e.item.name} ×${e.qty}` +
        (e.equipped ? ` <span class="equip-on">[attuned +15%]</span>` : "") +
        `</span><small>${statTxt}</small>`);
      const btn = el("button", "btn", e.equipped ? "Unattune" : "Attune");
      btn.onclick = () => { e.equipped = !e.equipped; refresh(); };
      li.appendChild(btn); ul.appendChild(li);
    });
    d.appendChild(ul); b.appendChild(d);
  }
};
PANEL_BODY.equipment = PANEL_BODY.inventory;
PANEL_BODY.codex = (b) => {
  b.innerHTML = `<p class="hint">World: <b>Orden</b>. Foe: the Void &amp; the Hollow Star.</p>`;
  const ul = el("ul", "list");
  GAME.npcs.slice(0, 12).forEach(n => ul.appendChild(el("li", "row",
    `<span>${n.name}</span><small>${n.role || ""} ${n.recruitable ? "· recruitable" : ""}</small>`)));
  b.appendChild(ul);
};
PANEL_BODY.rebirth = (b) => {
  b.innerHTML = `<p class="hint">Reset for compounding multipliers (Ascension Essence).</p>
    <div class="row"><span>Rebirths</span><b>${state.rebirth_count}</b></div>
    <div class="row"><span>Est. all-gain mult</span><b>${(1 + state.rebirth_count * 0.5).toFixed(2)}×</b></div>`;
};
PANEL_BODY.survival = (b) => {
  ["Food", "Water", "Warmth", "Health", "Morale"].forEach(n =>
    b.appendChild(el("div", "row", `<span>${n}</span><small>stable</small>`)));
};
PANEL_BODY.shops = (b) => {
  const ul = el("ul", "list");
  GAME.npcs.filter(n => n.role_category === "vendor").forEach(v =>
    ul.appendChild(el("li", "row", `<span>${v.name}</span><small>${v.role}</small>`)));
  b.appendChild(ul);
};
PANEL_BODY.villagers = (b) => {
  b.innerHTML = `<div class="row"><span>Population</span><b>${human(state.population)}</b></div>
    <p class="hint">Delegate villagers to 14 jobs; their stats add to yours.</p>`;
  const ul = el("ul", "list");
  GAME.npcs.filter(n => n.recruitable).slice(0, 8).forEach(n =>
    ul.appendChild(el("li", "row", `<span>${n.name}</span><small>${n.archetype || ""} ${n.rarity || ""}</small>`)));
  b.appendChild(ul);
};
PANEL_BODY.settlements = (b) => { b.innerHTML = `<p class="hint">Found new settlements once you build the Apartment Complex (BLD-004). Cost scales ×3 per settlement owned.</p>`; };
PANEL_BODY.crafting = (b) => { b.innerHTML = `<p class="hint">Gather → refine → craft. ${human(GAME.counts.materials)} materials, every one reason-tagged.</p>`; };
PANEL_BODY.research = (b) => { b.innerHTML = `<p class="hint">Unlocks with the Research Lab (BLD-007). Drives the space age.</p>`; };

/* ---- example condition-gated buttons (from ui_framework.buttons) ---- */
function renderButtonsBar() {
  let bar = document.getElementById("buttonbar");
  if (!bar) {
    const panel = el("div", "panel always");
    panel.innerHTML = `<div class="panel-head"><span>Actions (condition-gated buttons)</span></div>`;
    bar = el("div", "panel-body"); bar.id = "buttonbar";
    panel.appendChild(bar);
    document.getElementById("left-col").appendChild(panel);
  }
  bar.innerHTML = "";
  GAME.ui_framework.buttons.forEach(btn => {
    const ok = !btn.unlock || check(btn.unlock);
    const key = "btn:" + btn.id;
    const b = el("button", "btn" + (ok ? "" : " locked") + (ok && !state.seenUnlocked[key] ? " isnew" : ""), btn.label);
    if (!ok) b.dataset.req = btn.unlock;
    else b.onclick = () => { state.seenUnlocked[key] = true; alert(`Action: ${btn.action}`); refresh(); };
    bar.appendChild(b);
  });
}

/* ------------------------------- loop ---------------------------------- */
function refresh() { autoConvert(); renderHeader(); renderPanels(); renderClickStats(); }
function renderClickStats() {
  const t = totalStats();
  document.getElementById("clickstats").innerHTML =
    `Level ${state.level} · ATK ${human(t.atk)} · HP ${human(t.hp)} · Pop ${human(state.population)}`;
}

/* ------------------------------ controls ------------------------------- */
function wire() {
  document.getElementById("bigclick").onclick = () => {
    const t = totalStats();
    state.currency.bronze += 5 + Math.floor(t.atk / 5);
    refresh();
  };
  const bind = (rid, oid, fn) => {
    const r = document.getElementById(rid), o = document.getElementById(oid);
    r.oninput = () => { o.value = r.value; fn(+r.value); refresh(); };
  };
  bind("r_phase", "o_phase", v => state.phase_index = v);
  bind("r_pop", "o_pop", v => state.population = v);
  bind("r_rb", "o_rb", v => state.rebirth_count = v);
  bind("r_dr", "o_dr", v => state.dungeon_rank_cleared = v);
  document.getElementById("c_shack").onchange = e => { state.buildings["BLD-001"] = e.target.checked ? 1 : 0; refresh(); };
  document.getElementById("c_show_locked").onchange = refresh;
  document.getElementById("give_gold").onclick = () => { state.currency.gold += 1000; refresh(); };
  document.getElementById("give_item").onclick = () => {
    const samples = [
      { id: "EQ-SWORD", name: "Emberfang Blade", group: "Weapons", rarity: "rare", stats: { atk: 40, spd: 6 } },
      { id: "EQ-ARMOR", name: "Ashsteel Plate", group: "Armor", rarity: "uncommon", stats: { def: 30, hp: 80 } },
      { id: "EQ-RING", name: "Ring of the Scribe", group: "Armor", rarity: "epic", stats: { int: 25, lck: 10 } },
    ];
    samples.forEach(s => {
      if (state.items[s.id]) state.items[s.id].qty++;
      else state.items[s.id] = { item: s, qty: 1, equipped: false };
    });
    if (state.phase_index < 2) { state.phase_index = 2; document.getElementById("r_phase").value = 2; document.getElementById("o_phase").value = 2; }
    refresh();
  };
}

/* ------------------------------- boot ---------------------------------- */
fetch("game_data.json")
  .then(r => r.json())
  .then(d => {
    GAME = d;
    document.getElementById("counts").textContent =
      `${d.counts.characters} NPCs · ${human(d.counts.materials)} materials · ` +
      `${d.counts.quests} quests · ${d.counts.achievements} achievements · ` +
      `${d.counts.phases} phases · ${d.counts.dungeons} dungeon ranks · ${d.counts.enemies} enemies`;
    wire(); refresh();
  })
  .catch(e => {
    document.body.insertAdjacentHTML("beforeend",
      `<p style="color:#ff7777;padding:16px">Could not load game_data.json (${e}). ` +
      `Serve this folder over HTTP: <code>python -m http.server</code> then open the shown URL.</p>`);
  });
