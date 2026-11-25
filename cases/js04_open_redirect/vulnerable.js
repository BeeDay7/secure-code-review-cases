function redirectTarget(next) {
  // Flaw: any URL is accepted.
  return next || "/dashboard";
}
module.exports = { redirectTarget };
