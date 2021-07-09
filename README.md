# afib
Scores for Atrial Fibrillation

Includes scores for:
* Atrial Fibrillation Risk Index
* Postoperative Atrial Fibrillation 
* Alternative (New-onset) Postoperative Atrial Fibrillation 
* CHA₂DS₂-VASc
* Cardiac Anesthesia Risk Evaluation

For first time setup, run setup.py with `python3 setup.py develop`. 

# usage
Python 3.6 or greater is required. 
Also requires Numpy and Pytest, plus Bokeh if GUI will be used (can be installed with `pip`).

To see args for each risk score calculator, navigate to the respective file in `afib/risk_scores` and view docstrings.
Alternatively, install pydoc and run `python3 -m pydoc riskscore.py`, replacing riskscore with the file path.

A tests folder is included with examples.

## gui
GUI can be accessed by navigating to `afib/risk_scores/bokeh/gui.py`.
To run GUI, type the following in a terminal: `bokeh serve --show gui.py`.