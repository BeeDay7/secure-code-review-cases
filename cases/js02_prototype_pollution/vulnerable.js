function merge(target, source) {
  for (const key in source) {
    // Flaw: no filtering of dangerous keys.
    if (typeof source[key] === "object" && source[key] !== null) {
      if (typeof target[key] !== "object" || target[key] === null) target[key] = {};
      merge(target[key], source[key]);
    } else {
      target[key] = source[key];
    }
  }
  return target;
}
module.exports = { merge };
