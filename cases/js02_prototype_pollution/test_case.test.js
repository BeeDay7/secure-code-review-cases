const test = require("node:test");
const assert = require("node:assert");
const vulnerable = require("./vulnerable");
const fixed = require("./fixed");

const payload = () => JSON.parse('{"__proto__": {"isAdmin": true}}');

test("vulnerable merge pollutes Object.prototype", () => {
  vulnerable.merge({}, payload());
  assert.strictEqual({}.isAdmin, true);
  delete Object.prototype.isAdmin;
});
test("fixed merge leaves Object.prototype untouched", () => {
  fixed.merge({}, payload());
  assert.strictEqual({}.isAdmin, undefined);
});
