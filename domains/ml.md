# Machine learning foundations

[Back to the index](../README.md)

## In short

Machine learning foundations change slowly, which is why this page holds some of the oldest links in the list and they still work.

- **Learn by building.** fast.ai (top-down, practical) and Karpathy's Neural Networks: Zero to Hero (bottom-up, from backprop to GPT) are the two best free courses and complement each other.
- **See it move.** TensorFlow Playground and the Neural Network Zoo give intuition that formulas do not.
- **Data first.** Kaggle, Common Crawl and Roboflow Universe are where datasets live; for Polish text, the National Corpus of Polish (NKJP) and Morfologik are the standard resources.
- **Tools you will meet:** TensorFlow and Keras, Gradio for demos, Weights & Biases for tracking experiments, Netron for inspecting model files.
- **Classic techniques still pay.** OCR (Tesseract), term vectors and latent semantic analysis solve many text problems more cheaply than an LLM.

**Where to start:** fast.ai, then Zero to Hero, then a Kaggle competition.

## Contents

- [Courses and tutorials](#courses-and-tutorials)
- [Libraries and tools](#libraries-and-tools)
- [Datasets](#datasets)
- [NLP and text](#nlp-and-text)
- [Research](#research)
- [Computer vision and OCR](#computer-vision-and-ocr)

## Courses and tutorials

- [fast.ai course](https://course.fast.ai/) ⭐ - Free practical deep learning course for people with coding experience.
- [Neural Networks: Zero to Hero](https://karpathy.ai/zero-to-hero.html) ⭐ - Andrej Karpathy's course building neural networks and GPT-style models from scratch.
- [TensorFlow Playground](http://playground.tensorflow.org/) ⭐ - Interactive browser visualization for training small neural networks.
- [awesome-datascience](https://github.com/academic/awesome-datascience) - Curated list of data science learning resources and real-world project examples.
- [Shervine Amidi cheatsheets](https://stanford.edu/~shervine) - Stanford-hosted cheatsheets for machine learning and deep learning by Shervine Amidi.
- [TensorFlow Core tutorials](https://www.tensorflow.org/tutorials) - Official TensorFlow tutorials covering Keras, data loading and model training.
- [TensorFlow-Examples](https://github.com/aymericdamien/TensorFlow-Examples) - TensorFlow tutorials and example code for beginners, covering TF v1 and v2.
- [Transformers-Tutorials](https://github.com/NielsRogge/Transformers-Tutorials) - Jupyter notebook demos built with the Hugging Face Transformers library.
- [AI and ML cheat sheets (Kojouharov)](https://becominghuman.ai/cheat-sheets-for-ai-neural-networks-machine-learning-deep-learning-big-data-678c51b4b463) - Collection of AI, neural network and machine learning cheat sheets on Medium.
- [AlphaGo Zero explained (Medium)](https://medium.com/applied-data-science/alphago-zero-explained-in-one-diagram-365f5abf67e0) - Medium article explaining AlphaGo Zero in one diagram; page blocked, judged from title.
- [CNN chapter (Medium)](https://medium.com/deep-math-machine-learning-ai/chapter-8-0-convolutional-neural-networks-for-deep-learning-364971e34ab2) - Medium article chapter on convolutional neural networks; page blocked, judged from title.
- [Data mining resources (wyklady.org)](http://data-mining.wyklady.org/) - Polish resource on data mining theory, articles, scripts and algorithms.
- [Kaggle cheat sheets thread](https://www.kaggle.com/general/298280) - Kaggle discussion listing cheat sheets for deep learning, Keras, TensorFlow and PyTorch.
- [Machine Learning Exposed workshop](http://slides.com/javafxpert/machine-learning-exposed-workshop-part-one) - Introductory workshop slides on machine learning with light math.
- [Microsoft Learn: AI on Azure](https://learn.microsoft.com/pl-pl/training/paths/get-started-with-artificial-intelligence-on-azure) - Free Microsoft Learn path introducing AI apps and agents on Azure.
- [ml-road](https://github.com/yanshengjia/ml-road) - Collection of machine learning and agentic AI resources, practice and research notes.
- [Paperspace Blog](https://blog.paperspace.com/) - Tutorials and sample apps on machine learning and GPU cloud from Paperspace.
- [San Diego Machine Learning (YouTube)](https://www.youtube.com/@SanDiegoMachineLearning/videos) - YouTube channel with machine learning videos and talks.
- [TensorFlow Hub tutorials](https://www.tensorflow.org/hub/tutorials) - Tutorials for using and adapting pre-trained models from TensorFlow Hub.
- [Transfer learning in Python (Domino)](https://www.dominodatalab.com/blog/transfer-learning-in-python) - Hands-on tutorial on transfer learning in Python; page empty, judged from title.

## Libraries and tools

- [TensorFlow](https://www.tensorflow.org/) ⭐ - Homepage of TensorFlow, the open-source machine learning platform.
- [FANN](http://leenissen.dk/fann) - Fast multilayer artificial neural network library written in C, with bindings for many languages.
- [Gradio](https://gradio.app/) - Python library for building and sharing web demos of machine learning models.
- [Keras](https://keras.io/) - Official site and documentation of Keras, a high-level deep learning API.
- [Netron](https://github.com/lutzroeder/Netron) - Viewer for neural network, deep learning and machine learning model graphs.
- [Weights & Biases](https://wandb.ai/site) - Developer platform for experiment tracking, model evaluation and LLM application monitoring.
- [Cleora](https://cleora.ai/) - CPU-only Rust engine for graph embeddings using sparse Markov propagation.
- [ml_forge](https://github.com/zaina-ml/ml_forge) - Visual graph node editor for training computer vision models.
- [pipefunc](https://github.com/pipefunc/pipefunc) - Lightweight Python library for building function pipelines (DAGs) for scientific and HPC workflows.
- [pix2pix-tensorflow](https://github.com/affinelayer/pix2pix-tensorflow) - TensorFlow port of the pix2pix image-to-image translation method.
- [tycoon-learning-environment](https://github.com/vrtnis/tycoon-learning-environment) - JAX learning environment for transport economy, route planning and cargo flow.

## Datasets

- [Kaggle](https://www.kaggle.com/) ⭐ - Platform for data science competitions, datasets, notebooks and ML benchmarks.
- [Common Crawl](https://commoncrawl.org/) - Open repository of web crawl data, free to access and analyze.
- [GeoNames](http://www.geonames.org/) - Geographical database of place names, coordinates and postal codes, with a free API.
- [gsm8k](https://huggingface.co/datasets/openai/gsm8k) - Grade-school math word problem dataset from OpenAI, a standard benchmark for LLM reasoning.
- [National Corpus of Polish (NKJP)](http://korpus.pl/) - National Corpus of Polish: a large, linguistically annotated corpus of contemporary Polish.
- [Roboflow Universe](https://universe.roboflow.com/) - Community hub of open-source computer vision datasets and models.
- [nikiv.dev datasets wiki](https://wiki.nikiv.dev/machine-learning/datasets) - Personal wiki page listing machine learning datasets.
- [RefinedWeb dataset (Falcon)](https://huggingface.co/datasets/tiiuae/falcon-refinedweb) - Hugging Face dataset page for the RefinedWeb web-text corpus used to train Falcon models.

## NLP and text

- [Morfologik](http://morfologik.blogspot.com/) - Polish morphological analyser and spell-checking dictionaries.
- [Term vector theory (miislita)](http://www.miislita.com/term-vector/term-vector-1.html) - Classic tutorial on term vector theory and keyword weights in information retrieval.
- [anonPL-300M](https://huggingface.co/cenkierpiotr/anonPL-300M) - Fine-tuned GLiNER model that flags personal data in Polish legal text, for human review.
- [Apache OpenNLP](http://opennlp.sourceforge.net/) - Java toolkit for NLP tasks such as tokenisation and named entity recognition.
- [Apache UIMA](http://uima.apache.org/) - Framework for building analysis pipelines over unstructured text content.
- [Latent semantic analysis (Wikipedia)](http://en.wikipedia.org/wiki/Latent_semantic_analysis) - Wikipedia article on latent semantic analysis, a classic technique for word and document similarity.
- [LSA word embedding tool (CU Boulder)](http://lsa.colorado.edu/) - University of Colorado tool for exploring word embeddings and latent semantic analysis.

## Research

- [Neural Network Zoo](https://www.asimovinstitute.org/neural-network-zoo) ⭐ - Asimov Institute's illustrated catalogue of neural network architectures with short descriptions.
- [CompVis (LMU Munich)](https://github.com/CompVis) - Computer vision and learning research group at LMU Munich, origin of the Stable Diffusion code.
- [facebookresearch](https://github.com/facebookresearch) - GitHub organization publishing Meta AI research code and models.
- [Papers With Code](https://paperswithcode.com/) - Papers With Code now redirects to Hugging Face trending papers.
- [Breaking a Visual CAPTCHA](http://www.cs.sfu.ca/~mori/research/gimpy) - Classic computer vision research page on breaking a visual CAPTCHA.
- [FedML](https://fedml.ai/) - Platform for federated learning and edge AI at scale.
- [Jason Yosinski](http://yosinski.com/deepvis) - Research portfolio of Jason Yosinski, including the deepvis work on neural network visualization.

## Computer vision and OCR

- [Tesseract OCR](https://code.google.com/p/tesseract-ocr) ⭐ - Open-source OCR engine that recognises text in images.
- [ALIPR / SIMPLIcity](http://wang.ist.psu.edu/IMAGE) - Penn State research technologies for content-based image retrieval and automatic image annotation.
- [OCRopus](https://code.google.com/p/ocropus) - Python tools for document analysis and OCR, now in archive form.
