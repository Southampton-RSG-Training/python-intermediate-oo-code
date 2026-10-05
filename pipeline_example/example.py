from pathlib import Path

from pipeline.analysis import Analysis
from pipeline.data.csv import DataCSV
from pipeline.data.synthetic import DataSynthetic
from pipeline.models.sawtooth import ModelSawtooth
from pipeline.models.cosine import ModelCosine
from pipeline.plots.line import PlotLine
from pipeline.plots.error import PlotError


noisy_synthetic = DataSynthetic(0.1)
noisy_synthetic.load()
noisy_synthetic.to_csv(Path("real-data.csv"))  # We use Paths as they're system-agnostic!

real_data = DataCSV(Path("real-data.csv"))
real_data.load()

for model, title in zip(
    [ModelSawtooth(), ModelCosine()],
    ["Synthetic sawtooth", "Synthetic cosine"],
):
    analysis = Analysis(
        title=title,
        data=DataSynthetic(),
        model=model,
        plots=[PlotLine, PlotError]
    )
    analysis.run()


analysis = Analysis(
    title="Real sawtooth",
    data=noisy_synthetic,
    model=ModelSawtooth(),
    plots=[PlotLine, PlotError],
)
analysis.run()
