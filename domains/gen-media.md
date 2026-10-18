# Generative image, video and audio

[Back to the index](../README.md)

## In short

Generative media went from research code (latent diffusion, 2022) to hosted products in about three years. Two ways of working coexist.

- **Local and open.** Stable Diffusion and Flux models run on a consumer GPU through ComfyUI (node graphs, reproducible workflows) or AUTOMATIC1111 (forms and extensions). ControlNet adds control over pose, depth and edges; LoRA and DreamBooth teach a model a person, product or style from a few images. Civitai is where community models live.
- **Hosted and fast.** For video, voice and the newest image models, APIs win: fal.ai, Replicate and similar platforms expose hundreds of models behind one interface and charge per output. Kling, Wan, Vidu and HeyGen cover text-to-video and talking avatars.
- **Video is still the hard part.** Short clips are easy; consistency across shots, characters and lip sync is where most tools fail. Plan scenes as separate generations and stitch them.
- **Audio is the quiet win.** Open voice models (VibeVoice) and tools like ebook2audiobook make narration practical at home; Udio and similar services cover music.
- **Read the papers once.** The latent diffusion paper and the DreamBooth page explain why the tools behave as they do, which helps when tuning.

**Where to start:** ComfyUI with its examples page for local image work, fal.ai for API access to video and image models, Civitai for models.

## Contents

