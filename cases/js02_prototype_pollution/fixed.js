const BLOCKED = new Set(["__proto__", "constructor", "prototype"]);

function merge(target, source) {
  for (const key of Object.keys(source)) {
    // Fix: skip keys that reach the prototype chain.
    if (BLOCKED.has(key)) continue;
    const value = source[key];
    if (typeof value === "object" && value !== null) {
      if (typeof target[key] !== "object" || target[key] === null) target[key] = {};
      merge(target[key], value);
    } else {
      target[key] = value;
    }
  }
  return target;
}
module.exports = { merge };
