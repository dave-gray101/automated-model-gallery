<h1 align="center">
  <br>
  <img height="300" src="https://github.com/go-skynet/model-gallery/assets/2420543/7a6a8183-6d0a-4dc4-8e1d-f2672fab354e"> <br>
  Automated <a href="https://github.com/go-skynet/LocalAI">LocalAI</a> Model Gallery
<br>
</h1>

The model gallery is an automatically updated collection of model and prompt configurations for the community of users of [LocalAI](https://github.com/go-skynet/LocalAI).

Please note that entries in this repository are generated automatically and may not always be correct! We encourage contributions to the gallery to correct these issues!

## Suggestions
While this scraper is automated, there is effort required to support new model card formats and to recognize different configurations. If a model you are interested in running is available on HuggingFace, but does not appear within this gallery, please submit a PR to create a new `config_recognizer` for it. Nontechnical users should create an issue on this repo, rather than LocalAI - if the missing models are interesting enough, someone will implement the recognizer.

## HuggingFace to LocalAI Configuration Scraper

This tool is intended to be used to generate best-effort LocalAI model configuration and prompt templating files automatically for models hosted on huggingface.com

Documentation is currently very incomplete, but here's some quick notes:

`main.py` in this directory is the entrypoint for the multiprocess master script. It is responsible for kicking off all child processes that actually handle the scraping and config file writing.

The `lib` directory holds the code that implements this scraping / conversion. This should only need to be edited if you like python and want to help improve the scraper or fix bugs

The `prompt_recognizers` directory currently only has a single known-working format in it, which is the one used by the model cards of prolific model converter TheBloke. Currently it comes in a strict form that actually checks its one of his, and a "style of" form that doesn't enforce any filtering. Please add more formats here if your model card uses a different style!

The `config_recognizers` directory has more to it, but is similarly incomplete. Files here are responsible for identifying the different model types used on huggingface, so please look at the examples in here and add more as new models come out every day.

## Using the Model Gallery 
For how to use the files in this repository, see the [Documentation](https://localai.io/models/).

For those used to the original go-skynet/model-gallery, this repository functions a little differently. Rather than have a single "huggingface" gallery containing many unrelated models, in this repository each repo on huggingface has an individual gallery - with options for each quanization level. In order to always track the latest updates for a given HF model, the `.ref` files within this repo provide a stable reference to the latest version of the yaml for that repo.
