const MAP = { "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;", "'": "&#39;" };
const escapeHtml = (s) => String(s).replace(/[&<>"']/g, (c) => MAP[c]);

function renderComment(author, text) {
  // Fix: encode every untrusted value.
  return `<li><b>${escapeHtml(author)}</b>: ${escapeHtml(text)}</li>`;
}
module.exports = { renderComment, escapeHtml };
