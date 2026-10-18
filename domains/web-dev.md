# Web and software development

[Back to the index](../README.md)

## In short

Web development knowledge splits into things that last (HTTP, SQL, architecture, browser support) and things that rotate every few years (frameworks and component libraries). This page keeps both, grouped by section.

- **References that pay off for decades:** DevDocs (offline docs for everything), Can I use, HTTP status codes, Compiler Explorer, and Martin Fowler's architecture guide.
- **Do not build from zero.** Starter Index lists thousands of boilerplates; the FastAPI full-stack template and HTML5 Boilerplate are solid defaults. Supabase gives you Postgres, auth and storage in one go.
- **UI:** in React, pick one component library (MUI, Mantine, Ant Design, Chakra) and one primitive layer (Radix) and stay with them. Tailwind component kits (FlyonUI) fit when you prefer utility classes.
- **APIs:** public-apis and Postman's collection for real data, JSONPlaceholder and ReqRes for fake data while prototyping, jwt.io when auth breaks.
- **Data:** SQL basics never expire; ClickHouse for analytics, PostgreSQL for almost everything else.
- **Write for agents too:** llms.txt is a small proposed standard that gives AI agents a summary of your site, worth adding to docs.
- The Java, Scala, PHP and Android sections are older but still useful as reference; several Polish-language tutorials are included.

**Where to start:** roadmap.sh to see the map, DevDocs and Can I use as daily tools, Free for Developers before paying for any service.

## Contents

