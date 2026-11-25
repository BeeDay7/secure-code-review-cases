// Fix: no nested quantifiers, plus a length cap.
const EMAIL = /^[A-Za-z0-9._%+-]{1,64}@[A-Za-z0-9-]{1,63}(?:\.[A-Za-z0-9-]{1,63})*\.[A-Za-z]{2,24}$/;
const isEmail = (s) => typeof s === "string" && s.length <= 254 && EMAIL.test(s);
module.exports = { isEmail, EMAIL };
