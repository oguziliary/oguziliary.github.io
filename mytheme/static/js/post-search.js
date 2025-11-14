(function() {
    function initSearch() {
        var searchInput = document.getElementById('post-search');
        if (!searchInput) {
            return;
        }

        function filterPosts(searchTerm) {
            var posts = document.querySelectorAll('.content-main .post-list');
            var term = searchTerm.toLowerCase().trim();
            var hasResults = false;

            if (posts.length === 0) {
                return;
            }

            posts.forEach(function(post) {
                var titleElement = post.querySelector('h2 a');
                if (!titleElement) {
                    return;
                }

                var title = titleElement.textContent.toLowerCase();
                var matches = term === '' || title.includes(term);

                if (matches) {
                    post.style.display = '';
                    hasResults = true;
                } else {
                    post.style.display = 'none';
                }
            });

            // Show a message if no results found
            var noResultsMsg = document.getElementById('no-search-results');
            if (term && !hasResults) {
                if (!noResultsMsg) {
                    noResultsMsg = document.createElement('p');
                    noResultsMsg.id = 'no-search-results';
                    noResultsMsg.className = 'no-search-results';
                    noResultsMsg.textContent = 'No posts found matching "' + searchTerm + '"';
                    var contentMain = document.querySelector('.content-main');
                    if (contentMain) {
                        contentMain.appendChild(noResultsMsg);
                    }
                }
            } else if (noResultsMsg) {
                noResultsMsg.remove();
            }
        }

        // Search on input (real-time)
        searchInput.addEventListener('input', function(e) {
            filterPosts(e.target.value);
        });

        // Initialize - show all posts
        filterPosts('');
    }

    // Wait for DOM to be ready
    if (document.readyState === 'loading') {
        document.addEventListener('DOMContentLoaded', initSearch);
    } else {
        // DOM is already ready
        initSearch();
    }
})();

