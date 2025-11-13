(function() {
    var storageKey = 'preferred-theme';
    var root = document.documentElement;

    function getStoredTheme() {
        try {
            return localStorage.getItem(storageKey);
        } catch (e) {
            return null;
        }
    }

    function setStoredTheme(value) {
        try {
            localStorage.setItem(storageKey, value);
        } catch (e) {
            /* ignore storage failures */
        }
    }

    function applyTheme(theme, persist) {
        var targetTheme = theme === 'dark' ? 'dark' : 'light';
        root.classList.remove('theme-light', 'theme-dark');
        root.classList.add(targetTheme === 'dark' ? 'theme-dark' : 'theme-light');
        root.dataset.theme = targetTheme;
        if (persist) {
            setStoredTheme(targetTheme);
        }
        updateToggle(targetTheme);
    }

    function updateToggle(theme) {
        var toggle = document.getElementById('theme-toggle');
        if (!toggle) {
            return;
        }
        var isDark = theme === 'dark';
        toggle.setAttribute('aria-pressed', isDark.toString());
        toggle.setAttribute('aria-label', isDark ? 'Switch to light mode' : 'Switch to dark mode');
        toggle.textContent = isDark ? 'Light' : 'Dark';
    }

    function initToggle() {
        var toggle = document.getElementById('theme-toggle');
        if (!toggle) {
            return;
        }

        updateToggle(root.dataset.theme || 'light');

        toggle.addEventListener('click', function() {
            var newTheme = (root.dataset.theme === 'dark') ? 'light' : 'dark';
            applyTheme(newTheme, true);
        });
    }

    var storedTheme = getStoredTheme();
    var prefersDark = false;

    if (window.matchMedia) {
        var media = window.matchMedia('(prefers-color-scheme: dark)');
        prefersDark = media.matches;

        media.addEventListener('change', function(event) {
            var stored = getStoredTheme();
            if (!stored) {
                applyTheme(event.matches ? 'dark' : 'light', false);
            }
        });
    }

    var initialTheme = storedTheme || (prefersDark ? 'dark' : 'light');
    applyTheme(initialTheme, false);

    if (document.readyState === 'loading') {
        document.addEventListener('DOMContentLoaded', initToggle);
    } else {
        initToggle();
    }
})();