- [Learning and references](#learning-and-references)
- [Java and Scala](#java-and-scala)
- [UI and CSS](#ui-and-css)
- [Backend and APIs](#backend-and-apis)
- [Databases and SQL](#databases-and-sql)
- [JavaScript and frontend](#javascript-and-frontend)
- [Charts and visualization](#charts-and-visualization)
- [Boilerplates and starters](#boilerplates-and-starters)
- [Mobile and Android](#mobile-and-android)
- [PHP](#php)
- [CMS and e-commerce](#cms-and-e-commerce)
- [Python](#python)

## Learning and references

- [Can I use](http://caniuse.com/) ⭐ - Browser support tables for HTML5, CSS3 and other web technologies.
- [Compiler Explorer](https://godbolt.org/) ⭐ - Interactive online compiler showing assembly output for many languages.
- [DevDocs](https://devdocs.io/) ⭐ - Fast, offline documentation browser covering over 100 developer doc sets.
- [Free for Developers](https://free-for.dev/) ⭐ - Curated list of free tiers and free services for developers and open-source authors.
- [freeCodeCamp](https://www.freecodecamp.org/) ⭐ - Free open-source curriculum and coding courses for web development and more.
- [Software Architecture Guide](https://martinfowler.com/architecture) ⭐ - Martin Fowler guide collecting articles and resources on software architecture.
- [Algorytmy i Struktury Danych](http://www.algorytm.org/) - Polish site explaining algorithms and data structures with code examples in several languages.
- [awesome-cheatsheets](https://github.com/LeCoupa/awesome-cheatsheets) - Cheat sheets for popular programming languages, frameworks and development tools.
- [Codecademy Docs](https://www.codecademy.com/resources/docs) - Community reference docs for popular programming languages and frameworks.
- [Conventional Commits](https://www.conventionalcommits.org/en/v1.0.0) - Specification for structured commit messages readable by humans and machines.
- [DEV Community](https://dev.to/) - Community platform where developers publish articles and discuss software topics.
- [developer-roadmap](https://github.com/kamranahmedse/developer-roadmap) - Interactive roadmaps and guides to help developers plan their career growth.
- [GeeksforGeeks](https://www.geeksforgeeks.org/) - Large library of computer science and programming tutorials and interview questions.
- [GoalKicker free programming books](https://goalkicker.com/) - Free programming ebooks covering many languages and platforms.
- [GoalKicker.com](https://books.goalkicker.com/) - Free programming ebooks covering many languages and frameworks.
- [HTTP response status codes (Wikipedia PL)](https://pl.wikipedia.org/wiki/Kod_odpowiedzi_HTTP) - Polish Wikipedia article listing HTTP response status codes and their meanings.
- [llms.txt](https://llmstxt.org/) - Proposed standard for an /llms.txt file that gives AI agents a concise guide to a website.
- [nvm-windows](https://github.com/coreybutler/nvm-windows) - Node.js version manager for Windows.
- [roadmap.sh](https://roadmap.sh/) - Community-driven developer roadmaps, guides and articles for career growth.
- [the-book-of-secret-knowledge](https://github.com/trimstray/the-book-of-secret-knowledge) - Large curated collection of manuals, cheatsheets, one-liners and CLI and web tools.
- [ThoughtWorks Technology Radar](https://www.thoughtworks.com/radar) - Periodic opinionated overview of tools, techniques and platforms by ThoughtWorks.
- [W3Schools](http://www.w3schools.com/) - Web tutorials and references for HTML, CSS, JavaScript, Python, SQL and more.
- [4programmers FAQ: Polish characters](http://4programmers.net/C/FAQ/Rozpoznawanie_standardu_polskich_znak%C3%B3w) - Polish-language FAQ on recognising Polish character encodings, from 4programmers.net.
- [4programmers.net](http://4programmers.net/) - Polish programming forum covering many languages and technologies.
- [Envato Tuts+](http://active.tutsplus.com/) - Tutorials and courses on web and software development.
- [forumweb.pl](http://www.forumweb.pl/) - Polish webmaster forum covering HTML, JavaScript, PHP, Python, databases and SEO.
- [Funkcje.net](http://funkcje.net/) - Polish-language collection of PHP, JavaScript, HTML and CSS functions and tutorials.
- [HTML Cheat Sheet - JavaScript](http://htmlcheatsheet.com/js) - Single-page JavaScript cheat sheet with code examples.
- [html5demos](https://github.com/remy/html5demos) - Collection of HTML5 demos showing what browser apps can do.
- [HTTP 406 explained](http://www.checkupdown.com/status/E406.html) - Explanation of the HTTP 406 Not Acceptable status code.
- [Legacy Modernization meets GenAI](https://martinfowler.com/articles/legacy-modernization-gen-ai.html) - Martin Fowler article on using generative AI to modernize legacy systems.
- [LibHunt](https://www.libhunt.com/) - Ranking site for trending open-source libraries and their alternatives.
- [py4kids](https://github.com/wgong/py4kids/tree/master) - Python learning resources for kids.
- [Rabin-Karp algorithm (Wikipedia)](http://pl.wikipedia.org/wiki/Algorytm_Karpa-Rabina) - Polish Wikipedia article on the Rabin-Karp string search algorithm.
- [RegExLib](http://regexlib.com/) - Searchable online database of regular expressions with ratings and an online tester.
- [SSW.Rules](https://www.ssw.com.au/rules) - Collection of software development best-practice rules for .NET, Azure, Angular and React.
- [web-tooling-benchmark](https://github.com/v8/web-tooling-benchmark) - JavaScript benchmark suite of common web developer tooling workloads, from the V8 team.
- [webowe.pl](http://www.webowe.pl/) - Polish portal on internet technologies and web development.
- [WebSiteOptimization.com](http://www.websiteoptimization.com/) - Web performance and site optimization resource.

## Java and Scala

- [Apache Commons](http://commons.apache.org/) - Apache project of reusable Java components such as collections and I/O helpers.
- [Scala standard library API](http://www.scala-lang.org/api/current/index.html) - Official Scala standard library API documentation.
- [Akka documentation](http://doc.akka.io/) - Official Akka documentation index.
- [Apache HttpComponents](http://hc.apache.org/) - Java libraries for HTTP client and server development.
- [Apache Jackrabbit](http://jackrabbit.apache.org/) - Apache Java content repository implementing JCR for structured content.
- [Developer on the go](https://developeronthego.pl/) - Polish tech blog on Java, backend and practical programming tools.
- [Java HR interview cheatsheet](https://sjezierski.pl/informatyka/java-sciaga-na-rozmowe-rekrutacyjna) - Polish guide to Java interview topics, linking to articles on each subject.
- [java2s](http://www.java2s.com/) - Large collection of Java code examples and tutorials.
- [JavaStart](http://javastart.pl/) - Polish online Java course platform with lessons from beginner to advanced.
- [JavaStart Spring course](https://javastart.pl/kurs/spring) - Polish Spring Framework course with practical exercises for building web applications.
- [Kodejava](http://www.kodejava.org/) - Java tutorials and code examples for learning Java programming.
- [Launch4j](http://sourceforge.net/projects/launch4j) - Tool that wraps Java applications into Windows executables.
- [Lift](http://liftweb.net/getting_started) - Scala web framework, getting started page.
- [OpenGamma Strata](https://github.com/OpenGamma/Strata) - Open-source Java library for analytics and market risk calculations.
- [Roseindia](http://roseindia.net/) - Java tutorials and examples for beginners and developers.
- [ScalaTest](http://www.scalatest.org/) - Testing toolkit for Scala and Java.
- [Scalaz](https://github.com/scalaz/scalaz) - Functional programming library for Scala with type classes and data structures.
- [ZK](http://www.zkoss.org/zkdemo/userguide) - Java framework for building rich web user interfaces.

## UI and CSS

- [Bootstrap](https://getbootstrap.com/) ⭐ - Popular HTML, CSS and JavaScript front-end toolkit with Sass and components.
- [Ant Design](https://ant.design/) - React UI component library with enterprise-grade components and a design language.
- [Chakra UI](https://github.com/chakra-ui/chakra-ui) - Accessible React component library for building SaaS interfaces.
- [CSS-Tricks](http://css-tricks.com/) - Front-end learning site with articles and guides on HTML, CSS and JavaScript.
- [FlyonUI](https://flyonui.com/) - Free, open-source Tailwind CSS component library with semantic class names.
- [Mantine](https://mantine.dev/) - React component library with over 120 customizable components, hooks and utilities.
- [MUI](https://mui.com/) - React component library implementing Material Design, customizable and accessible.
- [Radix UI](https://www.radix-ui.com/) - Open-source, accessible UI primitives, icons and colors for building web interfaces.
- [React Bits](https://www.reactbits.dev/) - Free open-source animated React components with live demos and copyable source.
- [CSS Animated Backgrounds](https://wpdean.com/css-animated-background) - Collection of 47 CSS animated background examples for web designers.
- [Free Frontend: Bootstrap examples](https://freefrontend.com/bootstrap-code-examples) - Collection of Bootstrap code snippets and examples.
- [Free Frontend: CSS animated backgrounds](https://freefrontend.com/css-animated-backgrounds) - Gallery of CSS animated background snippets for landing pages and hero sections.
- [FreeCSSTemplates (now FCT.co)](http://www.freecsstemplates.org/) - Free HTML and CSS website templates, now operating under the FCT.co name.
- [jqGrid](http://www.trirand.com/blog) - jQuery grid plugin for displaying and editing tabular data.
- [Meyer's CSS Reset](http://meyerweb.com/eric/tools/css/reset) - Eric Meyer's classic CSS reset stylesheet.
- [React Draft Wysiwyg](https://jpuri.github.io/react-draft-wysiwyg) - React rich text editor component built on Draft.js.

## Backend and APIs

- [public-apis](https://github.com/public-apis/public-apis) ⭐ - Community-maintained list of free public APIs, grouped by category.
- [supabase](https://github.com/supabase/supabase) ⭐ - Open-source Firebase alternative built on Postgres, with auth, storage and realtime APIs.
- [High Scalability](http://highscalability.com/) - Blog on building large, fast and reliable websites.
- [JSONPlaceholder](https://jsonplaceholder.typicode.com/) - Free fake REST API with six resources for testing and prototyping, no signup.
- [jwt.io](http://jwt.io/) - Debugger and reference for JSON Web Tokens.
- [Postman Public REST APIs](https://www.postman.com/cs-demo/public-rest-apis/overview) - Collection of public REST APIs to test and learn from in Postman.
- [api-analytics](https://github.com/tom-draper/api-analytics) - Lightweight monitoring and analytics for API frameworks.
- [HTML/CSS to Image API](https://htmlcsstoimage.com/) - API service that renders HTML and CSS to images or website screenshots.
- [Kobiety do kodu - Web Services (REST)](https://kobietydokodu.pl/22-web-services) - Polish course lesson on web services and REST.
- [Merge](https://www.merge.dev/) - Unified API for HR, accounting, CRM and ATS integrations, positioned as context for AI agents.
- [Nango](https://github.com/NangoHQ/nango) - Unified API platform for connecting products and agents to many third-party APIs.
- [Parse Platform](https://parseplatform.org/) - Open-source backend platform for apps, an open alternative to Parse services.
- [RapidAPI](https://rapidapi.com/) - Marketplace for discovering and managing many APIs.
- [Reactive microservices REST API (Just Geek)](https://geek.justjoin.it/rest-api-reaktywnymi-mikrouslugami) - Polish article introducing reactive microservices as a basis for REST APIs.
- [ReqRes](https://reqres.in/) - Hosted REST API with realistic responses for testing front-end code, no signup.

## Databases and SQL

- [ClickHouse](https://clickhouse.com/) - Open-source column-oriented SQL database for real-time analytical reports.
- [MongoDB](http://cookbook.mongodb.org/) - Official MongoDB site for the document database and data platform.
- [TechOnTheNet](https://www.techonthenet.com/index.php) - Online tutorials for SQL, PL/SQL, Excel and related technologies, with syntax examples.
- [Bazy danych (wykłady.org)](http://bazy-danych.wyklady.org/) - Polish-language lecture and exercise materials on database management systems.
- [depesz](http://www.depesz.com/various/various-sqltrees.php) - Personal site of a PostgreSQL expert with SQL articles and tools.
- [FlyNerd SQL in 60 minutes](https://www.flynerd.pl/2018/05/naucz-sie-sql-w-60min-kurs-podstawy.html) - Polish one-hour SQL basics course with step-by-step exercises.
- [NoSQL Databases overview](http://nosql-database.org/) - Overview of NoSQL database types and how they differ from SQL.
- [PostgreSQL tutorial (Tutorialspoint)](https://www.tutorialspoint.com/postgresql/index.htm) - Introductory PostgreSQL tutorial with syntax and examples.
- [Relational databases intro (Samouczek Programisty)](https://www.samouczekprogramisty.pl/wstep-do-relacyjnych-baz-danych) - Polish introduction to relational databases: tuples, relations and attributes.
- [SQL basics (trener-it.pl)](http://trener-it.pl/strona/artykuly/46) - Polish introduction to SQL basics published on a personal IT trainer's website.
- [SQLpedia SQL course](https://www.sqlpedia.pl/kurs-sql) - Free beginner SQL course focused on SQL Server.

## JavaScript and frontend

- [Anime.js](https://animejs.com/) - Lightweight JavaScript animation library.
- [awesome-react](https://github.com/enaqx/awesome-react) - Curated list of React ecosystem libraries, tools and resources.
- [esm.sh](https://esm.sh/) - CDN that serves npm packages as ES modules for modern browsers.
- [lottie-web](https://github.com/airbnb/lottie-web) - Renders After Effects animations natively on the web, Android, iOS and React Native.
- [Prism](https://prismjs.com/) - Lightweight JavaScript syntax highlighter for code in web pages.
- [React docs (Polish)](https://pl.reactjs.org/docs/getting-started.html) - Polish translation of the React getting started documentation.
- [litegraph.js](https://github.com/jagenjo/litegraph.js) - JavaScript graph node engine and editor that runs in the browser on Canvas2D.
- [Locutus](http://phpjs.org/) - Standard library functions from many languages, implemented in TypeScript.
- [Modernizr](http://www.modernizr.com/) - Feature detection library for HTML5 and CSS3 browser support.
- [Neutralinojs](https://neutralino.js.org/) - Framework for lightweight cross-platform desktop apps built with JavaScript, HTML and CSS.
- [Preact guide](https://preactjs.com/guide/v10/getting-started) - Getting-started guide for Preact, a lightweight React-compatible library.

## Charts and visualization

- [Highcharts](http://www.highcharts.com/) - JavaScript charting library for interactive charts, including Stock, Maps and Gantt.
- [Mermaid](https://mermaid.js.org/) - Text-based diagramming and charting tool for creating diagrams from code.
- [Mike Bostock blog](http://bost.ocks.org/mike) - Personal blog of Mike Bostock, creator of D3.js, on data visualization.
- [Alternatives to typical technical illustrations (Smashing)](https://www.smashingmagazine.com/2024/11/alternatives-typical-technical-illustrations-data-visualisations) - Article on uncommon ways to present data and technical illustrations.
- [AndroidPlot](http://androidplot.com/wiki/Home) - Charting library for Android apps.
- [Highcharts demos](http://www.highcharts.com/demo) - Gallery of Highcharts examples for core, Stock, Maps and Gantt.
- [JFree](http://jfree.org/) - Home of JFree, maker of the JFreeChart Java charting library.
- [react-financial-charts](https://github.com/react-financial/react-financial-charts) - React charts library for financial data.
- [RGraph](http://www.rgraph.net/) - JavaScript charting library with many chart styles for web apps.
- [Visualizing Algorithms](http://bost.ocks.org/mike/algorithms) - Essay by Mike Bostock on visualizing algorithms with interactive graphics.

## Boilerplates and starters

- [full-stack-fastapi-template](https://github.com/fastapi/full-stack-fastapi-template) - Full-stack template with FastAPI, React, PostgreSQL and Docker Compose.
- [HTML5 Boilerplate](http://html5boilerplate.com/) - Front-end starter template with sensible defaults for HTML, CSS and JS.
- [Starter Index](https://starterindex.com/) - Directory of over 3,000 boilerplates and starter kits for building projects.
- [10x-astro-starter](https://github.com/przeprogramowani/10x-astro-starter) - Starter project for Astro, TypeScript and React from the Polish Przeprogramowani community.
- [BoilerplateList](https://boilerplatelist.com/) - Directory of boilerplates and starter kits for SaaS, mobile and browser extensions.
- [create-chrome-ext](https://github.com/guocaoyi/create-chrome-ext) - Scaffolding CLI for Chrome extensions with boilerplates for many UI frameworks.
- [micron](https://github.com/adamsky/saasbase) - Starter template for building web apps quickly, formerly published as saasbase.
- [SaaS Themes](https://saasthemes.com/) - Curated collection of boilerplates for building SaaS projects.
- [ShipFast](https://shipfa.st/) - Next.js starter kit with the basics needed to launch a product.

## Mobile and Android

- [Android Developers](http://developer.android.com/index.html) ⭐ - Official Google documentation, tools and training for Android developers.
- [Apache Cordova](http://incubator.apache.org/cordova) - Framework for building cross-platform mobile apps with HTML, CSS and JavaScript.
- [vogella Android tutorial](http://www.vogella.de/articles/Android/article.html) - Well-known tutorial series on Android development and Java.
- [AndDev](http://www.anddev.org/) - Android and Kotlin development tutorials with tested examples.
- [Android-er](http://android-er.blogspot.com/) - Android developer blog with tutorials on programming for Android.
- [Android-Forum.pl](http://android-forum.pl/) - Polish forum about Android phones, apps and tutorials.
- [Exploring Android](http://lampwww.epfl.ch/~michelou/android) - Personal academic notes on Android internals and development.
- [Qualcomm Developer Network](https://developer.qualcomm.com/develop/mobile-platforms/android) - Qualcomm developer resources for Android on Snapdragon platforms.

## PHP

- [FPDI](http://www.setasign.de/products/pdf-php-solutions/fpdi) - Free PHP class for importing pages from existing PDF files as templates in FPDF, TCPDF and mPDF.
- [SimplePie](http://simplepie.org/) - Feed parsing library for RSS and Atom written in PHP.
- [Elgg](http://elgg.org/) - Open source PHP framework and CMS for building social networking applications.
- [phpGrid](http://phpgrid.com/) - Commercial PHP datagrid component for editable, searchable tables.
- [phpQuery](https://code.google.com/p/phpquery) - jQuery-style DOM manipulation library for PHP; archived copy of the original Google Code project.
- [WinBinder](http://winbinder.org/) - Library for building native Windows GUI applications from PHP.

## CMS and e-commerce

- [WordPress Plugins directory](http://wordpress.org/extend/plugins) - Official directory of free WordPress plugins.
- [Blocksy](https://pl.wordpress.org/themes/blocksy) - WordPress theme with WooCommerce support and a customizable design system.
- [PrestaShop Addons](http://addons.prestashop.com/pl) - Official PrestaShop marketplace for modules and themes for online shops.
- [ThemeForest](https://themeforest.net/) - Marketplace for premium WordPress themes and website templates.
- [TinaCMS](https://tina.io/) - Git-based headless CMS with visual editing for React sites.

## Python

- [Real Python](https://realpython.com/) - Python tutorial site with articles and courses for all skill levels.
- [Streamlit](https://streamlit.io/) - Open-source Python framework for building interactive data apps quickly.
- [PyMasters](https://pymasters.pl/) - Polish community for Python developers to grow skills and professional contacts.
- [pythonbasics.org](https://pythonbasics.org/) - Free Python tutorials covering basics, Flask, Django, Pandas and Selenium.
