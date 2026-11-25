const test = require("node:test");
const assert = require("node:assert");
const vulnerable = require("./vulnerable");
const fixed = require("./fixed");

test("vulnerable redirects off-site", () => {
  assert.strictEqual(vulnerable.redirectTarget("https://evil.example/login"), "https://evil.example/login");
});
test("fixed blocks off-site targets", () => {
  for (const t of ["https://evil.example", "//evil.example", "/\\evil.example", "javascript:alert(1)"]) {
    assert.strictEqual(fixed.redirectTarget(t), "/dashboard");
  }
});
test("fixed keeps internal paths", () => {
  assert.strictEqual(fixed.redirectTarget("/invoices?page=2"), "/invoices?page=2");
});
