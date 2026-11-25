function renderComment(author, text) {
  // Flaw: raw interpolation into HTML.
  return `<li><b>${author}</b>: ${text}</li>`;
}
module.exports = { renderComment };
