# Graphics, shaders and game dev

[Back to the index](../README.md)

## In short

Real-time graphics rests on a small set of ideas: transform vertices, shade pixels, do it 60 times a second. The APIs change (OpenGL, WebGL, WebGPU), the ideas do not.

- **Shaders are the core skill.** Shadertoy is the playground and the best library of techniques; one fragment shader can hold a whole scene through ray marching.
- **Learn from people who explain the why:** Fabien Sanglard's engine source reviews, Paul Bourke's geometry pages, Amit Patel on pathfinding and grids, Catlike Coding for Unity and Godot, and the free book Game Programming Patterns.
- **Creative coding is the gentle entry.** Processing and its web descendants (OpenProcessing, Mr.doob's experiments) make it easy to sketch visuals; JS1k shows how much fits in one kilobyte.
- **Engines and libraries:** LWJGL and JogAmp for Java, libigl for geometry processing, Ren'Py for visual novels; for assets, OpenGameArt and Bfxr cover sprites and sound effects.
- **Fractals and generative art** sit where graphics meets math and the demoscene.

**Where to start:** Shadertoy, Game Programming Patterns, Fabien Sanglard.

## Contents

- [Game engines and frameworks](#game-engines-and-frameworks)
- [Creative coding and fractals](#creative-coding-and-fractals)
- [Game dev learning](#game-dev-learning)
- [3D and WebGL](#3d-and-webgl)
- [Shaders and GPU](#shaders-and-gpu)
- [Assets](#assets)

## Game engines and frameworks

- [AngelCode.com](http://www.angelcode.com/) - Game development tools and libraries, including AngelScript and BMFont.
- [Fabien Sanglard](http://fabiensanglard.net/) - Site with in-depth analyses of game engine and graphics source code.
- [LWJGL](http://www.lwjgl.org/) - Java bindings for OpenGL and other native APIs, used for game and graphics work.
- [Ren'Py](https://www.renpy.org/) - Open-source Python engine for building visual novels.
- [Electronic Arts](https://github.com/electronicarts) - Official GitHub organization of Electronic Arts, publishing open game development projects.
- [hagl](https://github.com/tuupola/hagl) - Hardware-agnostic graphics library for embedded displays.
- [libGDX users wiki](http://code.google.com/p/libgdx-users) - Archived community wiki and code for the libGDX Java game library.
- [libgdx-contribs](https://github.com/manuelbua/libgdx-contribs) - Contributions and utilities for the libGDX game framework.
- [Notch](https://www.notch.one/) - Real-time graphics tool for video production, live visual effects and VR.
- [playn](http://code.google.com/p/playn) - Java game framework deploying to JVM, HTML5, Android and iOS.
- [pygame Code Repository](http://www.pygame.org/pcr/repository.php) - Community repository of code and games for the pygame library.
- [Sauerbraten](http://sauerbraten.sourceforge.net/) - Open-source first-person shooter and its game engine.
- [The Powder Toy](https://github.com/The-Powder-Toy/The-Powder-Toy) - Open-source falling-sand physics sandbox in C++ and SDL, simulating air pressure and heat.

## Creative coding and fractals

- [Processing](http://processing.org/) ⭐ - Language and environment for learning to code through visual sketches.
- [JS1k](http://js1k.com/) - Annual JavaScript code golf competition where entries must fit in 1 KB.
- [mixbox](https://github.com/scrtwpns/mixbox) - Library for natural color mixing that models real pigments.
- [Mr.doob](http://mrdoob.com/) - Collection of digital toys and experiments by Mr.doob, creator of Three.js.
- [1k Mandelbrot demo tutorial](https://www.geeks3d.com/20110214/how-to-create-a-1k-mandelbrot-demo-in-opengl-c-with-source-code) - Tutorial on building a 1k Mandelbrot demo in OpenGL and C++.
- [Chrome Experiments](http://www.chromeexperiments.com/) - Gallery of web experiments built with Chrome and web technologies.
- [CreativeJS](http://creativejs.com/) - Showcase and news on creative JavaScript and HTML5 projects.
- [JH Labs](http://www.jhlabs.com/) - Java image-processing filters and effects by Jerry Huxtable.
- [Moebio](https://moebio.com/) - Portfolio of data visualization and math-driven art projects by Santiago Ortiz.
- [OpenProcessing](http://www.openprocessing.org/browse) - Community site for sharing and running Processing sketches.
- [Processing.js](http://processingjs.org/) - JavaScript port of the Processing visualization language.
- [RiTa](http://www.rednoise.org/rita) - JavaScript toolkit for generative language and text tools.

## Game dev learning

- [Amit Patel home page](http://www-cs-students.stanford.edu/~amitp) - Personal homepage of Amit Patel, known for game dev and pathfinding articles.
- [Catlike Coding](https://catlikecoding.com/) - Tutorials on game development with Unity and Godot.
- [Game Programming Patterns](http://gameprogrammingpatterns.com/contents.html) - Free online book on design patterns for game programming.
- [noclip](https://noclip.website/) - Digital museum for exploring video game levels in the browser.
- [Aurelien Ribon blog](http://www.aurelienribon.com/blog) - Personal blog of game developer Aurelien Ribon.
- [Blackpawn](http://www.blackpawn.com/) - Personal site with 3D graphics and game programming tutorials.
- [Coding Labs](http://www.codinglabs.net/) - C++ tutorials on game and engine programming with DirectX and OpenGL.
- [Game Developer (ex-Gamasutra)](http://www.gamasutra.com/) - Game industry news and analysis, formerly known as Gamasutra.
- [Game Development Stack Exchange](http://gamedev.stackexchange.com/) - Q&A site for game development questions.
- [GameDev.net](http://www.gamedev.net/) - Long-running game development community with articles and forums.
- [Gemserk blog](http://blog.gemserk.com/) - Blog of Gemserk, an indie game development studio.
- [Indie DB](http://www.indiedb.com/) - Community site for indie game developers to publish and find games.

## 3D and WebGL

- [JogAmp](http://jogamp.org/) - Java libraries exposing OpenGL, OpenCL, OpenAL and media processing.
- [libigl](https://libigl.github.io/) - C++ library for geometry processing.
- [Mesh2Motion](https://gamefromscratch.com/mesh2motion-free-open-source-animation-app) - Free, open-source browser tool for adding animation to 3D models.
- [Paul Bourke](http://paulbourke.net/) - Long-running reference site on computer graphics, 3D and visual techniques.
- [AlteredQualia](http://alteredqualia.com/) - Personal site with WebGL experiments and computer graphics work.
- [Learn OpenGL ES](http://www.learnopengles.com/) - Tutorials on OpenGL ES for Android and WebGL for the web.
- [OpenCSG](http://www.opencsg.org/) - Library for rendering constructive solid geometry with OpenGL.
- [WebGL / WebGPU Community](http://www.webgl.com/) - Community resource with tutorials and examples for WebGL and WebGPU.

## Shaders and GPU

- [Shadertoy](https://www.shadertoy.com/) ⭐ - Online community and playground for sharing GLSL fragment shaders.
- [Adam Sawicki homepage](http://www.asawicki.info/) - Personal site on graphics, GPU programming and game development.
- [GLSL lesson (cpp0x.pl)](http://cpp0x.pl/kursy/Kurs-OpenGL-C++/GLSL/243) - Polish-language GLSL lesson from an OpenGL and C++ course.
- [NVIDIA Developer](http://developer.nvidia.com/) - NVIDIA developer resources for GPU programming, CUDA and graphics SDKs.
- [Lighthouse3D GLSL tutorial](http://www.lighthouse3d.com/tutorials/glsl-tutorial) - Tutorial on GLSL shader programming with OpenGL.
- [oZone3D.Net](http://www.ozone3d.net/tutorials) - Tutorials on OpenGL, GLSL and graphics card programming.

## Assets

- [Bfxr](http://www.bfxr.net/) - Browser tool for generating retro sound effects for games, based on sfxr.
- [OpenGameArt.org](http://opengameart.org/) - Community site with free game art, sprites, music and sound effects under open licenses.
- [Fedit Image Editor](https://github.com/f055/fedit-image-editor) - Lightweight single-executable image editor for Windows, built in C++ with WinAPI.
- [Free Game Arts](http://freegamearts.tuxfamily.org/) - Free game art assets for game developers.
