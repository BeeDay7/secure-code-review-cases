const test = require("node:test");
const assert = require("node:assert");
const vulnerable = require("./vulnerable");
const fixed = require("./fixed");

const PAYLOAD = '<img src=x onerror="alert(1)">';

test("vulnerable output contains live markup", () => {
  assert.ok(vulnerable.renderComment("eve", PAYLOAD).includes("<img"));
});
test("fixed output is encoded", () => {
  const html = fixed.renderComment("eve", PAYLOAD);
  assert.ok(!html.includes("<img") && html.includes("&lt;img"));
});
