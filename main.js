console.log("Hello, World!");

function toggleSearch() {
    var searchInput = document.getElementById("search");
    if (searchInput.classList.contains("hidden")) {
        searchInput.classList.remove("hidden");
    } else {
        searchInput.classList.add("hidden");
    }
}