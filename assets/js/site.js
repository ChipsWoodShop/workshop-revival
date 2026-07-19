(function () {
  "use strict";

  document.querySelectorAll("[data-current-year]").forEach(function (element) {
    element.textContent = new Date().getFullYear();
  });

  document.querySelectorAll("[data-project-filters]").forEach(function (filterGroup) {
    var scope = filterGroup.parentElement;
    var cards = Array.from(scope.querySelectorAll("[data-category]"));
    var status = scope.querySelector("[data-filter-status]");
    var emptyMessage = scope.querySelector("[data-empty-message]");

    filterGroup.addEventListener("click", function (event) {
      var button = event.target.closest("[data-filter]");
      if (!button) return;

      var selected = button.dataset.filter;
      var visibleCount = 0;

      filterGroup.querySelectorAll("[data-filter]").forEach(function (candidate) {
        var isSelected = candidate === button;
        candidate.classList.toggle("is-active", isSelected);
        candidate.setAttribute("aria-pressed", String(isSelected));
      });

      cards.forEach(function (card) {
        var categories = card.dataset.category.split(" ");
        var isVisible = selected === "all" || categories.includes(selected);
        card.hidden = !isVisible;
        if (isVisible) visibleCount += 1;
      });

      if (status) {
        var categoryName = button.textContent.trim();
        status.textContent = visibleCount + " project" + (visibleCount === 1 ? "" : "s") + " shown for " + categoryName + ".";
      }
      if (emptyMessage) emptyMessage.hidden = visibleCount !== 0;
    });
  });
}());
