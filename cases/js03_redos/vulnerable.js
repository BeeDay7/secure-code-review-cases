// Flaw: nested quantifier causes catastrophic backtracking.
const EMAIL = /^([a-zA-Z0-9]+)*@[a-zA-Z0-9]+\.[a-z]{2,}$/;
const isEmail = (s) => EMAIL.test(s);
module.exports = { isEmail, EMAIL };
