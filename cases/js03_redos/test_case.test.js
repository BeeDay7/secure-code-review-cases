const test = require("node:test");
const assert = require("node:assert");
const vulnerable = require("./vulnerable");
const fixed = require("./fixed");

const nested = (src) => /\([^)]*[+*]\)[+*]/.test(src);

test("vulnerable pattern has a nested quantifier", () => {
  assert.ok(nested(vulnerable.EMAIL.source));
});
test("fixed pattern is fast on hostile input", () => {
  const hostile = "a".repeat(5000) + "!";
  const t0 = Date.now();
  assert.strictEqual(fixed.isEmail(hostile), false);
  assert.ok(Date.now() - t0 < 50);
  assert.ok(!nested(fixed.EMAIL.source));
});
test("fixed pattern accepts a normal address", () => {
  assert.ok(fixed.isEmail("abidemi@example.org"));
});
