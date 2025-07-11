# Machine Translation for Middle Eastern Languages

This repository provides data and codes of the paper entitled ["Literary Translations and Synthetic Data for Machine Translation of Low-resourced Middle Eastern Languages"](Literary Translations and Synthetic Data for Machine Translation of Low-resourced Middle Eastern Languages) accepted at the International Conference on Spoken Language Translation (IWSLT 2025) 2025. 

This project is a follow-up of [PARME](https://github.com/DOLMA-NLP/PARME) where over 36,000 translation pairs are provided for eight low-resourced languages in the Middle East: Luri Bakhtiari, Gilaki, Hawrami, Laki Kurdish, Mazandarani, Southern Kurdish, Talysh and Zazaki. The current project extends the resources with sentences from literary works.

## Alignment
Given translations of novels or storybooks in one of the target languages, our objective is to align each translated sentence with the original text, mostly in English. To do so, we try two approaches:

- **Automatically align**: automatically align translation with the original sentences using bitext mining and embeddings. This is prone to mismatches.
- **Manually align**: manually align sentences/phrases in those books with their original sentences in English. This has the highest quality but costly and time-consuming! The following schema shows the actions that a human aligner should make:

<iframe frameborder="0" style="width:50;height:923px;" src="https://viewer.diagrams.net/?tags=%7B%7D&highlight=0000ff&edit=_blank&layers=1&nav=1&title=Diagram-en.drawio#R7V1Nc6M4EP01Ps6UEcjgYz68463dTG1VDps9bRFQbGYxcoE8dubXrzCSDW7ZZipB0hCSg1GDZNRP3erXkpKRe7fafcnD9fKBxiQdoXG8G7n3I4Q%2BYeTzj1LyWkmCiVcJFnkSVyLnKHhMfhAhHAvpJolJ0XiQUZqyZN0URjTLSMQasjDP6bb52AtNm9%2B6DhcECB6jMIXSv5OYLUUv8Pgon5NksZTf7IzFnVUoHxaCYhnGdFsTubORe5dTyqqr1e6OpKXypF6qer%2BduXt4sZxkrE2Fp69cGX84ruv8m2xnfvB1Xjx%2FEq18D9ON6PBMvC17lSrI6SaLSdnKeOTebpcJI4%2FrMCrvbjnoXLZkq5SXHH75QjMmUET7cpKmdzSl%2Bb4t9wWXv%2BK5mrz64fKC5fQ%2FUrsz2f%2FwO7C%2F8uVJzsiuJhL9%2F0LoirD8lT8i7049AYYYjc4kqMrbI7aOK55Z1nCV9UIxnBaHto8a5xdC6T8BAAIAzHsMABoHLQBAOgFwoQVkizQplgAG3kfW1HWYJouMX0dcI4Sr67bURMKdx424sUriuKx%2Bm5Mi%2BRE%2B75sqQVzTJGP7ruDbEb4v29owWlS4OQCGjGbkBEspOoW7LIt3Ru9iMv4JYhKdGmJTnYB50GJCbgarZABMbWIKwBxHJ2IYIHYXFoRLeP9v%2BMdDyCKrzK30elFAnl%2Bg%2F4xDErxETRydoPzKg5M%2BRVUxU%2F%2B8GfoOvu44PZ2oTj526IA8bDh08KEjdHqMAHBsSgS0xg4BUDeJOXsQRZqzJV3QLExnR%2BltE5DjM39SuhYwfCOMvQocSj%2FVBInsEvZUu%2F6nbOozFqX7nWh5X3iVhYx396leqNUqi8dq%2B5Ksdxa2gm7yiFxQzbR6joX5grALz8mJqFTcxVGQkzRkyfcmLXt3RKeanVqMSRB7KtMJ0LP7bqaDrOM9EndtxEeTpr2xf13TWp2UAzn%2BYxlAZREpbAq62oXMbgfBFQ9Em%2BYRKCJmvdYB0wIPYbYJy4p7va%2FK3g7g7X1bcBU8pJXuODClIPgOEnyH8EnRJvSs5DtNVD1HYZNa%2BY4DEw8CVreC9XGdJlYZ5S8A62Rq3NXC7MQcdRqJ2EajpqZplANTCXP3I0HgGmeyjg%2F0PVBZqRsRwV%2FnsoI9WsJl5Xv3ncyaz8Q5MG0wd%2Fa9HfO5pPrs1qEZYrfmU3AI5hFmfc6Cgjy055qOoBBMMHyoNWwlAnqNAKYLZn2OYaERGM%2FYIMU%2Bgj7HsAACbN4PQYIOACBZfFPuChsd8lNxWCwPfLem%2FSZUdZqMD7qVO8LQJZ1ejQZrCsMKfUlZ66BRfMNfZbLgAvU%2BbEyTbVSBsKh2xAK0hPBpAHbaUhUpg5b2qB46%2FgagIWUfgD4PNPbxOwENWuoa6AnEdWClQjciEr%2FKSlHQcnjqYaUIbluYCa40E1yp44nTEE21IFCHCYFerrlaEJDr3kdgWzCoyilrHevyyz7s7iglBHp3VkN9D7O31A1qOXu7rlWzt3xvfek2Q7O1BR4MZhQ69mCGpmsLPJU3eKqzusFtPZVvl6eCSYKOc6KGPNUEm%2BYVrmL9vltVWxZrKSHQ68EUhwF6MdpPJwsLVK1YVu8zswDkzlcdKNPrcBTr7T1GAPgbJQJajUA2PERMCt3Iv1NwLWLykFURk3zv3nM78w5MIt97bmeBp4KLCYOnkrrx2noqbJengiv9%2FeR2vm86C%2BVp3x5vylOpVK3XUylO1PeZRkNiYX60QxoNZ49hZ8nhqJ0bfJZp6jdvLlE11vH%2BEg9SeXGky6uOdP2%2ByGg%2BHNW7bMano2Jq%2FKiep9yPr8WTnveY53zse0xm40lzMgsmpsNu6XIM5IQvQMBryKFf0LTsgFZYlJahFxbFXn1N25QthsW8tcB8gK6cshGH5UzRyeSvgkBr6IcVG%2Fj7HX2jFtO2XggUtP6jOScIi3nLUKQAepmstCBqUq6kW3KAVGUJXcBgwXQ8nIY%2Fr5u2p%2BGxXTljrH3ZXlfO2L5QSrH7veNQKohIFKlU%2FRxgD18c8W9QtfmQSWI9eCqFbtquw8tZ1xJPNYEc3fyJqK4mf2BSHXovXjz%2Bu4Uqh3z8pxXu7H8%3D"></iframe>

## Resources
### Datasets for reproducibility
In the paper, we report experiments using different alignment techniques, mostly relying in automatic alignment and LLMs, respectively referred to as `V` and `L`. However, by the time the paper was reviewed, we had manually aligned most of the automatically-aligned sentences! As such, there is no need specifically employ the datasets used in the paper, unless you are interested in the reproducibility of our experiment results.

The datasets with different shuffling seed keys used in the paper are provided in [datasets/reproducible_datasets.7z](datasets/reproducible_datasets.7z).



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
