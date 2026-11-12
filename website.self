<!DOCTYPE html>
<!-- Tells the browser this is a modern HTML5 page -->
<html lang="en">
<!-- <html> wraps the whole page. lang="en" = the page is in English -->

<head>
    <!-- <head> = information ABOUT the page (not shown on screen) -->

    <meta charset="UTF-8">
    <!-- Lets the page display all letters and emojis correctly -->

    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <!-- Makes the page fit phones, tablets and computers properly -->

    <title>My Portfolio</title>
    <!-- EDIT ME: the text on the browser tab -->

    <!-- ===== FONT: Plus Jakarta Sans (loaded from Google Fonts, needs internet) ===== -->
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <!-- Warms up the connection to Google Fonts so it loads faster -->
    <link href="https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;600;700&display=swap" rel="stylesheet">
    <!-- Downloads the font in 4 thicknesses: 400 normal, 500 medium, 600 semi-bold, 700 bold -->

    <style>
        /* ======================================================
           CSS = the DESIGN of the page.
           Format:  selector { property: value; }
           ====================================================== */

        /* ---------- 1. COLOR VARIABLES (taken from your palette image) ----------
           Change a color here and it changes everywhere on the page. */
        :root {
            --sage: #a5a785;        /* EDIT ME: soft green (used for small accents) */
            --cream: #f6f3ea;       /* EDIT ME: page background */
            --blush: #ead4d2;       /* EDIT ME: light pink (cards, borders) */
            --mauve: #b99aa3;       /* EDIT ME: dusty pink (subtle text, lines) */
            --rose: #c4677f;        /* EDIT ME: main strong pink (buttons, headings) */
            --text: #4a3a40;        /* EDIT ME: dark text color */
            --white: #ffffff;       /* pure white for cards */
        }

        /* ---------- 2. RESET (removes the browser's default spacing) ---------- */
        * {
            margin: 0;              /* no outside space */
            padding: 0;             /* no inside space */
            box-sizing: border-box; /* width includes padding, so sizes are easier to predict */
        }

        /* ---------- 3. PAGE BASICS ---------- */
        html {
            scroll-behavior: smooth; /* smooth scrolling when jumping around the page */
        }

        body {
            font-family: "Plus Jakarta Sans", sans-serif; /* your font (sans-serif is the backup) */
            background-color: var(--cream);  /* page color from the variable above */
            color: var(--text);              /* default text color */
            line-height: 1.6;                /* space between lines of text */
            overflow-x: hidden;              /* stops sideways scrolling on phones */
        }

        /* ---------- 4. CARNATION DECORATIONS ---------- */
        .flower {
            position: fixed;        /* stays in place even while scrolling */
            z-index: 0;             /* sits BEHIND the content */
            opacity: 0.35;          /* see-through so text stays readable (0 = invisible, 1 = solid) */
            pointer-events: none;   /* clicks go "through" the flower, so it never blocks buttons */
        }

        .flower-1 { width: 150px; top: -40px;    right: -40px; }   /* top-right corner */
        .flower-2 { width: 110px; bottom: 60px;  left: -30px;  }   /* bottom-left corner */
        .flower-3 { width: 70px;  bottom: -15px; right: 12%;   }   /* bottom-right area */

        /* ---------- 5. HEADER + NAVIGATION ---------- */
        header {
            position: sticky;       /* stays at the top while you scroll */
            top: 0;                 /* sticks to the very top */
            z-index: 10;            /* stays ABOVE everything else */
            background-color: rgba(246, 243, 234, 0.92); /* cream, slightly see-through */
            backdrop-filter: blur(8px);                   /* blurs what's behind the header */
            border-bottom: 1px solid var(--blush);        /* thin pink line under the header */
            display: flex;                   /* puts logo and burger in a row */
            justify-content: space-between;  /* logo on the left, burger on the right */
            align-items: center;             /* centers them vertically */
            padding: 14px 20px;              /* space inside the header */
        }

        .logo {
            font-weight: 700;       /* bold */
            font-size: 20px;        /* text size */
            color: var(--rose);     /* pink */
        }

        /* ---------- BURGER BUTTON (the 3 lines) ---------- */
        .burger {
            background: none;       /* no button background */
            border: none;           /* no button border */
            cursor: pointer;        /* shows a hand when hovering */
            display: flex;          /* stacks the lines */
            flex-direction: column; /* ...vertically */
            gap: 5px;               /* space between the 3 lines */
            padding: 6px;           /* makes the button easier to tap */
        }

        .burger span {
            display: block;                  /* each line is its own block */
            width: 26px;                     /* line length */
            height: 3px;                     /* line thickness */
            background-color: var(--rose);   /* pink lines */
            border-radius: 3px;              /* rounded line ends */
            transition: 0.3s;                /* smooth animation when it changes */
        }

        /* When the menu is open, the burger turns into an X */
        .burger.open span:nth-child(1) { transform: translateY(8px) rotate(45deg); }   /* top line tilts down */
        .burger.open span:nth-child(2) { opacity: 0; }                                  /* middle line disappears */
        .burger.open span:nth-child(3) { transform: translateY(-8px) rotate(-45deg); } /* bottom line tilts up */

        /* ---------- MENU (the list of tabs) ---------- */
        nav {
            position: absolute;     /* floats under the header */
            top: 100%;              /* starts right below the header */
            left: 0;                /* from the left edge... */
            right: 0;               /* ...to the right edge (full width) */
            background-color: var(--white);   /* white dropdown */
            border-bottom: 1px solid var(--blush);
            max-height: 0;          /* menu is closed (zero height) by default */
            overflow: hidden;       /* hides the links while closed */
            transition: max-height 0.4s ease; /* smooth slide open/close */
        }

        nav.open {
            max-height: 400px;      /* menu is open: gives it room to show */
        }

        nav button {
            display: block;         /* each tab on its own line */
            width: 100%;            /* full width */
            background: none;       /* no background */
            border: none;           /* no border */
            font-family: inherit;   /* use the same Plus Jakarta Sans font */
            font-size: 16px;        /* text size */
            font-weight: 500;       /* medium thickness */
            color: var(--text);     /* normal text color */
            padding: 16px 20px;     /* space inside each tab button */
            text-align: left;       /* text on the left */
            cursor: pointer;        /* hand on hover */
            transition: 0.3s;       /* smooth color change */
        }

        nav button:hover {
            background-color: var(--blush);  /* light pink when the mouse is over it */
        }

        nav button.active {
            color: var(--rose);              /* the current tab is pink... */
            font-weight: 700;                /* ...and bold */
            border-left: 4px solid var(--rose); /* with a pink bar on the left */
        }

        /* ---------- 6. PAGE CONTAINER ---------- */
        main {
            position: relative;     /* needed so z-index works */
            z-index: 1;             /* sits ABOVE the flowers */
            max-width: 900px;       /* never wider than 900px (keeps text readable on big screens) */
            margin: 0 auto;         /* centers the container */
            padding: 30px 20px 60px; /* space inside: top, sides, bottom */
        }

        /* ---------- 7. HERO (photo + name at the top) ---------- */
        .hero {
            text-align: center;     /* center everything */
            margin-bottom: 35px;    /* space below */
        }

        .hero img {
            width: 140px;           /* photo width */
            height: 140px;          /* photo height (same = square → circle) */
            border-radius: 50%;     /* makes it a circle */
            object-fit: cover;      /* crops the photo nicely without stretching */
            border: 5px solid var(--white);   /* white ring */
            box-shadow: 0 6px 20px rgba(196, 103, 127, 0.3); /* soft pink shadow */
            background-color: var(--blush);   /* shown if the photo can't load */
        }

        .hero h1 {
            font-size: 28px;        /* name size */
            margin-top: 15px;       /* space above the name */
            color: var(--rose);     /* pink name */
        }

        .hero p {
            color: var(--mauve);    /* soft dusty pink */
            max-width: 480px;       /* keeps the intro from getting too wide */
            margin: 8px auto 0;     /* centers it, 8px space on top */
        }

        /* ---------- 8. TABS (the 5 content sections) ---------- */
        .tab {
            display: none;          /* all tabs are HIDDEN by default */
        }

        .tab.active {
            display: block;                 /* only the active tab is shown */
            animation: fadeIn 0.6s ease;    /* plays the fade animation below */
        }

        /* The fade animation: starts see-through and slightly lower, ends solid */
        @keyframes fadeIn {
            from { opacity: 0; transform: translateY(15px); }  /* start */
            to   { opacity: 1; transform: translateY(0); }     /* end */
        }

        .tab h2 {
            font-size: 24px;        /* section title size */
            color: var(--rose);     /* pink title */
            margin-bottom: 6px;     /* space below */
        }

        .tab .intro {
            color: var(--mauve);    /* soft pink subtitle */
            margin-bottom: 22px;    /* space below */
        }

        /* ---------- 9. CARDS (small white boxes) ---------- */
        .grid {
            display: grid;                      /* grid = rows and columns layout */
            grid-template-columns: 1fr;         /* phones: 1 column */
            gap: 16px;                          /* space between cards */
        }

        .card {
            background-color: var(--white);     /* white box */
            border: 1px solid var(--blush);     /* thin pink border */
            border-radius: 18px;                /* rounded corners */
            padding: 22px;                      /* space inside */
            transition: 0.3s;                   /* smooth hover effect */
        }

        .card:hover {
            transform: translateY(-4px);                       /* lifts up a little */
            box-shadow: 0 10px 25px rgba(196, 103, 127, 0.18); /* soft pink shadow */
        }

        .card .icon {
            font-size: 30px;        /* emoji size */
            margin-bottom: 8px;     /* space below the emoji */
        }

        .card h3 {
            font-size: 17px;        /* card title size */
            margin-bottom: 4px;     /* space below */
        }

        .card p {
            font-size: 14.5px;      /* card text size */
        }

        /* Photo used inside the Achievements tab */
        .photo {
            width: 100%;            /* fills the width */
            max-height: 360px;      /* not too tall */
            object-fit: cover;      /* crops neatly */
            border-radius: 18px;    /* rounded corners */
            margin-top: 18px;       /* space above */
            background-color: var(--blush); /* shown if photo is missing */
        }

        /* ---------- 10. TIMELINE (used by Journey & Experience) ---------- */
        .timeline {
            border-left: 3px solid var(--blush);  /* vertical pink line on the left */
            padding-left: 22px;                   /* space between line and text */
        }

        .event {
            position: relative;     /* lets us place the dot relative to this box */
            margin-bottom: 26px;    /* space between events */
        }

        .event::before {
            content: "";            /* makes an empty decoration (the dot) */
            position: absolute;     /* places it exactly where we want */
            left: -31px;            /* moves it onto the vertical line */
            top: 6px;               /* moves it down a little */
            width: 14px;            /* dot width */
            height: 14px;           /* dot height */
            background-color: var(--rose);       /* pink dot */
            border: 3px solid var(--cream);      /* ring that matches the page */
            border-radius: 50%;                  /* makes it round */
        }

        .event .date {
            font-size: 13px;        /* small text */
            font-weight: 700;       /* bold */
            color: var(--rose);     /* pink */
        }

        .event h3 {
            font-size: 17px;        /* event title size */
        }

        .event p {
            font-size: 14.5px;      /* event text size */
        }

        /* ---------- 11. FOOTER ---------- */
        footer {
            position: relative;     /* so z-index works */
            z-index: 1;             /* above the flowers */
            text-align: center;     /* centered */
            color: var(--mauve);    /* soft pink text */
            font-size: 13px;        /* small text */
            padding-bottom: 30px;   /* space at the bottom */
        }

        /* ======================================================
           12. BIGGER SCREENS (tablets and computers)
           Everything above is for PHONES. The rules inside the
           braces below only apply when the screen is 768px wide
           or more. This is called "mobile-first" design.
           ====================================================== */
        @media (min-width: 768px) {

            .burger { display: none; }   /* hide the burger on big screens */

            nav {
                position: static;        /* menu is now part of the header, not floating */
                max-height: none;        /* always open */
                overflow: visible;       /* show everything */
                background: none;        /* no white box */
                border: none;            /* no border */
                display: flex;           /* tabs side by side */
                gap: 4px;                /* space between tabs */
            }

            nav button {
                width: auto;             /* each button fits its text */
                padding: 8px 16px;       /* smaller padding */
                border-radius: 20px;     /* pill shape */
                border-left: none !important; /* remove the left bar used on phones */
            }

            nav button.active {
                background-color: var(--rose);  /* active tab gets a pink pill... */
                color: var(--white);            /* ...with white text */
            }

            .grid {
                grid-template-columns: repeat(2, 1fr); /* 2 columns of cards */
            }

            .hero h1 { font-size: 36px; }          /* bigger name */
            .flower-1 { width: 240px; }            /* bigger flowers */
            .flower-2 { width: 170px; }
            .flower-3 { width: 100px; }
        }

        @media (min-width: 1100px) {
            .grid {
                grid-template-columns: repeat(3, 1fr); /* 3 columns on large screens */
            }
        }
    </style>
