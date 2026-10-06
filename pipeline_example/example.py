from pathlib import Path

from pipeline.analysis import Analysis
from pipeline.data.csv import DataCSV
from pipeline.data.synthetic import DataSynthetic
from pipeline.models.sawtooth import ModelSawtooth
from pipeline.models.cosine import ModelCosine
from pipeline.plots.line import PlotLine
from pipeline.plots.error import PlotError


# We want to compare how well our methods work on known synthetic data, then try applying them to real data.
for model, title in zip(
    [ModelSawtooth(), ModelCosine()],
    ["Synthetic triangle", "Synthetic cosine"],
):
    analysis = Analysis(
        title=title,
        data=DataSynthetic(num_points=20),
        model=model,
        plots=[PlotError],
    )
    analysis.run()

# We can compare the figures and see how well the differing models worked.
# The sawtooth/triangle wave one works surprisingly well! Why?
analysis = Analysis(
    title="Test synthetic triangle",
    data=DataSynthetic(num_points=100),
    model=ModelSawtooth(),
    plots=[PlotLine],
)
analysis.run()
# ...because actually it picks a slightly-less-than 1 period wavelength,
# and optimises to fit the flatter slopes of the edges of the cosine with the end of the previous wave and the start of the next wave.
# If we used many more points, that would show, you can play around with `num_points` to check.
# I wasn't expecting that, and it's a good reminder of how machine learning is very good at producing plausible-looking but wrong results.

# Now we've gotten an idea of how well they work on 'fake' data, let's compare them to real data!
# ...we have no real data so we're going to make some noisy fake data then pretend it's real.
# (There are people who do this in actual publications, please don't)
noisy_synthetic = DataSynthetic(0.1)
noisy_synthetic.load()
noisy_synthetic.to_csv(Path("real-data.csv"))  # We use Paths as they're system-agnostic!

# We load our 'real data'...
real_data = DataCSV(Path("real-data.csv"))
real_data.load()

for model, title in zip(
    [ModelSawtooth(), ModelCosine()],
    ["Real triangle", "Real cosine"],
):
    analysis = Analysis(
        title=title,
        data=real_data,
        model=model,
        plots=[PlotLine, PlotError],
    )
    analysis.run()

# And we can see how well each model fits it.
