# Object-Oriented Python Demo

This repo contains a couple of demo packages designed to show more or less what OO looks like in Python. I made them in a bit of a rush, and there's a focus on showing a useful set of features, not necessarily on being the *best* way of doing things in OO. There's always a tension with 'toy' examples between exhibiting as many features as possible, and not making something so convoluted that the features seem unhelpful - I may not have come down on the right side!

## Getting Started

Clone the repo to your machine:

```bash
git clone https://github.com/Southampton-RSG-Training/python-intermediate-oo-code
```

Then set up a virtual environment and install the prerequisites:

```bash
cd python-intermediate-oo-code
python -m venv venv
source venv/bin/activate (or Scripts/activate on windows)
pip install -r requirements.txt
```

## Packages

The demo packages are based on the two examples in the slides, though there's some small differences in places just because it worked better.

The code for both is set up as a directory that functions as an importable package,
and an `example.py` file that shows how you might call it.

### University Example

The `university_example` directory contains code that basically covers the examples of staff in a university, teaching courses and publishing papers. The files are structured with a focus on what concepts they're demonstrating, rather than how they'd be in a real codebase.

You can enter into the directory and run the example:

```bash
cd university_example
python example.py
```

(If you try and run from another directory, it won't find the `university` package! Proper installable packages are a whole other topic)

Then poke around the code and try to map your understanding of what happened to the model structure.

### Pipeline Example

The `pipeline_example` directory contains code that covers the example of a pipeline fitting models to data and plotting results. In this case, the 'data' is a cosine-like wave (OK, actually a cosine wave) and we experiment with fitting triangle and cosine waves to it.

The code is structured in a more 'realistic' way, and is type-hinted.
It's a little convoluted in order to show off all the features.

You can enter into the directory and run the example (don't forget to `cd ..` if you were in the `university_example` directory!):

```bash
cd pipeline_example
python example.py
```

It'll pop up some plots, and save some figures. Then you can scope out the structure that resulted in it.

## Feedback

I'd like to write this up into a proper lesson at some point, and you can help me get a jump start on it by letting me know if there's bits of this that are confusing/unhelpful/wrong or conversely, bits you thought worked well. Just open an issue on the repo.

Actually writing the lesson means getting the £££... (I wish we lived in the world the papers pretend we do where academics get buckets of cash to do whatever they want).