- [Image generation](#image-generation)
- [Stable Diffusion and ComfyUI tooling](#stable-diffusion-and-comfyui-tooling)
- [Video generation](#video-generation)
- [Platforms and APIs](#platforms-and-apis)
- [Audio, voice and music](#audio-voice-and-music)
- [Learning and prompts](#learning-and-prompts)

## Image generation

- [CompVis stable-diffusion](https://github.com/CompVis/stable-diffusion) - Official GitHub repository of the Stable Diffusion latent text-to-image model.
- [denoising-diffusion-pytorch](https://github.com/lucidrains/denoising-diffusion-pytorch) - PyTorch implementation of Denoising Diffusion Probabilistic Models.
- [DreamBooth project page](https://dreambooth.github.io/) - Project page for DreamBooth, the method for personalizing text-to-image diffusion models.
- [Latent Diffusion paper (arXiv)](https://arxiv.org/abs/2112.10752) - arXiv abstract page for the latent diffusion paper behind Stable Diffusion.
- [latent-diffusion](https://github.com/CompVis/latent-diffusion) - Official code for High-Resolution Image Synthesis with Latent Diffusion Models by CompVis.
- [OmniGen](https://github.com/VectorSpaceLab/OmniGen) - Unified image generation model and code by VectorSpaceLab.
- [DeepFloyd IF](https://github.com/deep-floyd/IF) - Repository of the DeepFloyd IF open text-to-image diffusion model.
- [flowty-realtime-lcm-canvas](https://github.com/flowtyone/flowty-realtime-lcm-canvas) - Realtime sketch-to-image demo using LCM and the Gradio library.
- [Ideogram](https://about.ideogram.ai/1.0) - Ideogram AI image generation model, now on its 4.0 version page.
- [Lexica](https://lexica.art/) - AI image generator with a searchable index of Stable Diffusion prompts.
- [maple-diffusion](https://github.com/madebyollin/maple-diffusion) - Stable Diffusion inference on iOS and macOS using Apple's MPSGraph.
- [neural-style-tf](https://github.com/gordicaleksa/neural-style-tf/blob/master/neural_style.py) - TensorFlow implementation of neural style transfer by Aleksa Gordić.
- [stable-diffusion-tensorflow](https://github.com/divamgupta/stable-diffusion-tensorflow) - Stable Diffusion implementation in TensorFlow and Keras.
- [stable_diffusion_playground](https://github.com/gordicaleksa/stable_diffusion_playground) - Experiments with Stable Diffusion that save metadata for reproducible generation and interpolation.
- [Text-to-image models (HF)](https://huggingface.co/models?pipeline_tag=text-to-image&sort=likes) - Hugging Face listing of text-to-image models sorted by likes.

## Stable Diffusion and ComfyUI tooling

- [AUTOMATIC1111 stable-diffusion-webui](https://github.com/AUTOMATIC1111/stable-diffusion-webui) ⭐ - Browser UI for running Stable Diffusion locally, with a large extension ecosystem.
- [ComfyUI](https://github.com/comfyanonymous/ComfyUI) ⭐ - Modular node-based GUI and backend for running diffusion models locally.
- [Civitai](https://civitai.com/) - Community hub for sharing Stable Diffusion and Flux models, embeddings and AI art.
- [ComfyUI examples](https://comfyanonymous.github.io/ComfyUI_examples) - Collection of example ComfyUI node workflows for diffusion models.
- [ControlNet 1.1 nightly](https://github.com/lllyasviel/ControlNet-v1-1-nightly) - Nightly release of ControlNet 1.1, the conditioning model for diffusion image generation.
- [Diffusers loading guide](https://huggingface.co/docs/diffusers/using-diffusers/loading) - Hugging Face documentation on loading pipelines, models and schedulers in diffusers.
- [InvokeAI](https://github.com/invoke-ai/InvokeAI) - Creative engine and web UI for running Stable Diffusion models for image generation.
- [sd-webui-controlnet](https://github.com/Mikubill/sd-webui-controlnet) - WebUI extension adding ControlNet conditioning to Stable Diffusion.
- [AVeryComfyNerd](https://github.com/nerdyrodent/AVeryComfyNerd) - GitHub collection of ComfyUI workflows and related resources.
- [civitai (GitHub)](https://github.com/civitai/civitai) - Source repository of the Civitai platform for models and textual inversions.
- [DiffusionBee](https://github.com/divamgupta/diffusionbee-stable-diffusion-ui) - Desktop app to run Stable Diffusion locally on Apple Silicon Macs with an installer.
- [fast-DreamBooth notebook](https://colab.research.google.com/github/TheLastBen/fast-stable-diffusion/blob/main/fast-DreamBooth.ipynb) - Google Colab notebook for fast DreamBooth fine-tuning of Stable Diffusion.
- [Stable Diffusion Playground](https://github.com/Logeswaran123/Stable-Diffusion-Playground) - App for generating images and videos with Stable Diffusion models.
- [Sygil-Dev webui](https://github.com/Sygil-Dev/Sygil-WebUI) - Stable Diffusion web UI project; activity level not verified.

## Video generation

- [CogVideo](https://github.com/THUDM/CogVideo) - Text and image to video generation models: CogVideoX and CogVideo.
- [Synthesia](https://www.synthesia.io/) - AI video platform that generates presenter videos from text with avatars.
- [HeyGen](https://www.heygen.com/) - AI video platform for creating videos with a personal avatar.
- [huobao-drama](https://github.com/chatfire-AI/huobao-drama/tree/master) - AI platform that turns a one-sentence idea into a short drama, from script to final video.
- [Immersity (LeiaPix)](https://www.leiapix.com/) - Converts 2D photos into 3D depth animations with AI.
- [Invideo AI](https://invideo.io/) - AI video creator that turns text prompts into edited videos.
- [Kaiber](https://www.kaiber.ai/superstudio) - AI video generation platform with its Superstudio creative tool.
- [Kling AI](https://www.klingai.com/) - AI video and image generation platform.
- [OpusClip](https://www.opus.pro/) - AI tool that turns long videos into short clips for social platforms.
- [Pyramid Flow SD3](https://huggingface.co/rain1011/pyramid-flow-sd3) - Model weights for Pyramid Flow video generation, SD3-based variant, on Hugging Face.
- [Replicate text-to-video collection](https://replicate.com/collections/text-to-video) - Collection of text-to-video models runnable through Replicate's API.
- [Vidu](https://www.vidu.studio/) - AI video generator from text prompts, images and reference clips.
- [Wan AI](https://wanxai.com/) - Platform for AI text-to-image and text-to-video generation models.

## Platforms and APIs

- [fal.ai](https://fal.ai/) - Inference platform hosting over 1,000 generative media models behind one API.
- [Decart](https://platform.decart.ai/) - API platform for real-time AI video and image generation.
- [DreamStudio](https://dreamstudio.com/create) - Stability AI web app for generating images with Stable Diffusion models.
- [getimg.ai](https://getimg.ai/) - Web platform for creating images, video, music and speech with several AI models.
- [GoAPI](https://goapi.ai/) - Unified API provider for Midjourney, GPT, Stable Diffusion and DALL-E models.
- [Krea](https://www.krea.ai/home) - AI image and video generation platform with a creative editing workspace.
- [Leonardo.ai](https://leonardo.ai/) - AI image generation platform; page blocked, judged from title.
- [PiAPI](https://piapi.ai/) - Hub offering APIs for AI video, image, music and 3D generation across 50+ models.
- [Scenario](https://www.scenario.gg/) - Platform for generating game assets with AI image, video, 3D and audio models.
- [Stability AI](https://stability.ai/) - Homepage of Stability AI, maker of Stable Diffusion models and tools.
- [Tensor.Art](https://tensor.art/) - Free online image generator and model hosting site; blocked, judged from title.
- [ThinkDiffusion](https://www.thinkdiffusion.com/) - Cloud workspaces for Stable Diffusion, ComfyUI, Flux and other generative AI apps.

## Audio, voice and music

- [ebook2audiobook](https://github.com/DrewThomasson/ebook2audiobook) - Converts ebooks into chaptered audiobooks with AI voice models and voice cloning.
- [Strudel](https://strudel.cc/) - Browser-based live coding environment for making music with patterns.
- [VibeVoice](https://github.com/microsoft/VibeVoice) - Open-source voice AI models from Microsoft for speech generation.
- [AssemblyAI](https://www.assemblyai.com/) - Speech-to-text and audio understanding API for developers.
- [LALAL.AI](https://www.lalal.ai/) - Online AI tool for separating vocals from instrumental tracks.
- [Riverside](https://riverside.fm/) - Online studio for high-quality podcast and video recording and editing.
- [SOUNDRAW](https://soundraw.io/) - AI music generator for royalty-free tracks with stem downloads.
- [Udio](https://www.udio.com/) - AI music generation platform for creating songs from text prompts.
- [voicebox](https://github.com/jamiepine/voicebox) - Open-source voice studio for cloning voices and generating speech, powered by Qwen3-TTS.

## Learning and prompts

- [AI generative art tools](https://pharmapsychotic.com/tools.html) - List of generative AI art tools and utilities.
- [DiffusionDB](https://github.com/poloclub/diffusiondb) - Large-scale dataset of text-to-image prompts and images generated with Stable Diffusion.
- [Personal embeddings training guide](https://bennycheung.github.io/stable-diffusion-training-for-embeddings) - Blog post on training personal textual-inversion embeddings for Stable Diffusion.
- [PromptHero](https://prompthero.com/) - Search engine and gallery of AI image prompts for Stable Diffusion and Midjourney.
- [promptoMANIA](https://promptomania.com/) - Prompt builder and AI art community with model directory and guides.
- [SD resource goldmine](https://rentry.org/sdgoldmine) - Community list of Stable Diffusion resources hosted on Rentry.
- [Stable Diffusion Art](https://stable-diffusion-art.com/) - Tutorial and prompt site about Stable Diffusion; blocked, judged from title.
- [Tryolabs fine-tuning guide](https://tryolabs.com/blog/2022/10/25/the-guide-to-fine-tuning-stable-diffusion-with-your-own-images) - Guide to fine-tuning Stable Diffusion with Dreambooth on your own images.
