# Machine Translation for Middle Eastern Languages

This repository provides data and code of the paper entitled [Literary Translations and Synthetic Data for Machine Translation of Low-resourced Middle Eastern Languages](https://sinaahmadi.github.io/docs/articles/ahmadi2025iwslt.pdf) accepted at the International Conference on Spoken Language Translation (IWSLT 2025) 2025. 

This project is a follow-up of [PARME](https://github.com/DOLMA-NLP/PARME) where over 36,000 translation pairs are provided for eight low-resourced languages in the Middle East: Luri Bakhtiari (`bqi`), Gilaki (`glk`), Hawrami (`hac`), Laki Kurdish (`lki`), Mazandarani (`mzn`), Southern Kurdish (`sdh`), Talysh (`tly`) and Zazaki (`zza`). The current project extends the resources with sentences from literary works.

## :triangular_ruler: Alignment
Given translations of novels or storybooks in one of the target languages, our objective is to align each translated sentence with the original one, mostly in English. To do so, we try two approaches:

- **Automatically align** align translation with the original sentences using bitext mining and embeddings. This is prone to mismatches.
- **Manually align** sentences/phrases in those books with their original sentences in English. This has the highest quality but costly and time-consuming! We do this as an additional step after automatically align. The following schema shows the actions that a human aligner should make (match, merge, split or ignore):

<p align="center" width="100%">
<img width="40%" src="manual-alignment-process.png" alt="loanwords">
</p>

## :gem: Resources
**The manually-aligned sentences can be found in the [datasets/manually-aligned](datasets/manually-aligned) folder.** This contains over 20,000 sentence pairs in English and one of the following languages:

- Gilaki-English:  1000 sentence pairs
- Hawrami-Central Kurdish:   318 sentence pairs
- Hawrami-English: 13843 sentence pairs
- Laki Kurdish-English:  1221 sentence pairs
- Southern Kurdish-English:  3683 sentence pairs

In addition, we provide two small corpora for Laki and Southern Kurdish in [corpora](corpora).

:point_right: In the [VecAlign](datasets/VecAlign) folder, there are files that need to be manually aligned. Feel free to do it and create a pull request.

### Datasets for reproducibility
In the paper, we report experiments using different alignment techniques, mostly relying on automatic alignment (`V`) and LLMs (`L`). However, by the time the paper was reviewed, we had manually aligned most of the automatically-aligned sentences. As such, there is no need to employ the datasets used in the paper, unless you are interested in the reproducibility of our experiment results. These datasets with different shuffling seed keys used in the paper are provided in [datasets/reproducible_datasets.7z](datasets/reproducible_datasets.7z).

## Licensing and Use

This dataset is derived from translated literary works, provided under agreement with the original publisher. It is in a format designed for research in language technology under the **Creative Commons Attribution 4.0 International (CC BY 4.0)** license. Please note that:

- The dataset **must not** be used to reconstruct the original literary works.
- You are free to share — copy and redistribute the material in any medium or format
- You are free to adapt — remix, transform, and build upon the material for any purpose, even commercially


## Cite this project

If you're using this project, please cite [this paper](https://sinaahmadi.github.io/docs/articles/ahmadi2025iwslt.pdf):

```
@inproceedings{ahmadi2025iwslt,
  title={Literary Translations and Synthetic Data for Machine Translation of Low-resourced {Middle Eastern} Languages},
  author={Ahmadi, Sina and Hameed, Razhan and Sennrich, Rico},
    booktitle = "Proceedings of the 63rd Annual Meeting of the Association for Computational Linguistics",
    year = "2025",
    address = "Vienna, Austria",
    publisher = "Association for Computational Linguistics"
}
```
