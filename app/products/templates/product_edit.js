const STATE = { index: "" };

const table = document.getElementsByClassName("product-list-table")[0];

document.getElementById("cancelButton").onclick = () => {
  window.location.href = "/products";
};

if (table) {
  function e(id) {
    window.location.href = `/products/${id}`;
  }

  function updateTable() {
    const indexLower = normalizeString(STATE.index);
    let showAny = false;

    [...table.tBodies[0].rows].forEach((r) => {
      const data = JSON.parse(r.dataset.json);
      const show = normalizeString(data.index) === indexLower;

      if (show) {
        showAny = true;
        r.classList.remove("hidden");
      } else {
        r.classList.add("hidden");
      }
    });

    if (showAny) {
      table.parentNode.classList.remove("hidden");
    } else {
      table.parentNode.classList.add("hidden");
    }
  }

  document.getElementById("index").oninput = (e) => {
    STATE.index = e.target.value;
    updateTable();
  };
}
