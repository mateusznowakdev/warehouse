const STATE = { showOutOfStock: false, search: "" };

const table = document.getElementsByClassName("product-list-table")[0];

function e(id) {
  window.location.href = `/products/${id}`;
}

function s(index) {
  window.location.href = `{{ ENV_SEARCH_URL_PREFIX }}${encodeURI(index)}{{ ENV_SEARCH_URL_SUFFIX }}`;
}

function w(index) {
  window.location.href = `{{ ENV_WAREHOUSE_URL_PREFIX }}${encodeURI(index)}{{ ENV_WAREHOUSE_URL_SUFFIX }}`;
}

function updateTable() {
  const searchLower = normalizeString(STATE.search);

  [...table.tBodies[0].rows].forEach((r) => {
    const data = JSON.parse(r.dataset.json);

    // default condition
    let show = data.quantity > 0;
    // reset for all if checkbox checked
    if (STATE.showOutOfStock) {
      show = true;
    }
    // hide objects that do not match search query
    if (show) {
      if (
        !normalizeString(data.index).includes(searchLower) &&
        !normalizeString(data.description).includes(searchLower)
      ) {
        show = false;
      }
    }

    if (show) {
      r.classList.remove("hidden");
    } else {
      r.classList.add("hidden");
    }
  });
}

document.getElementById("showOutOfStock").onchange = (e) => {
  STATE.showOutOfStock = e.target.checked;
  updateTable();
};

document.getElementById("search").oninput = (e) => {
  STATE.search = e.target.value;
  updateTable();
};

document.getElementById("addButton").onclick = () => {
  window.location.href = "/products/new";
};

document.getElementById("printButton").onclick = () => {
  print();
};

document.getElementById("exportButton").onclick = () => {
  window.location.href = "/products/export";
};

const hash = window.location.hash;
if (hash.length > 0) {
  [...table.tBodies[0].rows].forEach((r) => {
    const data = JSON.parse(r.dataset.json);
    if (data.id == hash.substring(1)) {
      r.classList.add("last");
    }
  });
}
