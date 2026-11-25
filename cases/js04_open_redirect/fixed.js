function redirectTarget(next) {
  // Fix: only same-site relative paths.
  if (typeof next !== "string" || !next.startsWith("/") || next.startsWith("//") || next.includes("\\")) {
    return "/dashboard";
  }
  const url = new URL(next, "https://app.example");
  return url.origin === "https://app.example" ? url.pathname + url.search : "/dashboard";
}
module.exports = { redirectTarget };