</head>

<body>
    <!-- <body> = everything you SEE on the page -->

    <!-- ===== CARNATION DRAWING =====
         This is drawn ONCE here, then reused 3 times below with <use>.
         width="0" height="0" hides this original copy. -->
    <svg width="0" height="0" style="position:absolute">
        <defs>
            <!-- <defs> = a place to store shapes without showing them yet -->

            <!-- One petal shape (an oval) -->
            <ellipse id="petal" cx="50" cy="24" rx="13" ry="20"/>
            <!-- cx/cy = center position, rx/ry = width/height of the oval -->

            <!-- The whole flower, named "carnation" -->
            <symbol id="carnation" viewBox="0 0 100 100">
                <!-- viewBox = the drawing area is 100 x 100 units -->

                <!-- OUTER layer of petals: light pink, 8 petals turned around the center (50,50) -->
                <g fill="#ecc3cd">
                    <use href="#petal" transform="rotate(0 50 50)"/>
                    <use href="#petal" transform="rotate(45 50 50)"/>
                    <use href="#petal" transform="rotate(90 50 50)"/>
                    <use href="#petal" transform="rotate(135 50 50)"/>
                    <use href="#petal" transform="rotate(180 50 50)"/>
                    <use href="#petal" transform="rotate(225 50 50)"/>
                    <use href="#petal" transform="rotate(270 50 50)"/>
                    <use href="#petal" transform="rotate(315 50 50)"/>
                </g>

                <!-- MIDDLE layer: medium pink, smaller petals, shifted to fill the gaps -->
                <g fill="#dc94a7" transform="translate(50 50) scale(0.75) translate(-50 -50)">
                    <use href="#petal" transform="rotate(22 50 50)"/>
                    <use href="#petal" transform="rotate(67 50 50)"/>
                    <use href="#petal" transform="rotate(112 50 50)"/>
                    <use href="#petal" transform="rotate(157 50 50)"/>
                    <use href="#petal" transform="rotate(202 50 50)"/>
                    <use href="#petal" transform="rotate(247 50 50)"/>
                    <use href="#petal" transform="rotate(292 50 50)"/>
                    <use href="#petal" transform="rotate(337 50 50)"/>
                </g>

                <!-- INNER layer: deep pink, smallest petals -->
                <g fill="#c4677f" transform="translate(50 50) scale(0.5) translate(-50 -50)">
                    <use href="#petal" transform="rotate(0 50 50)"/>
                    <use href="#petal" transform="rotate(60 50 50)"/>
                    <use href="#petal" transform="rotate(120 50 50)"/>
                    <use href="#petal" transform="rotate(180 50 50)"/>
                    <use href="#petal" transform="rotate(240 50 50)"/>
                    <use href="#petal" transform="rotate(300 50 50)"/>
                </g>

                <!-- CENTER of the flower -->
                <circle cx="50" cy="50" r="6" fill="#a84e66"/>
            </symbol>
        </defs>
    </svg>

    <!-- The 3 flowers placed on the page. Their position/size is set in the CSS (.flower-1, .flower-2, .flower-3) -->
    <svg class="flower flower-1" viewBox="0 0 100 100"><use href="#carnation"/></svg>
    <svg class="flower flower-2" viewBox="0 0 100 100"><use href="#carnation"/></svg>
    <svg class="flower flower-3" viewBox="0 0 100 100"><use href="#carnation"/></svg>

    <!-- ===== HEADER with logo, burger button and menu ===== -->
    <header>
        <div class="logo">🌸 My Portfolio</div>
        <!-- EDIT ME: your name or site title -->

        <button class="burger" id="burger" aria-label="Open menu">
            <!-- The burger button. id="burger" lets the JavaScript find it -->
            <span></span>  <!-- line 1 -->
            <span></span>  <!-- line 2 -->
            <span></span>  <!-- line 3 -->
        </button>

        <nav id="menu">
            <!-- The menu. data-tab="..." must match the id of a section below -->
            <button class="active" data-tab="hobbies">Hobbies</button>
            <button data-tab="talents">Talents</button>
            <button data-tab="achievements">Achievements</button>
            <button data-tab="journey">Journey</button>
            <button data-tab="experience">Experience</button>
        </nav>
    </header>

    <!-- ===== MAIN CONTENT ===== -->
    <main>

        <!-- HERO: your photo, name and short intro (always visible) -->
        <section class="hero">
            <img src="me.jpg" alt="My profile photo">
            <!-- EDIT ME: save your photo in the SAME folder as this file and name it me.jpg -->

            <h1>Samantha Nicole U. Lontok</h1>
            <!-- EDIT ME: your full name -->

            <p>Hi! I'm a student who loves creating, learning and trying new things. Welcome to my little corner of the web.</p>
            <!-- EDIT ME: a short inatroduction about yourself -->
        </section>

        <!-- ---------- TAB 1: HOBBIES ---------- -->
        <section class="tab active" id="hobbies">
            <!-- class="tab active" = this one shows first. id="hobbies" matches data-tab="hobbies" -->
            <h2>Hobbies</h2>
            <p class="intro">Things I enjoy doing in my free time.</p>

            <div class="grid">
                <!-- Each .card is one hobby. Copy a whole <div class="card">...</div> to add another -->
                <div class="card">
                    <div class="icon">🎵</div>        <!-- EDIT ME: emoji -->
                    <h3>Music</h3>                    <!-- EDIT ME: hobby name -->
                    <p>Listening to playlists that match every mood.</p> <!-- EDIT ME: description -->
                </div>
                <div class="card">
                    <div class="icon">📸</div>
                    <h3>Photography</h3>
                    <p>Capturing small moments with friends.</p>
                </div>
                <div class="card">
                    <div class="icon">📚</div>
                    <h3>Reading</h3>
                    <p>Getting lost in a good story.</p>
                </div>
                <div class="card">
                    <div class="icon">𓂃🪶</div>
                    <h3>Writing</h3>
                    <p>Creating stories out of my imagination.</p>
            </div>
        </section>

        <!-- ---------- TAB 2: TALENTS ---------- -->
        <section class="tab" id="talents">
            <h2>Talents</h2>
            <p class="intro">What I'm good at.</p>

            <div class="grid">
                <div class="card">
                    <div class="icon">💃</div>
                    <h3>Dancing</h3>
                    <p>Performing on stage with confidence.</p>
                </div>
                <div class="card">
                    <div class="icon">🎤</div>
                    <h3>Singing</h3>
                    <p>Singing solo or with a group.</p>
                </div>
                <div class="card">
                    <div class="icon">💻</div>
                    <h3>Coding</h3>
                    <p>Learning to build my own websites.</p>
                </div>
            </div>
        </section>

        <!-- ---------- TAB 3: ACHIEVEMENTS ---------- -->
        <section class="tab" id="achievements">
            <h2>Achievements</h2>
            <p class="intro">Awards and moments I'm proud of.</p>

            <div class="grid">
                <div class="card">
                    <div class="icon">🏆</div>
                    <h3>Championship Award</h3>          <!-- EDIT ME: award name -->
                    <p>Won with my team at a school competition.</p>
                </div>
                <div class="card">
                    <div class="icon">🎓</div>
                    <h3>Honor Student (Junior Student)</h3>
                    <p>Recognized for good grades.</p>
                </div>
                <div class="card">
                    <div class="icon">🎓</div>
                    <h3>High Honor Student (Senior Student)</h3>
                    <p>Recognized for good grades.</p>
                </div>
                <div class="card">
                    <div class="icon">🎓</div>
                    <h3>Best in Work Immersion</h3>
                    <p>Recognized for hardwork and dedication in Work Immersion.</p>
            </div>

            <img class="photo" src="group.jpg" alt="My team celebrating with a trophy">
            <!-- EDIT ME: save your team photo as group.jpg in the same folder -->
        </section>

        <!-- ---------- TAB 4: JOURNEY ---------- -->
        <section class="tab" id="journey">
            <h2>Journey</h2>
            <p class="intro">How I got to where I am today.</p>

            <div class="timeline">
                <!-- Each .event is one point on the line. Copy one to add more -->
                <div class="event">
                    <div class="date">2010</div>                 <!-- EDIT ME: year -->
                    <h3>Where it all began</h3>                  <!-- EDIT ME: title -->
                    <p>Write about where you were born or grew up.</p> <!-- EDIT ME: details -->
                </div>
                <div class="event">
                    <div class="date">2020</div>
                    <h3>Started high school</h3>
                    <p>Made new friends and found new interests.</p>
                </div>
                <div class="event">
                    <div class="date">2026</div>
                    <h3>Now</h3>
                    <p>Building my first portfolio website!</p>
                </div>
            </div>
        </section>

        <!-- ---------- TAB 5: EXPERIENCE ---------- -->
        <section class="tab" id="experience">
            <h2>Experience</h2>
            <p class="intro">Roles, projects and activities I've been part of.</p>

            <div class="timeline">
                <div class="event">
                    <div class="date">2025 - Present</div>
                    <h3>Student Organization Member</h3>   <!-- EDIT ME: role -->
                    <p>Helped plan events and activities.</p>
                </div>
                <div class="event">
                    <div class="date">2024</div>
                    <h3>School Performance</h3>
                    <p>Performed on stage with my classmates.</p>
                </div>
                <div class="event">
                    <div class="date">2023</div>
                    <h3>Group Project Leader</h3>
                    <p>Guided my team to finish on time.</p>
                </div>
            </div>
        </section>
    </main>

    <footer>
        Made with 🌸 by Sammy
        <!-- EDIT ME: your name -->
    </footer>

    <!-- ======================================================
         JAVASCRIPT = makes the page DO things (clicks, switching tabs)
         ====================================================== -->
    <script>
        // Find the elements on the page and store them in variables
        const burger = document.getElementById("burger");          // the burger button
        const menu = document.getElementById("menu");              // the menu
        const buttons = document.querySelectorAll("nav button");   // all 5 tab buttons
        const tabs = document.querySelectorAll(".tab");            // all 5 content sections

        // When the burger is clicked...
        burger.addEventListener("click", function () {
            menu.classList.toggle("open");     // add "open" if missing, remove it if there
            burger.classList.toggle("open");   // same for the burger (turns it into an X)
        });

        // Go through each tab button, one by one
        buttons.forEach(function (button) {

            // When THIS button is clicked...
            button.addEventListener("click", function () {

                // 1) Remove "active" from ALL buttons and ALL tabs
                buttons.forEach(function (b) { b.classList.remove("active"); });
                tabs.forEach(function (t) { t.classList.remove("active"); });

                // 2) Add "active" to the clicked button
                button.classList.add("active");

                // 3) Find the tab whose id matches the button's data-tab, and show it
                const target = document.getElementById(button.dataset.tab);
                target.classList.add("active");

                // 4) Close the burger menu (useful on phones)
                menu.classList.remove("open");
                burger.classList.remove("open");

                // 5) Scroll back to the top smoothly
                window.scrollTo({ top: 0, behavior: "smooth" });
            });
        });
    </script>
</body>
</html>
