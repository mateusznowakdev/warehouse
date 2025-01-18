function normalizeString(string) {
  return string
    .normalize("NFD")
    .replace(/[\u0300-\u036f]/g, "")
    .toLowerCase()
    .replace(/[^a-z0-9]+/g, '')
}

[...document.getElementsByClassName("fmt-date")].forEach((e) => {
  e.innerText = new Date(e.innerText).toLocaleDateString(undefined, {
    dateStyle: "short",
  });
});

[...document.getElementsByClassName("fmt-datetime")].forEach((e) => {
  e.innerText = new Date(e.innerText).toLocaleString(undefined, {
    dateStyle: "short",
    timeStyle: "medium",
  });
});

[...document.getElementsByClassName("fmt-decimal")].forEach((e) => {
  e.innerText = new Intl.NumberFormat(undefined, {
    minimumFractionDigits: 2,
    maximumFractionDigits: 2,
  }).format(e.innerText);
});
