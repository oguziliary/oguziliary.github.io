(function() {
    function initFilters() {
        var searchInput = document.getElementById('post-search');
        var langButtons = document.querySelectorAll('.lang-filter-button');

        // No posts / filters on this page
        var posts = document.querySelectorAll('.content-main .post-list');
        if (!posts.length) {
            return;
        }

        function getActiveLanguages() {
            var active = [];
            langButtons.forEach(function(btn) {
                if (btn.classList.contains('lang-filter-button--active')) {
                    var lang = btn.getAttribute('data-lang');
                    if (lang) {
                        active.push(lang);
                    }
                }
            });
            return active;
        }

        function updatePosts() {
            var term = searchInput ? searchInput.value.toLowerCase().trim() : '';
            var activeLangs = getActiveLanguages();
            var hasResults = false;

            posts.forEach(function(post) {
                var titleElement = post.querySelector('h2 a');
                if (!titleElement) {
                    return;
                }

                var title = titleElement.textContent.toLowerCase();
                var postLang = post.getAttribute('data-lang') || '';

                var matchesSearch = term === '' || title.includes(term);
                var matchesLang = !activeLangs.length || activeLangs.indexOf(postLang) !== -1;
                var visible = matchesSearch && matchesLang;

                post.style.display = visible ? '' : 'none';
                if (visible) {
                    hasResults = true;
                }
            });

            // Show a message if no results found
            var noResultsMsg = document.getElementById('no-search-results');
            if ((term || activeLangs.length) && !hasResults) {
                if (!noResultsMsg) {
                    noResultsMsg = document.createElement('p');
                    noResultsMsg.id = 'no-search-results';
                    noResultsMsg.className = 'no-search-results';
                    noResultsMsg.textContent = 'No posts found matching current filters.';
                    var contentMain = document.querySelector('.content-main');
                    if (contentMain) {
                        contentMain.appendChild(noResultsMsg);
                    }
                }
            } else if (noResultsMsg) {
                noResultsMsg.remove();
            }
        }

        // Initialize language buttons (EN / TR)
        // Both buttons are active by default, regardless of page language
        if (langButtons.length) {
            var defaultActive = ['en', 'tr'];

            langButtons.forEach(function(btn) {
                var lang = (btn.getAttribute('data-lang') || '').toLowerCase();
                var isActive = defaultActive.indexOf(lang) !== -1;
                if (isActive) {
                    btn.classList.add('lang-filter-button--active');
                    btn.setAttribute('aria-pressed', 'true');
                } else {
                    btn.classList.remove('lang-filter-button--active');
                    btn.setAttribute('aria-pressed', 'false');
                }

                btn.addEventListener('click', function() {
                    var currentlyActive = btn.classList.contains('lang-filter-button--active');

                    if (currentlyActive) {
                        // Only allow turning off if at least one other button stays active
                        var activeCount = getActiveLanguages().length;
                        if (activeCount <= 1) {
                            return;
                        }
                        btn.classList.remove('lang-filter-button--active');
                        btn.setAttribute('aria-pressed', 'false');
                    } else {
                        btn.classList.add('lang-filter-button--active');
                        btn.setAttribute('aria-pressed', 'true');
                    }

                    updatePosts();
                });
            });
        }

        // Search on input (real-time)
        if (searchInput) {
            searchInput.addEventListener('input', function() {
                updatePosts();
            });
        }

        // Initial state - apply filters once
        updatePosts();
    }

    // Wait for DOM to be ready
    if (document.readyState === 'loading') {
        document.addEventListener('DOMContentLoaded', initFilters);
    } else {
        // DOM is already ready
        initFilters();
    }
})();

