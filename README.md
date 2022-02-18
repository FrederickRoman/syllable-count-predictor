# syllable-count-predictor
Neural network model that predicts the number of syllables in an English word. It shows its creation end-to-end: from data collection to evaluation of various models. One of the explored models is used in the [Readgauge app](https://readscale.netlify.app).

## Getting Started

This project is self-contained. It has both the data and the code. All you need to do is to meet the prerequisites. 

### Prerequisites

Python>=3.8.6

```
nltk
pandas 
numpy 
tensorflow 
```
### Preprocessing
#### Syllable count dictionary creation
Run the jupyter notebook cells in train.ipynb under [/preprocess/syllable_count_dict_creation](https://github.com/FrederickRoman/syllable-count-predictor/blob/main/ML/preprocess/syllable_count_dict_creation/syllable_count_dict_creation.ipynb)
#### Synthetic syllable count dictionary creation (for data augmentation)

```
python ./ML/preprocess/data_synthesizer/data_synthesizer.py 
```

### Training
Run the jupyter notebook cells in train.ipynb under [training/feedforward](https://github.com/FrederickRoman/syllable-count-predictor/blob/main/ML/training/feedforward/ff_on_natural_data/train.ipynb) or under [training/blstm](https://github.com/FrederickRoman/syllable-count-predictor/blob/main/ML/training/blstm/blstm_on_natural_data/train.ipynb).


## External deployment (not on this repo)

These model were trained to find one to be integrated to to the [Readgauge](https://readscale.netlify.app) client-side web app. It runs live [here](https://readscale.netlify.app) and its repository is [here](https://github.com/FrederickRoman/Readgauge).

<div style="display:flex; flex-direction:column;">
<img src="https://github.com/FrederickRoman/Readgauge/blob/main/public/android-chrome-512x512.png" alt="Readgauge logo" height="200"/>
<img src="https://github.com/FrederickRoman/Readgauge/blob/main/docs/mockups/Home_Nest%20Hub.png" height="200" alt="Results mockup"/>
</div>

### Data source

The syllableCountDict dataset contains the syllable count of each word

It was created using [nltk's built-in CMU dictionary](https://www.nltk.org/_modules/nltk/corpus/reader/cmudict.html).

The Carnegie Mellon Pronouncing Dictionary [cmudict.0.6]
Copyright 1998 Carnegie Mellon University
